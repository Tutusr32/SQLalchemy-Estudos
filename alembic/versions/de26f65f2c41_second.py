"""Second

Revision ID: de26f65f2c41
Revises: f14ba062cdfb
Create Date: 2026-01-29 20:50:43.086665

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from infra.repository.filmes_repository import FilmesRepository
from infra.entities.filmes import Filmes
from infra.entities.atores import Atores

# revision identifiers, used by Alembic.
revision: str = 'de26f65f2c41'
down_revision: Union[str, Sequence[str], None] = 'f14ba062cdfb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    filmes_repository = FilmesRepository()
    filmes_repository.insert('Olá', 'Mundo', 123)


def downgrade() -> None:
    filmes_repository = FilmesRepository()
    filmes_repository.delete('Olá')


