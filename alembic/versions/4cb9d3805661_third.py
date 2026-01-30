"""Third

Revision ID: 4cb9d3805661
Revises: de26f65f2c41
Create Date: 2026-01-29 21:20:41.432834

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filmes
from infra.entities.atores import Atores

# revision identifiers, used by Alembic.
revision: str = '4cb9d3805661'
down_revision: Union[str, Sequence[str], None] = 'de26f65f2c41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.execute("""
        INSERT INTO filmes (titulo, genero, ano)
        VALUES ('Estou', 'aqui', 777);
    """)


def downgrade():
    op.execute("""
        DELETE FROM filmes
        WHERE titulo = 'Estou';
    """)
