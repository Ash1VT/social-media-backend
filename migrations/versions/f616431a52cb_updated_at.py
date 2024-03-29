"""updated_at

Revision ID: f616431a52cb
Revises: 4fbd40052c37
Create Date: 2023-01-28 03:05:45.781168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f616431a52cb'
down_revision = '4fbd40052c37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('post', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'updated_at')
    op.drop_column('comment', 'updated_at')
    # ### end Alembic commands ###
