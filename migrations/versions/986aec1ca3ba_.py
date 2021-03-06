"""empty message

Revision ID: 986aec1ca3ba
Revises: 
Create Date: 2022-02-06 22:25:59.280173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '986aec1ca3ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # commands auto generated by Alembic - please adjust!
    op.create_table(
        'URL',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('long', sa.String(), nullable=True),
        sa.Column('short', sa.String(), nullable=True),
        sa.Column('total_clicks', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_URL_id'), 'URL', ['id'], unique=False)
    op.create_index(op.f('ix_URL_long'), 'URL', ['long'], unique=True)
    op.create_index(op.f('ix_URL_short'), 'URL', ['short'], unique=True)
    # end Alembic commands ###


def downgrade():
    # commands auto generated by Alembic - please adjust!
    op.drop_index(op.f('ix_URL_short'), table_name='URL')
    op.drop_index(op.f('ix_URL_long'), table_name='URL')
    op.drop_index(op.f('ix_URL_id'), table_name='URL')
    op.drop_table('URL')
    # end Alembic commands ###
