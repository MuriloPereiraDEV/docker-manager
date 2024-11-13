from Back.src.db.configuration import DBConnectionHandler


class UserDB:
    def __init__(self, email: str, password: str = None, id: str = None, first_name: str = None, last_name: str = None):
        self.id = id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def verify_user(self):
        with DBConnectionHandler() as db:
            try:
                db.cursor.execute(
                    query="""
                        SELECT
                            id, email, first_name, last_name
                        FROM
                            users
                        WHERE
                            email = %s AND password = %s;
                    """,
                    vars=(
                        self.email,
                        self.password
                    )
                )
                return db.cursor.fetchone()
            except Exception as exception:
                db.connection.rollback()
                raise Exception(str(exception))
            finally:
                db.connection.close()
        return None

    def create_user(self):
        with DBConnectionHandler() as db:
            try:
                db.cursor.execute(
                    query="""
                        INSERT INTO 
                            users (first_name, last_name, email, password)
                        VALUES 
                            (%s, %s, %s, %s)
                        RETURNING id;
                    """,
                    vars=(
                        self.first_name,
                        self.last_name,
                        self.email,
                        self.password
                    )
                )
                db.connection.commit()
                new_user_id = db.cursor.fetchone()[0]
                return new_user_id
            except Exception as exception:
                db.connection.rollback()
                raise Exception(str(exception))
            finally:
                db.connection.close()
        return None
