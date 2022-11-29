from .entities.User import User


class ModelUser():

    @classmethod
    def register(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO accounts (id, username, password, name, last_name, email)
                    VALUES (0, '{0}', '{1}', '{2}', '{3}', '{4}')""".format(
                user.username,
                User.create_hash_password(user.password),
                user.name,
                user.last_name,
                user.email
            )
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password 
                    FROM accounts WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(
                    row[0], 
                    row[1], 
                    User.check_password(row[2], user.password),
                    None,
                    None,
                    None
                    )
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username  
                    FROM accounts WHERE id = '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, None, None, None)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
