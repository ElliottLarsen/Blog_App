"""empty message

Revision ID: 293126d496fa
Revises: bb1e359c3065
Create Date: 2022-08-21 19:52:29.915804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '293126d496fa'
down_revision = 'bb1e359c3065'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('reply')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reply',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('post_id', sa.INTEGER(), nullable=True),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('comment')
    # ### end Alembic commands ###