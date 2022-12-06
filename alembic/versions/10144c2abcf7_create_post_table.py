"""create  post table

Revision ID: 10144c2abcf7
Revises: 
Create Date: 2022-12-06 10:49:49.305017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10144c2abcf7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer,nullable = False, primary_key= True),sa.Column('title', sa.String, nullable = False)) 
    pass


def downgrade():
    op.drop_table('posts',)
    pass
