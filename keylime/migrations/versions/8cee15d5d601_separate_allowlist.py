"""separate_allowlist

Revision ID: 8cee15d5d601
Revises: eb869a77abd1
Create Date: 2021-01-14 14:06:53.230988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cee15d5d601'
down_revision = 'eb869a77abd1'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()


def upgrade_registrar():
    pass


def downgrade_registrar():
    pass


def upgrade_cloud_verifier():
    with op.batch_alter_table('verifiermain') as batch_op:
        batch_op.add_column(sa.Column('allowlist_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_verifiermain_allowlists', 'allowlists',
                                    ['allowlist_id'], ['id'])
        batch_op.drop_column('tpm_policy')
        batch_op.drop_column('vtpm_policy')
        batch_op.drop_column('allowlist')


def downgrade_cloud_verifier():
    pass
