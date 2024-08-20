#!/usr/bin/env python3

from dotenv import load_dotenv
from lbrc_flask.database import db
from alembic.config import Config
from alembic import command
from faker import Faker

fake = Faker()

# Load environment variables from '.env' file.
load_dotenv()

from template import create_app

application = create_app()
application.app_context().push()
db.create_all()

alembic_cfg = Config("alembic.ini")
command.stamp(alembic_cfg, "head")

# TO DO: Create test data

db.session.close()
