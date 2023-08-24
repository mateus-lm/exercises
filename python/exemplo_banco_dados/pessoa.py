import sqlite3 

def insere_pessoa(cursor, nome, dataNascimento, sexo):
    pessoa = [
        (nome, dataNascimento, sexo)
    ]
    cursor.executemany("INSERT INTO pessoa VALUES (?, ?, ?)", pessoa)

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

# cursor.execute("CREATE TABLE pessoa(nome, dataNascimento, sexo)")

# banco.commit()

#cursor.execute("INSERT INTO pessoa VALUES ('Mateus M', '2012-23-12', 'M')")
# banco.commit()
insere_pessoa(cursor, 'Oracle', '1969-01-09', 'F' )
banco.commit()

cursor.execute("SELECT * FROM PESSOA")
print(cursor.fetchall())