"""Add currency to ticker

Revision ID: 8484b11f633f
Revises: 508be5bf5d21
Create Date: 2021-10-05 00:03:11.429328

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "8484b11f633f"
down_revision = "508be5bf5d21"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "tickers",
        sa.Column(
            "currency",
            sa.Enum("USD", "KRW", name="currency", native_enum=False),
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("tickers", "currency")
    # ### end Alembic commands ###