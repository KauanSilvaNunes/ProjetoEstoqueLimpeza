import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def conexao():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"), 
            database=os.getenv("DB_NAME")
        )
        if conexao.is_connected():
            print("Conexão com MySQL (XAMPP) estabelecida com sucesso!")
            return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None



if __name__=="__main__":
    conn=conexao()
    conn.close()