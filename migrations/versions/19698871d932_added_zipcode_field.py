"""added zipcode field

Revision ID: 19698871d932
Revises: 34dada2362b1
Create Date: 2018-05-04 19:27:02.154882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19698871d932'
down_revision = '34dada2362b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('zipcode', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'zipcode')
    # ### end Alembic commands ###
