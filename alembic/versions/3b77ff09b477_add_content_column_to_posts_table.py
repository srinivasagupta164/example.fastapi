"""add content column to posts table

Revision ID: 3b77ff09b477
Revises: 10144c2abcf7
Create Date: 2022-12-06 11:31:08.335414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b77ff09b477'
down_revision = '10144c2abcf7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable = False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
