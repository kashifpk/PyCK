import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import (
    Base,
    Page
    )

def populate_app(engine, db_session):
    Base.metadata.create_all(engine)
    with transaction.manager:
        for i in range(35):
            model = Page('Test %i' % i, 'Just testing number %i' % i)
            db_session.add(model)
    
