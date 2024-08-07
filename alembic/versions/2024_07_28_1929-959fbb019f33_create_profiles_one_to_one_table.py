"""create profiles one to one table

Revision ID: 959fbb019f33
Revises: d9161b360f4b
Create Date: 2024-07-28 19:29:49.062237

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "959fbb019f33"
down_revision: Union[str, None] = "d9161b360f4b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "profiles",
        sa.Column("first_name", sa.String(length=40), nullable=True),
        sa.Column("last_name", sa.String(length=40), nullable=True),
        sa.Column("bio", sa.Text(), server_default="", nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("profiles")
    # ### end Alembic commands ###
