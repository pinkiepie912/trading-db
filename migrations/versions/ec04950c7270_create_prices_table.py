"""create prices table

Revision ID: ec04950c7270
Revises: 845650b96c82
Create Date: 2021-03-24 23:00:34.912471

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "ec04950c7270"
down_revision = "845650b96c82"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "prices",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("ticker", sa.String(length=255), nullable=False),
        sa.Column("adjclose", sa.Float(), nullable=False),
        sa.Column("close", sa.Float(), nullable=False),
        sa.Column("high", sa.Float(), nullable=False),
        sa.Column("low", sa.Float(), nullable=False),
        sa.Column("open", sa.Float(), nullable=False),
        sa.Column("volume", sa.BigInteger(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("currency", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_date_name", "prices", [sa.text("date DESC"), "name"], unique=False
    )
    op.create_index(
        "ix_date_ticker",
        "prices",
        [sa.text("date DESC"), "name"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_date_ticker", table_name="prices")
    op.drop_index("ix_date_name", table_name="prices")
    op.drop_table("prices")
    # ### end Alembic commands ###
