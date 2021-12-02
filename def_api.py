import mysql.connector



def conexao():
    db = mysql.connector.connect(
        host="localhost",
        database="aula_api",
        user="root",
        password="lucas26"
    )
    return db
    

def inserir(db, nome):
    mysql = f"insert into pessoas(nome) values ('{nome}')"
    try:
        cursor = db.cursor()
        cursor.execute(mysql)
        db.commit()
        cursor.close()
        print("registro feito!")
    except Exception as error:
        print(error)    


def deletar(db, codigo):
    mysql = f"delete from pessoas where codigo = {codigo}"
    try:
        cursor = db.cursor()
        cursor.execute(mysql)
        db.commit()
        cursor.close()
    except Exception as error:
        print(error)    


def atualizar(db, codigo, nome):
    info = (nome, codigo)
    mysql ="update pessoas set nome = %s where codigo = %s"
    try:
        cursor = db.cursor()
        cursor.execute(mysql, info)
        db.commit()
        cursor.close()
        print("registro feito!")
    except Exception as error:
        print(error)


def selecionar_tudo(db):
    mysql = "select * from pessoas"
    try:
        cursor = db.cursor()
        cursor.execute(mysql)
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    except Exception as error:
        print(error)    


def selecionar(db, codigo):
    mysql = f"select * from pessoas where codigo = {codigo}"
    try:
        cursor = db.cursor()
        cursor.execute(mysql)
        resultado = cursor.fetchone()
        cursor.close()
        return {resultado[0]: resultado[1]}
    except Exception as error:
        print(error)


















