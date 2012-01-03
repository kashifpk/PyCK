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
        model = Page('Test', 'Just testing')
        db_session.add(model)
    
