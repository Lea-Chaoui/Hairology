from flask import Flask, request, jsonify, render_template, redirect, session
import sqlite3
 

app = Flask(__name__)
app.secret_key = "secretkey123"  


def get_db():
    return sqlite3.connect("database.db")

# acceuil 

@app.route("/")
def index():
    return render_template("index.html")  

@app.route("/scan")
def scan_page():
    if "user_id" not in session:  
        return redirect("/login") 
    return render_template("scan.html")


# inscription
@app.route("/signup", methods=["GET", "POST"])
def signup():
    error = None
    if request.method == "POST":
        prenom = request.form["prenom"]
        nom = request.form["nom"]
        genre = request.form["genre"]
        type_cheveux = request.form["type_cheveux"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO users (prenom, nom, genre, type_cheveux, email, password)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (prenom, nom, genre, type_cheveux, email, password))
            conn.commit()
            conn.close()
            return redirect("/login")
        except sqlite3.IntegrityError:
            error = "Cet email est déjà utilisé."
            conn.close()

    return render_template("signup.html", error=error)

#connexion

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE email=? AND password=?", (email, password))
        row = cursor.fetchone()
        conn.close()

        if row:
            session["user_id"] = row[0]
            return redirect("/profil")
        else:
            error = "Email ou mot de passe incorrect."

    return render_template("login.html", error=error)

# profil

@app.route("/profil", methods=["GET", "POST"])
def profile():
    user_id = session.get("user_id")
    if not user_id:
        return redirect("/login")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT prenom, nom, genre, type_cheveux
        FROM users WHERE id=?
    """, (user_id,))
    row = cursor.fetchone()

    user = {
        "prenom": row[0],
        "nom": row[1],
        "genre": row[2],
        "type_cheveux": row[3],
    }

    cursor.execute("""
        SELECT p.id, p.nom, p.marque, up.date_scan, up.date_utilisation
        FROM products p
        JOIN user_products up ON up.product_id = p.id
        WHERE up.user_id = ?
    """, (user_id,))
    products = []
    for r in cursor.fetchall():
        products.append({
            "id": r[0],
            "nom": r[1],
            "marque": r[2],
            "date_ajout": r[3],
            "date_utilisation": r[4]
        })
    user["products"] = products

    conn.close()
    return render_template("profil.html", user=user)

# déconnexion 

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect("/login")

# scan , api

@app.route("/api/scan", methods=["POST"])
def scan_product():
    data = request.get_json()
    ean = data.get("ean")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, nom, marque FROM products WHERE ean = ?",
        (ean,)
    )
    product = cursor.fetchone()
    conn.close()

    if product:
        return jsonify({
            "status": "found",
            "product": {
                "id": product[0],
                "nom": product[1],
                "marque": product[2]
            }
        })

    return jsonify({"status": "not_found"})


@app.route("/analyze/<ean>", methods=["GET"])
def analyze_product(ean):
    conn = get_db()
    cursor = conn.cursor()


    cursor.execute("SELECT id, nom, marque FROM products WHERE ean=?", (ean,))
    prod = cursor.fetchone()
    if not prod:
        conn.close()
        return jsonify({"error": "Produit non trouvé"}), 404

    product_id, nom, marque = prod


    cursor.execute("""
        SELECT i.name
        FROM ingredients i
        JOIN product_ingredients pi ON i.id = pi.ingredient_id
        WHERE pi.product_id = ?
    """, (product_id,))
    ingredients = [row[0] for row in cursor.fetchall()]


    user_id = session.get("user_id")
    incompatibilities_found = []

    if user_id:
        cursor.execute("""
            SELECT i.name
            FROM ingredients i
            JOIN product_ingredients pi ON i.id = pi.ingredient_id
            JOIN user_products up ON up.product_id = pi.product_id
            WHERE up.user_id = ?
        """, (user_id,))
        user_ingredients = [row[0] for row in cursor.fetchall()]

        for ing_a in ingredients:
            ing_a_norm = ing_a.strip().lower()  # enlever espaces et mettre en minuscules
            for ing_b in user_ingredients:
                ing_b_norm = ing_b.strip().lower()

                cursor.execute("""
                    SELECT risk_level, description
                    FROM incompatibilities
                    WHERE (LOWER(TRIM(ingredient_a))=? AND LOWER(TRIM(ingredient_b))=?) 
                    OR (LOWER(TRIM(ingredient_a))=? AND LOWER(TRIM(ingredient_b))=?)
                """, (ing_a_norm, ing_b_norm, ing_b_norm, ing_a_norm))
                
                for row in cursor.fetchall():
                    incompatibilities_found.append({
                        "ingredient_a": ing_a,
                        "ingredient_b": ing_b,
                        "risk_level": row[0],
                        "description": row[1]
                    })


    conn.close()


    return jsonify({
        "id": product_id,  
        "nom": nom,
        "marque": marque,
        "ingredients": ingredients,
        "incompatibilities": incompatibilities_found
    })

@app.route("/add_to_collection", methods=["POST"])
def add_to_collection():
    if "user_id" not in session:
        return jsonify({"error": "Non connecté"}), 401

    data = request.get_json()
    product_id = data.get("product_id")
    user_id = session["user_id"]

    if not product_id:
        return jsonify({"error": "Produit non spécifié"}), 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO user_products (user_id, product_id, date_scan)
        VALUES (?, ?, CURRENT_TIMESTAMP)
    """, (user_id, product_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Produit ajouté à votre collection !"})

@app.route("/mark_used", methods=["POST"])
def mark_used():
    if "user_id" not in session:
        return jsonify({"error": "Non connecté"}), 401

    data = request.get_json()
    product_id = data.get("product_id")
    user_id = session["user_id"]

    if not product_id:
        return jsonify({"error": "Produit non spécifié"}), 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE user_products
        SET date_utilisation = CURRENT_TIMESTAMP
        WHERE user_id = ? AND product_id = ?
    """, (user_id, product_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Produit marqué comme utilisé !"})


@app.route("/add_product", methods=["POST"])
def add_product():
    data = request.get_json()
    ean = data.get("ean")
    nom = data.get("nom")
    marque = data.get("marque")
    ingredients_list = data.get("ingredients", [])

    if not ean or not nom:
        return jsonify({"error": "EAN et nom requis"}), 400

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO products (ean, nom, marque) VALUES (?, ?, ?)", (ean, nom, marque))
        product_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error": "Produit déjà existant"}), 400

    for ing in ingredients_list:
        cursor.execute("SELECT id FROM ingredients WHERE name=?", (ing,))
        row = cursor.fetchone()
        if row:
            ing_id = row[0]
        else:
            cursor.execute("INSERT INTO ingredients (name) VALUES (?)", (ing,))
            ing_id = cursor.lastrowid

        cursor.execute("INSERT OR IGNORE INTO product_ingredients (product_id, ingredient_id) VALUES (?, ?)", (product_id, ing_id))

    user_id = session.get("user_id")
    if user_id:
        cursor.execute("INSERT OR IGNORE INTO user_products (user_id, product_id) VALUES (?, ?)", (user_id, product_id))

    conn.commit()
    conn.close()

    return jsonify({"message": f"Produit '{nom}' ajouté avec succès !"})


if __name__ == "__main__":
    app.run(
        debug=True,
        #ssl_context='adhoc'
    )
