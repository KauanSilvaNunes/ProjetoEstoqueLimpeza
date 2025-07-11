from DAO.connect import connect


class UserDAO:


    def selectionUser(self,registro):
        conn, cursor=connect()
        try:
            cursor.execute("SELECT * FROM usuario WHERE registro_funcionario = %s", (registro,))
            user=cursor.fetchall()
            return user
        except Exception as e:
            print("Erro ", e)
        finally:
            cursor.close()
            conn.close()




if __name__=="__main__":
    user=UserDAO()
    print(user.selectionUser(1))