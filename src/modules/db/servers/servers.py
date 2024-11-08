from src.db.configuration import DBConnectionHandler
from typing import List


class ServerDB:
    def __init__(self, ip: str, port: int, name: str, id: str = None) -> None:
        self.id = id
        self.ip = ip
        self.port = port
        self.name = name

    @classmethod
    def __format_data(cls, data):
        return [ServerDB(id=server[0], ip=server[1], port=server[2], name=server[3]).__dict__ for server in data]

    def add_server(self):
        with DBConnectionHandler() as db:
            try:
                db.cursor.execute(
                    query="""
                        INSERT INTO 
                            servers (ip, port, name)
                        VALUES 
                            (%s, %s, %s)
                        RETURNING id;
                    """,
                    vars=(
                        self.ip,
                        self.port,
                        self.name
                    )
                )
                db.connection.commit()
                return db.cursor.fetchone()[0]
            except Exception as exception:
                db.connection.rollback()
                raise Exception(str(exception))
            finally:
                db.connection.close()
        return None

    @classmethod
    def get_servers(cls):
        with DBConnectionHandler() as db:
            try:
                db.cursor.execute(
                    query="""
                        SELECT 
                            id, ip, port, name 
                        FROM
                            servers;
                    """,
                )
                servers_list = db.cursor.fetchall()
                return cls.__format_data(data=servers_list)
            except Exception as exception:
                db.connection.rollback()
                raise Exception(str(exception))
            finally:
                db.connection.close()
        return None
