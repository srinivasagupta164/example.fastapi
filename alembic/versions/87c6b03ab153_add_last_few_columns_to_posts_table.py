"""add last few columns to posts table

Revision ID: 87c6b03ab153
Revises: e608419eec68
Create Date: 2022-12-06 12:05:51.319511

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision = '87c6b03ab153'
down_revision = 'e608419eec68'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False, server_default = 'True'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable = False, server_default = sa.text('now()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published_at')
    op.drop_column('posts', 'created_at')
    pass
