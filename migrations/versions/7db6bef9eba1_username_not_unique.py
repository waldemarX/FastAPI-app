"""username not unique

Revision ID: 7db6bef9eba1
Revises: 800596d54cf8
Create Date: 2024-02-05 16:45:14.725807

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7db6bef9eba1'
down_revision: Union[str, None] = '800596d54cf8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_username_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_username_key', 'user', ['username'])
    # ### end Alembic commands ###
