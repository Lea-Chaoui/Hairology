let cameraError = false;
let quaggaInitialized = false;
let lastCode = null;
let count = 0;

// Quagga, scanner

function initScanner() {
    Quagga.init({
        inputStream: {
            type: "LiveStream",
            target: document.querySelector("#scanner"),
            constraints: {
                facingMode: "environment",
                audio: false
            }
        },
        decoder: {
            readers: ["ean_reader", "ean_13_reader"]
        },
        locate: true
    }, function(err) {
        if (err) {
            console.error("Impossible d'accéder à la caméra. Tu peux utiliser le code EAN manuel.", err);
            cameraError = true; 
            return;
        }
        Quagga.start();
        quaggaInitialized = true;
    });

    Quagga.onDetected(data => {
        const code = data.codeResult.code;

        if (code === lastCode) {
            count++;
        } else {
            lastCode = code;
            count = 1;
        }

        if (count >= 2) {
            Quagga.stop();
            analyzeEAN(code);
        }
    });
}


// analyser le EAN 

function analyzeEAN(code) {
    fetch(`/analyze/${code}`)
        .then(res => {
            if (!res.ok) {
                return res.json().then(data => { throw new Error(data.error); });
            }
            return res.json();
        })
        .then(data => {

            displayProduct(data);
        })
        .catch(err => {
            if (err.message === "Produit non trouvé") {

                const nom = prompt("Produit non trouvé. Entrez le nom du produit à ajouter :");
                if (!nom) return;

                const marque = prompt("Entrez la marque du produit :") || "";
                const ingredientsInput = prompt("Entrez les ingrédients séparés par des virgules :");
                const ingredients = ingredientsInput ? ingredientsInput.split(",").map(s => s.trim()) : [];

                fetch("/add_product", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        ean: code,
                        nom: nom,
                        marque: marque,
                        ingredients: ingredients
                    })
                })
                .then(res => res.json())
                .then(data => alert(data.message))
                .catch(e => alert("Erreur lors de l'ajout du produit : " + e));
            } else {
                alert(err.message);
            }
        });
}

// EAN manuel

function sendManualCode() {
    const code = document.getElementById("eanField").value.trim();
    if (!code) return alert("Entrez un code EAN");
    analyzeEAN(code);
}

// produit et ajout

function displayProduct(product) {
    if (!product.id) { alert("Produit sans ID !"); return; }



        const infoDiv = document.getElementById("productInfo");
    infoDiv.innerHTML = `
        <h3>${product.nom} (${product.marque || "Marque inconnue"})</h3>
        <p>Ingrédients : ${product.ingredients.join(", ")}</p>
        ${product.incompatibilities.length > 0 
            ? `<p style="color:red;"><strong>⚠️ Incompatibilités 
            <br> Oups !
            <br>  Ce produit n’aime pas votre dernier soin… Vos cheveux risquent de faire la tête !
            :</strong><br>
               ${product.incompatibilities.map(inc => `${inc.ingredient_a} ⚠ ${inc.ingredient_b} (${inc.risk_level}) - ${inc.description}`).join("<br>")}
               </p>`
            : `<p style="color:green;">✅ Pas d'incompatibilités avec vos produits.</p>`}
    `;
    

    const btnContainer = document.getElementById("addButtonContainer");
    btnContainer.style.display = "block";

    const addBtn = document.getElementById("addToCollectionBtn");
    addBtn.onclick = () => {
        fetch("/add_to_collection", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ product_id: product.id })
        })
        .then(res => res.json())
        .then(data => alert(data.message))
        .catch(err => console.error(err));
    };
}

document.addEventListener("DOMContentLoaded", () => {

    initScanner();

    const overlay = document.getElementById("scannerOverlay");
    overlay.addEventListener("click", () => {
        overlay.style.display = "none"; 
        if (cameraError) {
            alert("Impossible d'accéder à la caméra. Tu peux utiliser le code EAN manuel.");
        } else if (!quaggaInitialized) {
            Quagga.start();
            quaggaInitialized = true;
        }
    });
});
