"""added the byline and author's name to the project

Revision ID: 60213a5e602a
Revises: 
Create Date: 2018-12-17 18:22:22.259215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60213a5e602a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('author', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'author')
    # ### end Alembic commands ###
