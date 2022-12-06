"""add user table

Revision ID: efef0a235bc1
Revises: 3b77ff09b477
Create Date: 2022-12-06 11:37:17.623307

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision = 'efef0a235bc1'
down_revision = '3b77ff09b477'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                     sa.Column('id', sa.Integer, nullable = False),
                     sa.Column('email', sa.String, nullable = False),
                     sa.Column('password', sa.String, nullable = False),
                     sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable = False, server_default = sa.text('now()')),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email')
                     )
    pass


def downgrade():
    op.drop_table('users')
    pass
