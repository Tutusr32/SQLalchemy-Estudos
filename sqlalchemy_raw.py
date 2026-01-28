from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

# Configurações
engine = create_engine(
    'mysql+pymysql://app_user:my_pw@localhost:3306/cinema'
)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Entidades
class Filmes(Base):
    __tablename__ = "filmes"
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme: Título = {self.titulo}, Gênero = {self.genero}, Ano = {self.ano}"

# Insert
filme_insert = Filmes(titulo="Dracula", genero="Drama", ano=1996)

session.add(filme_insert)

# Delete
session.query(Filmes).filter(Filmes.titulo=="Batman").delete()

# Update
session.query(Filmes).filter(Filmes.genero=="Drama").update({"ano": 2000})

# Select
filmes = session.query(Filmes).all()

for filme in filmes:
    print(filme)

session.commit()
session.close() 