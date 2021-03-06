"""empty message

Revision ID: 6dd1e66336af
Revises: 94c98286e9e1
Create Date: 2018-10-01 16:38:33.480612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dd1e66336af'
down_revision = '94c98286e9e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_deactivated', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_deactivated')
    # ### end Alembic commands ###
