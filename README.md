#  Estudos de SQLAlchemy com Python (ORM + MySQL)

Repositório dedicado aos meus estudos de **SQLAlchemy ORM** com Python, utilizando **MySQL** como banco de dados e uma arquitetura organizada por camadas (configs, entidades e repositórios).

O foco é aprender na prática:

- Mapeamento objeto-relacional (ORM)
- Relacionamentos entre tabelas
- Joins com SQLAlchemy
- CRUD completo
- Organização de projeto backend

---

##  Estrutura do Projeto

```text
infra/
 ┣ configs/
 ┃ ┗ base.py
 ┃ ┗ connection.py
 ┣ entities/
 ┃ ┗ filmes.py
 ┃ ┗ atores.py
 ┣ repository/
 ┃ ┗ filmes_repository.py
 ┃ ┗ atores_repository.py

main.py
```
Origem dos códigos de estudo: https://github.com/programadorLhama/sqlalchemy
