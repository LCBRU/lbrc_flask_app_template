#!/usr/bin/env python3

from dotenv import load_dotenv
from lbrc_flask.database import db


# Load environment variables from '.env' file.
load_dotenv()

from alembic_spike import create_app

application = create_app()
application.app_context().push()
db.create_all()
db.session.close()

from alembic.config import Config
from alembic import command
alembic_cfg = Config("alembic.ini")
command.stamp(alembic_cfg, "head")
