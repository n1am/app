"""Add alias transfer token expiration

Revision ID: a7bcb872c12a
Revises: 36646e5dc6d9
Create Date: 2022-06-13 10:29:39.614171

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7bcb872c12a'
down_revision = '36646e5dc6d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alias', sa.Column('transfer_token_expiration', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('alias', 'transfer_token_expiration')
    # ### end Alembic commands ###