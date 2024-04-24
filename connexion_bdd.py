import mysql.connector

# connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="thyss",
    password="thyss",
    database="cinema"
)

# création d'un curseur pour exécuter des requêtes SQL
cursor = db.cursor()

# execution de la requête
cursor.execute("SELECT * FROM movie LIMIT 2;")

# récupération des résultats
result = cursor.fetchall()

# affichage des résultats
for row in result:
    print(row)

# fermeture du curseur et de la connexion à la base de données
cursor.close()
db.close()
