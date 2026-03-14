import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# utilisateurs

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prenom TEXT NOT NULL,
    nom TEXT NOT NULL,
    genre TEXT,
    type_cheveux TEXT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# produits

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ean TEXT UNIQUE,
    nom TEXT NOT NULL,
    marque TEXT
)
""")

# ingredients

cursor.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)
""")

# produits avec ingredients 

cursor.execute("""
CREATE TABLE IF NOT EXISTS product_ingredients (
    product_id INTEGER,
    ingredient_id INTEGER,
    PRIMARY KEY (product_id, ingredient_id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
)
""")

# incompatibilités

cursor.execute("""
CREATE TABLE IF NOT EXISTS incompatibilities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_a TEXT NOT NULL,
    ingredient_b TEXT NOT NULL,
    risk_level TEXT,
    description TEXT
)
""")

# historique utilisateur

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_products (
    user_id INTEGER,
    product_id INTEGER,
    date_scan TEXT DEFAULT CURRENT_TIMESTAMP,
    date_utilisation TEXT,
    PRIMARY KEY (user_id, product_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
""")

# Liste des produits 

products = [
    {
        "nom": "Colorista Hair Makeup 1 Day Color Highlights #VioletHair pour brunettes",
        "marque": "L'Oréal",
        "ean": "3600523616916",
        "ingredients": [
            "AQUA", "CETEARYL ALCOHOL", "GLYCERIN", "BEHENTRIMONIUM CHLORIDE", "CANDELILLA CERA / CANDELILLA WAX",
            "AMODIMETHICONE", "CETYL ESTERS", "ISOPROPYL ALCOHOL", "TOCOPHERYL ACETATE", "SODIUM PCA",
            "PHENOXYETHANOL", "ETHYLHEXYL SALICYLATE", "TRIDECETH-6", "CHLORHEXIDINE DIGLUCONATE",
            "LIMONENE", "CAMELINA SATIVA SEED OIL", "LINALOOL", "BENZYL ALCOHOL", "BENZYL BENZOATE",
            "GERANIOL", "CETRIMONIUM CHLORIDE", "CITRONELLOL", "HEXYL CINNAMAL", "AMYL CINNAMAL", "PARFUM"
        ]
    },
    {
        "nom": "Coloration Permanente 4.0 Châtain Brillance Haute Intensité Préférence L'OREAL PARIS",
        "marque": "L'Oréal",
        "ean": "3600523616923",
        "ingredients": [
            "AQUA", "CETEARYL ALCOHOL", "GLYCERIN", "BEHENTRIMONIUM CHLORIDE", "CANDELILLA CERA / CANDELILLA WAX",
            "AMODIMETHICONE", "CETYL ESTERS", "ISOPROPYL ALCOHOL", "TOCOPHERYL ACETATE", "SODIUM PCA",
            "PHENOXYETHANOL", "ETHYLHEXYL SALICYLATE", "TRIDECETH-6", "CHLORHEXIDINE DIGLUCONATE",
            "LIMONENE", "CAMELINA SATIVA SEED OIL", "LINALOOL", "BENZYL ALCOHOL", "BENZYL BENZOATE",
            "GERANIOL", "CETRIMONIUM CHLORIDE", "CITRONELLOL", "HEXYL CINNAMAL", "AMYL CINNAMAL", "PARFUM"
        ]
    },
    {
        "nom": "Elution - Shampooing doux équilibrant antipelliculaire",
        "marque": "Ducray",
        "ean": "3282770390032",
        "ingredients": [
            "AQUA", "SODIUM LAURETH SULFATE", "GLYCINE", "GLYCERIN", "LAURYL BETAINE", "ACRYLATES COPOLYMER",
            "METHYL GLUCETH-20", "PEG-7 GLYCERYL COCOATE", "CITRIC ACID", "PARFUM", "GLYCOL PALMITATE",
            "GLYCOL STEARATE", "HYDROXYPROPYL GUAR HYDROXYPROPYLTRIMONIUM CHLORIDE", "PANTHENOL", "PANTOLACTONE",
            "PHENOXYETHANOL", "PIROCTONE OLAMINE", "SILICA", "SODIUM CHLORIDE", "SODIUM HYDROXIDE",
            "TRISODIUM ETHYLENEDIAMINE DISUCCINATE", "ZINC GLYCINATE"
        ]
    },
    {
        "nom": "Clarifying Detox Shampoo - Shampoing Clarifiant",
        "marque": "LIVING PROOF",
        "ean": "840216935600",
        "ingredients": [
            "AQUA", "SODIUM LAUROYL METHYL ISETHIONATE", "COCAMIDOPROPYL HYDROXYSULTAINE", "SODIUM METHYL COCOYL TAURATE",
            "DECYL GLUCOSIDE", "CETEARYL ALCOHOL", "GLYCERYL CAPRYLATE/CAPRATE", "CETYL ALCOHOL", "CETYL STEARATE",
            "CHARCOAL POWDER", "BETAINE", "SODIUM COCOYL ALANINATE", "TRISODIUM GLUTAMATE DIACETATE",
            "HYDROXYPHENYL PROPAMIDOBENZOIC ACID", "SODIUM POLYSTYRENE SULFONATE", "PEG-5 ETHYLHEXANOATE",
            "GLYCERYL STEARATE", "ISOSTEARYL ISOSTEARATE", "STEARIC ACID", "POTASSIUM CETYL PHOSPHATE", "GLYCERIN",
            "STEARETH-20", "PEG-75 STEARATE", "TRIDECETH-9", "CETETH-20", "ACRYLATES/C10-30 ALKYL ACRYLATE CROSSPOLYMER",
            "PARFUM", "SODIUM HYDROXIDE", "PROPANEDIOL", "ETHYLHEXYLGLYCERIN", "HYDROXYACETOPHENONE",
            "LINALOOL", "HEXYL CINNAMAL", "CITRONELLOL", "LIMONENE"
        ]
    },
    {
        "nom": "Shampooing crème nutrition miel de provence et karité bio",
        "marque": "Le Petit Marseillais",
        "ean": "3574661574561",
        "ingredients": [
            "AQUA", "AMMONIUM LAURYL SULFATE", "COCAMIDOPROPYL BETAINE", "GLYCERIN", "SODIUM CHLORIDE",
            "BUTYROSPERMUM PARKII BUTTER", "HELIANTHUS ANNUUS SEED OIL", "MEL EXTRACT", "LACTIC ACID",
            "STARCH HYDROXYPROPYLTRIMONIUM CHLORIDE", "UREA", "POLYQUATERNIUM-10", "GLYCOL DISTEARATE",
            "CARBOMER", "SODIUM LACTATE", "SODIUM HYDROXIDE", "CITRIC ACID", "BENZOIC ACID", "SODIUM BENZOATE",
            "PARFUM", "BENZYL SALICYLATE", "ALPHA-ISOMETHYL IONONE", "COUMARIN"
        ]
    },
    {
        "nom": "Gliss Shampooing",
        "marque": "Schwarzkopf",
        "ean": "3178040429628",
        "ingredients": [
            "AQUA", "SODIUM LAURETH SULFATE", "COCAMIDOPROPYL BETAINE", "PEG-7 GLYCERYL COCOATE", "MAGNESIUM CHLORIDE",
            "DIMETHICONE", "VACCINIUM MACROCARPON FRUIT EXTRACT", "DIMETHYLSILANOL HYALURONATE", "GLYCERIN",
            "HYDROLYZED KERATIN", "MAGNESIUM CITRATE", "PARFUM", "SODIUM BENZOATE", "PEG-120 METHYL GLUCOSE DIOLEATE",
            "AMODIMETHICONE", "CITRIC ACID", "SODIUM CHLORIDE", "GUAR HYDROXYPROPYLTRIMONIUM CHLORIDE",
            "PEG-40 HYDROGENATED CASTOR OIL", "HYDROGENATED CASTOR OIL", "GLYCOL DISTEARATE", "LAURETH-4",
            "PRUNUS ARMENIACA KERNEL OIL", "LAURETH-23", "TRIDECETH-10", "SODIUM HYDROXIDE", "PROPYLENE GLYCOL",
            "BENZYL ALCOHOL", "PHENOXYETHANOL", "SODIUM SALICYLATE", "POTASSIUM SORBATE", "SORBIC ACID"
        ]
    },
    {
        "nom": "Be curly advanced",
        "marque": "Aveda",
        "ean": "0018084053683",
        "ingredients": [
            "AQUA", "PROPANEDIOL", "ETHYLHEXYL OLIVATE", "STEARAMIDOPROPYL DIMETHYLAMINE", "POLYESTER-11",
            "HYDROLYZED PEA PROTEIN", "HYDROLYZED VEGETABLE PROTEIN", "GARCINIA INDICA SEED BUTTER",
            "KAEMFERIA GALANGA ROOT EXTRACT", "SQUALANE", "BEHENTRIMONIUM METHOSULFATE", "CETRIMONIUM CHLORIDE",
            "GLYCINE SOJA OIL", "HYDROXYPROPYLTRIMONIUM HYDROLYZED CORN STARCH", "BIS-OCTYLDODECYL DIMER DILINOLEATE/PROPANEDIOL COPOLYMER",
            "SCLEROTIUM GUM", "SODIUM CHLORIDE", "HYDROXYPROPYL STARCH PHOSPHATE", "LACTIC ACID", "CETEARYL ALCOHOL",
            "PARFUM", "LINALOOL", "CITRAL", "LIMONENE", "CITRONELLOL", "EUGENOL", "GERANIOL", "TOCOPHEROL",
            "PHENOXYETHANOL", "SODIUM BENZOATE", "POTASSIUM SORBATE"
        ]
    },
    {
        "nom": "Honey Gloss Ceramide Therapy - Masque cheveux",
        "marque": "Gisou",
        "ean": "8720986610148",
        "ingredients": [
            "AQUA", "CETEARYL ALCOHOL", "BEHENAMIDOPROPYL DIMETHYLAMINE", "DICOCOYLETHYL HYDROXYETHYLMONIUM METHOSULFATE",
            "BUTYROSPERMUM PARKII BUTTER", "LACTIC ACID", "MIEL", "PROPOLIS CERA", "CERAMIDE NP",
            "HYDROLYZED SODIUM HYALURONATE", "SODIUM HYALURONATE", "HYDROXYPROPYLTRIMONIUM HYALURONATE",
            "PANTHENOL", "SQUALANE", "TOCOPHEROL", "GLYCERIN", "ETHYLHEXYLGLYCERIN", "1,2-HEXANEDIOL",
            "SUNFLOWER SEED OIL GLYCERIDES", "HYDROGENATED ETHYLHEXYL OLIVATE", "VITIS VINIFERA SEED OIL",
            "CARTHAMUS TINCTORIUS SEED OIL", "CALENDULA OFFICINALIS FLOWER EXTRACT", "HYDROGENATED OLIVE OIL UNSAPONIFIABLES",
            "OENOTHERA BIENNIS OIL", "ROSA CANINA FRUIT OIL", "HELIANTHUS ANNUUS SEED OIL", "HELIANTHUS ANNUUS SPROUT EXTRACT",
            "CITRUS AURANTIUM BERGAMIA FRUIT EXTRACT", "DAUCUS CAROTA SATIVA ROOT EXTRACT", "CAESALPINIA SPINOSA FRUIT EXTRACT",
            "PARFUM", "SODIUM BENZOATE", "MALTODEXTRIN", "CITRUS AURANTIUM"
        ]
    },
    {
    "nom": "Crème capillaire définition boucles (Hair styling - Maxi format)",
    "marque": "BYPHASSE",
    "ean": "8436097096046",
    "ingredients": [
        "AQUA", "CETYL ALCOHOL", "CETRIMONIUM CHLORIDE", "PROPYLENE GLYCOL", "GLYCERYL STEARATE SE",
        "SODIUM BENZOATE", "HYDROXYETHYLCELLULOSE", "POTASSIUM SORBATE", "PARFUM", "AMODIMETHICONE",
        "TRIETHANOLAMINE", "CITRIC ACID", "ALOE BARBADENSIS LEAF JUICE", "PANTHENOL", "TRIDECETH-12",
        "AMYL CINNAMAL", "LINALOOL", "BENZYL SALICYLATE", "LIMONENE", "HYDROXYCITRONELLAL"
    ]
    }

]

for product in products:

    cursor.execute("""
        INSERT OR IGNORE INTO products (ean, nom, marque) VALUES (?, ?, ?)
    """, (product["ean"], product["nom"], product["marque"]))
    
    cursor.execute("SELECT id FROM products WHERE ean = ?", (product["ean"],))
    product_id = cursor.fetchone()[0]
    
    for ing in product["ingredients"]:
        cursor.execute("INSERT OR IGNORE INTO ingredients (name) VALUES (?)", (ing,))
        cursor.execute("SELECT id FROM ingredients WHERE name = ?", (ing,))
        ingredient_id = cursor.fetchone()[0]

        cursor.execute("""
            INSERT OR IGNORE INTO product_ingredients (product_id, ingredient_id)
            VALUES (?, ?)
        """, (product_id, ingredient_id))

# liste d'ingredients

ingredients = [
    "AQUA",
    "CETEARYL ALCOHOL",
    "GLYCERIN",
    "BEHENTRIMONIUM CHLORIDE",
    "CANDELILLA CERA / CANDELILLA WAX",
    "AMODIMETHICONE",
    "CETYL ESTERS",
    "ISOPROPYL ALCOHOL",
    "TOCOPHERYL ACETATE",
    "SODIUM PCA",
    "PHENOXYETHANOL",
    "ETHYLHEXYL SALICYLATE",
    "TRIDECETH-6",
    "CHLORHEXIDINE DIGLUCONATE",
    "LIMONENE",
    "CAMELINA SATIVA SEED OIL",
    "LINALOOL",
    "BENZYL ALCOHOL",
    "BENZYL BENZOATE",
    "GERANIOL",
    "CETRIMONIUM CHLORIDE",
    "CITRONELLOL",
    "HEXYL CINNAMAL",
    "AMYL CINNAMAL",
    "PARFUM",
    "SODIUM LAURETH SULFATE",
    "GLYCINE",
    "LAURYL BETAINE",
    "ACRYLATES COPOLYMER",
    "METHYL GLUCETH-20",
    "PEG-7 GLYCERYL COCOATE",
    "CITRIC ACID",
    "GLYCOL PALMITATE",
    "GLYCOL STEARATE",
    "HYDROXYPROPYL GUAR HYDROXYPROPYLTRIMONIUM CHLORIDE",
    "PANTHENOL",
    "PANTOLACTONE",
    "PIROCTONE OLAMINE",
    "SODIUM CHLORIDE",
    "SODIUM HYDROXIDE",
    "TRISODIUM ETHYLENEDIAMINE DISUCCINATE",
    "ZINC GLYCINATE",
    "SODIUM LAUROYL METHYL ISETHIONATE",
    "COCAMIDOPROPYL HYDROXYSULTAINE",
    "SODIUM METHYL COCOYL TAURATE",
    "DECYL GLUCOSIDE",
    "GLYCERYL CAPRYLATE/CAPRATE",
    "CETYL ALCOHOL",
    "CETYL STEARATE",
    "CHARCOAL POWDER",
    "BETAINE",
    "SODIUM COCOYL ALANINATE",
    "TRISODIUM GLUTAMATE DIACETATE",
    "HYDROXYPHENYL PROPAMIDOBENZOIC ACID",
    "SODIUM POLYSTYRENE SULFONATE",
    "PEG-5 ETHYLHEXANOATE",
    "GLYCERYL STEARATE",
    "ISOSTEARYL ISOSTEARATE",
    "STEARIC ACID",
    "POTASSIUM CETYL PHOSPHATE",
    "STEARETH-20",
    "PEG-75 STEARATE",
    "TRIDECETH-9",
    "CETETH-20",
    "ACRYLATES/C10-30 ALKYL ACRYLATE CROSSPOLYMER",
    "PROPANEDIOL",
    "ETHYLHEXYLGLYCERIN",
    "HYDROXYACETOPHENONE",
    "SODIUM COCOYL ISETHIONATE",
    "DIMETHICONE",
    "VACCINIUM MACROCARPON FRUIT EXTRACT",
    "DIMETHYLSILANOL HYALURONATE",
    "HYDROLYZED KERATIN",
    "MAGNESIUM CITRATE",
    "PEG-120 METHYL GLUCOSE DIOLEATE",
    "GUAR HYDROXYPROPYLTRIMONIUM CHLORIDE",
    "PEG-40 HYDROGENATED CASTOR OIL",
    "HYDROGENATED CASTOR OIL",
    "LAURETH-4",
    "PRUNUS ARMENIACA KERNEL OIL",
    "LAURETH-23",
    "TRIDECETH-10",
    "ETHYLHEXYL OLIVATE",
    "STEARAMIDOPROPYL DIMETHYLAMINE",
    "POLYESTER-11",
    "HYDROLYZED PEA PROTEIN",
    "HYDROLYZED VEGETABLE PROTEIN",
    "GARCINIA INDICA SEED BUTTER",
    "KAEMFERIA GALANGA ROOT EXTRACT",
    "SQUALANE",
    "BEHENTRIMONIUM METHOSULFATE",
    "GLYCINE SOJA OIL",
    "HYDROXYPROPYLTRIMONIUM HYDROLYZED CORN STARCH",
    "BIS-OCTYLDODECYL DIMER DILINOLEATE/PROPANEDIOL COPOLYMER",
    "SCLEROTIUM GUM",
    "HYDROXYPROPYL STARCH PHOSPHATE",
    "LACTIC ACID",
    "TRIDECETH-12",
    "ALOE BARBADENSIS LEAF JUICE",
    "HYDROXYETHYLCELLULOSE",
    "SODIUM BENZOATE",
    "POTASSIUM SORBATE",
    "TRIETHANOLAMINE",
    "BENZYL SALICYLATE",
    "HYDROXYCITRONELLAL",
    "BEHENAMIDOPROPYL DIMETHYLAMINE",
    "DICOCOYLETHYL HYDROXYETHYLMONIUM METHOSULFATE",
    "BUTYROSPERMUM PARKII BUTTER",
    "MIEL",
    "PROPOLIS CERA",
    "CERAMIDE NP",
    "HYDROLYZED SODIUM HYALURONATE",
    "SODIUM HYALURONATE",
    "HYDROXYPROPYLTRIMONIUM HYALURONATE",
    "TOCOPHEROL",
    "1,2-HEXANEDIOL",
    "SUNFLOWER SEED OIL GLYCERIDES",
    "HYDROGENATED ETHYLHEXYL OLIVATE",
    "VITIS VINIFERA SEED OIL",
    "CARTHAMUS TINCTORIUS SEED OIL",
    "CALENDULA OFFICINALIS FLOWER EXTRACT",
    "HYDROGENATED OLIVE OIL UNSAPONIFIABLES",
    "OENOTHERA BIENNIS OIL",
    "ROSA CANINA FRUIT OIL",
    "HELIANTHUS ANNUUS SEED OIL",
    "HELIANTHUS ANNUUS SPROUT EXTRACT",
    "CITRUS AURANTIUM BERGAMIA FRUIT EXTRACT",
    "DAUCUS CAROTA SATIVA ROOT EXTRACT",
    "CAESALPINIA SPINOSA FRUIT EXTRACT",
    "PROPYLENE GLYCOL",
    "GLYCERYL STEARATE SE",
    "AMMONIA",
    "AMMONIUM THIOGLYCOLATE",
    "HYDROGEN PEROXIDE",
    "PERSULFATES",
    "PROTEIN TREATMENTS",
    "HENNA",
    "INDIGO",
    "METALLIC SALTS",
    "CYCLOPENTASILOXANE",
    "COCAMIDOPROPYL BETAINE",
    "LAURYL GLUCOSIDE",
    "COCO-GLUCOSIDE",
    "CAPRYLYL/CAPRYL GLUCOSIDE",
    "SODIUM COCO SULFATE",
    "COCONUT FLOWER SUGAR",
    "ALOE BARBADENSIS LEAF EXTRACT",
    "CITRUS AURANTIUM DULCIS PEEL OIL",
    "LAMINARIA DIGITATA EXTRACT",
    "BELLIS PERENNIS FLOWER EXTRACT",
    "MAGNOLIA OFFICINALIS BARK EXTRACT",
    "ASCORBYL PALMITATE",
    "BETA SITOSTEROL",
    "SQUALENE",
    "XANTHAN GUM",
    "GLYCERYL OLEATE",
    "HYDROGENATED PALM GLYCERIDES CITRATE",
    "LECITHIN",
    "POLYGLYCERYL 4 CAPRATE"
]


for ing in ingredients:
    cursor.execute(
        "INSERT OR IGNORE INTO ingredients (name) VALUES (?)",
        (ing,)
    )

# liste des nicompatibilités

incompatibilities = [
    ("SODIUM HYDROXYDE", "AMMONIA", "⚠️", "Incompatibles"),
    ("SODIUM HYDROXYDE", "AMMONIUM THIOGLYCOLATE", "⚠️", "Incompatibles"),
    ("SODIUM HYDROXYDE", "HYDROGEN PEROXIDE", "⚠️", "Incompatibles"),
    ("SODIUM HYDROXYDE", "PERSULFATES", "⚠️", "Incompatibles"),
    ("SODIUM HYDROXYDE", "PROTEIN TREATMENTS", "⚠️", "Incompatibles"),
    ("AMMONIUM THIOGLYCOLATE", "SODIUM HYDROXYDE", "⚠️", "Incompatibles"),
    ("AMMONIUM THIOGLYCOLATE", "HYDROGEN PEROXIDE", "⚠️", "Incompatibles"),
    ("AMMONIUM THIOGLYCOLATE", "PERSULFATES", "⚠️", "Incompatibles"),
    ("AMMONIUM THIOGLYCOLATE", "AMMONIA", "⚠️", "Incompatibles"),
    ("AMMONIA", "SODIUM HYDROXYDE", "⚠️", "Incompatibles"),
    ("AMMONIA", "AMMONIUM THIOGLYCOLATE", "⚠️", "Incompatibles"),
    ("AMMONIA", "HENNA", "⚠️", "Incompatibles"),
    ("AMMONIA", "INDIGO", "⚠️", "Incompatibles"),
    ("HYDROGEN PEROXIDE", "SODIUM HYDROXYDE", "⚠️", "Incompatibles"),
    ("HYDROGEN PEROXIDE", "AMMONIUM THIOGLYCOLATE", "⚠️", "Incompatibles"),
    ("HYDROGEN PEROXIDE", "HENNA", "⚠️", "Incompatibles"),
    ("HYDROGEN PEROXIDE", "INDIGO", "⚠️", "Incompatibles"),
    ("HYDROGEN PEROXIDE", "METALLIC SALTS", "⚠️", "Incompatibles"),
    ("HYDROGEN PEROXIDE", "ZINC PYRITHIONE", "⚠️", "Incompatibles"),
    ("METALLIC SALTS", "HYDROGEN PEROXIDE", "⚠️", "Incompatibles"),
    ("METALLIC SALTS", "PERSULFATES", "⚠️", "Incompatibles"),
    ("METALLIC SALTS", "CHEMICAL COLORANTS", "⚠️", "Incompatibles"),
    ("HENNA", "HYDROGEN PEROXIDE", "⚠️", "Incompatibles"),
    ("HENNA", "PERSULFATES", "⚠️", "Incompatibles"),
    ("HENNA", "AMMONIA", "⚠️", "Incompatibles"),
    ("HENNA", "AMMONIUM THIOGLYCOLATE", "⚠️", "Incompatibles"),
    ("HENNA", "METALLIC SALTS", "⚠️", "Incompatibles"),
    ("INDIGO", "HYDROGEN PEROXIDE", "⚠️", "Incompatibles"),
    ("INDIGO", "PERSULFATES", "⚠️", "Incompatibles"),
    ("INDIGO", "AMMONIA", "⚠️", "Incompatibles"),
    ("DIMETHICONE", "SODIUM LAUROYL SARCOSINATE", "⚠️", "Incompatibles"),
    ("DIMETHICONE", "COCAMIDOPROPYL BETAINE", "⚠️", "Incompatibles"),
    ("DIMETHICONE", "LAURYL GLUCOSIDE", "⚠️", "Incompatibles"),
    ("DIMETHICONE", "SODIUM COCO-SULFATE", "⚠️", "Incompatibles"),
    ("DIMETHICONE", "SODIUM COCOYL ISETHIONATE", "⚠️", "Incompatibles"),
    ("DIMETHICONE", "DISODIUM LAURETH SULFOSUCCINATE", "⚠️", "Incompatibles"),
    ("DIMETHICONE", "COCO-GLUCOSIDE", "⚠️", "Incompatibles"),
    ("DIMETHICONE", "CAPRYLYL/CAPRYL GLUCOSIDE", "⚠️", "Incompatibles"),
    ("CYCLOPENTASILOXANE", "SODIUM COCOYL ISETHIONATE", "⚠️", "Incompatibles"),
    ("CYCLOPENTASILOXANE", "DECYL GLUCOSIDE", "⚠️", "Incompatibles"),
    ("CYCLOPENTASILOXANE", "SODIUM LAUROYL SARCOSINATE", "⚠️", "Incompatibles"),
    ("AMODIMETHICONE", "SODIUM COCO-SULFATE", "⚠️", "Incompatibles"),
    ("AMODIMETHICONE", "SODIUM LAURYL SULFATE", "⚠️", "Incompatibles"),
    ("AMODIMETHICONE", "LAURYL GLUCOSIDE", "⚠️", "Incompatibles"),
    ("AMODIMETHICONE", "SODIUM COCOYL ISETHIONATE", "⚠️", "Incompatibles"),
    ("AMODIMETHICONE", "DISODIUM LAURETH SULFOSUCCINATE", "⚠️", "Incompatibles"),
    ("AMODIMETHICONE", "COCO-GLUCOSIDE", "⚠️", "Incompatibles"),
    ("AMODIMETHICONE", "CAPRYLYL/CAPRYL GLUCOSIDE", "⚠️", "Incompatibles"),
    ("SODIUM LAURYL SULFATE", "RICINUS COMMUNIS SEED OIL", "⚠️", "Incompatibles"),
    ("SODIUM LAURYL SULFATE", "BUTYROSPERMUM PARKII BUTTER", "⚠️", "Incompatibles"),
    ("SODIUM LAURYL SULFATE", "DIMETHICONE", "⚠️", "Incompatibles"),
    ("SODIUM LAURYL SULFATE", "BEHENTRIMONIUM METHOSULFATE", "⚠️", "Incompatibles"),
    ("SODIUM LAURYL SULFATE", "CETRIMONIUM CHLORIDE", "⚠️", "Incompatibles"),
    ("SODIUM LAURYL SULFATE", "POLYQUATERNIUM-10", "⚠️", "Incompatibles"),
    ("SODIUM LAURYL SULFATE", "COCAMIDOPROPYL BETAINE", "⚠️", "Incompatibles"),
    ("COCONUT OIL", "SODIUM LAURYL SULFATE", "⚠️", "Incompatibles"),
    ("COCONUT OIL", "AMODIMETHICONE", "⚠️", "Incompatibles"),
    ("COCONUT OIL", "DIMETHICONE", "⚠️", "Incompatibles"),
    ("COCONUT OIL", "SODIUM COCO-SULFATE", "⚠️", "Incompatibles"),
    ("SHEA BUTTER", "SODIUM LAURYL SULFATE", "⚠️", "Incompatibles"),
    ("SHEA BUTTER", "AMODIMETHICONE", "⚠️", "Incompatibles"),
    ("SHEA BUTTER", "DIMETHICONE", "⚠️", "Incompatibles"),
    ("SHEA BUTTER", "SODIUM COCO-SULFATE", "⚠️", "Incompatibles"),
    ("LIMONENE", "AMMONIA", "⚠️", "Incompatibles"),
    ("LIMONENE", "HYDROGEN PEROXIDE", "⚠️", "Incompatibles"),
    ("LIMONENE", "PERSULFATES", "⚠️", "Incompatibles"),
    ("LIMONENE", "METALLIC SALTS", "⚠️", "Incompatibles"),
    ("HYDROLYZED KERATIN", "SODIUM HYDROXIDE", "⚠️", "Incompatibles"),
    ("HYDROLYZED KERATIN", "AMMONIUM THIOGLYCOLATE", "⚠️", "Incompatibles"),
    ("HYDROLYZED KERATIN", "HYDROGEN PEROXIDE", "⚠️", "Incompatibles"),
    ("HYDROLYZED KERATIN", "PERSULFATES", "⚠️", "Incompatibles"),
    ("CYCLOPENTASILOXANE", "SODIUM LAURYL SULFATE", "⚠️", "Incompatibles"),
    ("CYCLOPENTASILOXANE", "AMODIMETHICONE", "⚠️", "Incompatibles"),
    ("CYCLOPENTASILOXANE", "SODIUM COCO-SULFATE", "⚠️", "Incompatibles"),
    ("CYCLOPENTASILOXANE", "COCAMIDOPROPYL BETAINE", "⚠️", "Incompatibles"),
    ("COCAMIDOPROPYL BETAINE", "DIMETHICONE", "⚠️", "Incompatibles"),
    ("COCAMIDOPROPYL BETAINE", "AMODIMETHICONE", "⚠️", "Incompatibles"),
    ("COCAMIDOPROPYL BETAINE", "CYCLOPENTASILOXANE", "⚠️", "Incompatibles"),
    ("COCAMIDOPROPYL BETAINE", "SODIUM LAURYL SULFATE", "⚠️", "Incompatibles")
]

for inc in incompatibilities:
    cursor.execute("""
    INSERT OR IGNORE INTO incompatibilities (ingredient_a, ingredient_b, risk_level, description)
    VALUES (?, ?, ?, ?)
    """, inc)

conn.commit()
conn.close()

print("Base de données créée avec succès")
