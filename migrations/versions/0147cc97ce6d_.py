"""empty message

Revision ID: 0147cc97ce6d
Revises: 42612003f43f
Create Date: 2017-04-27 14:12:23.632672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0147cc97ce6d'
down_revision = '42612003f43f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('email', sa.String(length=80), nullable=True))
    op.add_column('user_profile', sa.Column('firstname', sa.String(length=80), nullable=True))
    op.add_column('user_profile', sa.Column('lastname', sa.String(length=80), nullable=True))
    op.drop_constraint(u'user_profile_username_key', 'user_profile', type_='unique')
    op.create_unique_constraint(None, 'user_profile', ['email'])
    op.drop_column('user_profile', 'username')
    op.drop_column('user_profile', 'first_name')
    op.drop_column('user_profile', 'last_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('last_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.add_column('user_profile', sa.Column('first_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.add_column('user_profile', sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user_profile', type_='unique')
    op.create_unique_constraint(u'user_profile_username_key', 'user_profile', ['username'])
    op.drop_column('user_profile', 'lastname')
    op.drop_column('user_profile', 'firstname')
    op.drop_column('user_profile', 'email')
    # ### end Alembic commands ###
