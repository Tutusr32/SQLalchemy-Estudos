from infra.configs.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Filmes(Base):
    __tablename__ = "filmes"
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    atores = relationship("Atores", backref="filme", lazy = "selectin")

    def __repr__(self):
        return f"Filme: Título = {self.titulo}, Gênero = {self.genero}, Ano = {self.ano}"
