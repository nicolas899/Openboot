import mysql
import mysql.connector

cone = mysql.connector.connect(user='root', host='Localhost',database='openb',port='3306')

cursor = cone.cursor()

cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

cursor.execute("INSERT INTO Alumnos VALUES(1,'Nicolas', 'Gaitan')")
cursor.execute("INSERT INTO Alumnos VALUES(2,'Angel', 'Di maria')")
cursor.execute("INSERT INTO Alumnos VALUES(3,'Diego', 'Milito')")
cursor.execute("INSERT INTO Alumnos VALUES(4,'Leo', 'Messi')")
cursor.execute("INSERT INTO Alumnos VALUES(5,'Cristiano', 'Ronaldo')")
cursor.execute("INSERT INTO Alumnos VALUES(6,'Roman', 'Riquelme')")
cursor.execute("INSERT INTO Alumnos VALUES(7,'Pablo', 'Vegetti')")
cursor.execute("INSERT INTO Alumnos VALUES(8,'Javier', 'Zanetti')")

cone.commit()

cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Leo'")
mostrar = cursor.fetchall()
print(mostrar)

cone.close()

