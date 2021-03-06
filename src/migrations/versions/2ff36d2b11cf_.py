"""empty message

Revision ID: 2ff36d2b11cf
Revises: 44c7225ea02a
Create Date: 2018-05-05 11:48:45.062970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ff36d2b11cf'
down_revision = '44c7225ea02a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('requirements',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('distribution_name', sa.String(length=255), nullable=True),
    sa.Column('credits', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requirements')
    # ### end Alembic commands ###
