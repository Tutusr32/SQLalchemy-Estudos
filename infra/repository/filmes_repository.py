from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filmes

class FilmesRepository:

    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data
            
    def insert(self, titulo, genero, ano):
        with DBConnectionHandler() as db:
            try:
                data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
                db.session.add(data_insert)
                db.session.commit()

            except Exception:
                db.session.rollback()
                raise

    def delete(self, titulo):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
                db.session.commit()

            except Exception:
                db.session.rollback()
                raise
            
    def update(self, genero, ano):
        with DBConnectionHandler() as db:
            try: 
                db.session.query(Filmes).filter(Filmes.genero == genero).update({"ano": ano})
                db.sessiom.commit()

            except Exception:
                db.session.rollback()
                raise