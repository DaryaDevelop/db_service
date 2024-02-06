"""empty message

Revision ID: 94b7902f9c02
Revises: 88ee6613d079
Create Date: 2024-02-04 17:28:52.810784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94b7902f9c02'
down_revision = '88ee6613d079'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uuid', sa.Uuid(), nullable=False))
        batch_op.create_unique_constraint(None, ['uuid'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('uuid')

    # ### end Alembic commands ###
