"""empty message

Revision ID: 80331bdec4a8
Revises: 
Create Date: 2019-11-05 17:13:35.002041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80331bdec4a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_title'), 'product', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_title'), table_name='product')
    op.drop_table('product')
    # ### end Alembic commands ###
