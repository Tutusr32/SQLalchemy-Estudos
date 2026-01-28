from infra.repository.atores_repositoty import AtoresRepository
from infra.repository.filmes_repository import FilmesRepository
from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filmes
from infra.entities.atores import Atores

# Usando relationship
with DBConnectionHandler() as db:
    filmes = db.session.query(Filmes).all()

    for filme in filmes:
        print(filme.titulo)

        for ator in filme.atores:
            print("  ->", ator.nome)
    