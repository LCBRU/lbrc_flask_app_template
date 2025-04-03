import alembic.config

from {{cookiecutter.project_slug}} import create_app
from {{cookiecutter.project_slug}}.security import init_authorization
alembicArgs = [
    '--raiseerr',
    'upgrade', 'head',
]
alembic.config.main(argv=alembicArgs)

application = create_app()
application.app_context().push()

init_authorization()
