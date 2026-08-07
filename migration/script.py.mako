"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision}
Create Date: ${create_date}

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "${up_revision}"

down_revision: Union[str,None] = ${down_revision | repr}

branch_labels = ${branch_labels | repr}

depends_on = ${depends_on | repr}



def upgrade():

    pass



def downgrade():

    pass