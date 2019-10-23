"""add language to posts

Revision ID: 308af6d6c052
Revises: e1edab1fa298
Create Date: 2019-10-23 18:27:02.964758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '308af6d6c052'
down_revision = 'e1edab1fa298'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
