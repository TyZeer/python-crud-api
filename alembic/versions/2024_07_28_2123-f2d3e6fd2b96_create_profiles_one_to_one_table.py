"""create profiles one to one table

Revision ID: f2d3e6fd2b96
Revises: 959fbb019f33
Create Date: 2024-07-28 21:23:26.472316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2d3e6fd2b96'
down_revision: Union[str, None] = '959fbb019f33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
