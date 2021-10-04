"""Use SA enum

Revision ID: 508be5bf5d21
Revises: b17069a2f80c
Create Date: 2021-10-04 21:47:57.757534

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "508be5bf5d21"
down_revision = "b17069a2f80c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("prices", "stock_type")
    op.add_column(
        "tickers",
        sa.Column(
            "stock_type",
            sa.Enum("STOCK", "ETF", name="stocktype", native_enum=False),
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("tickers", "stock_type")
    op.add_column(
        "prices",
        sa.Column("stock_type", mysql.VARCHAR(length=255), nullable=False),
    )
    # ### end Alembic commands ###