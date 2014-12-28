"""
Models related utility functions
"""

import importlib


def get_models(application, get_app_models=True,
               return_dict=False, ignore_auth_tables=True):
    """
    Processes the passed application package and returns all SQLAlchemy models for the application.

    :param get_app_models: Indicates if the apps present in the application should also be searched for models (default True)

    """

    auth_tables = ('users', 'permissions',
                   'user_permissions', 'route_permissions')

    if return_dict:
        all_models = {}
    else:
        all_models = []

    if hasattr(application, 'models') and hasattr(application.models, '__all__'):

        if return_dict:
            all_models['__main__'] = []

        for M in application.models.__all__:
            #models_module = __import__(application.models.__name__, globals(), locals(), ['__all__'], -1)
            models_module = importlib.import_module(application.models.__name__)
            M = getattr(models_module, M)
            if hasattr(M, '__tablename__'):
                if ignore_auth_tables:
                    if M.__tablename__ in auth_tables:
                        continue

                if return_dict:
                    all_models['__main__'].append(M)
                else:
                    all_models.append(M)

    if get_app_models:
        for app in application.apps.enabled_apps:
            if str == type(app):
                app_name = app
            else:
                app_name = app.APP_NAME

            #models_module = __import__(application.apps.__name__ + '.' + app_name + '.models', globals(), locals(), ['__all__'], -1)
            try:
                models_module = importlib.import_module(application.apps.__name__ + '.' + app_name + '.models')
            except ImportError:
                continue

            if return_dict:
                all_models[app_name] = []

            for M in models_module.__all__:
                #models_module = __import__(application.models.__name__, globals(), locals(), ['__all__'], -1)
                M = getattr(models_module, M)
                if hasattr(M, '__tablename__'):
                    if return_dict:
                        all_models[app_name].append(M)
                    else:
                        all_models.append(M)

    return all_models


def get_columns(model, col_type=None):
    """
    Returns column objects of the current model

    :param col_type:
        (Optional) The type of columns to return. Currently supported types are 'primary_key' and 'foreign_key'
    """

    ret_cols = []

    for col in list(model.__table__.columns.keys()):

        obj = getattr(model, col)

        if not col_type:
            ret_cols.append(obj)

        elif 'primary_key' == col_type:
            if True == obj.property.columns[0].primary_key:
                ret_cols.append(obj)

        elif 'foreign_key' == col_type:
            if len(obj.property.columns[0].foreign_keys) > 0:
                ret_cols.append(obj)

    return ret_cols


def models_dict_to_list(models):
    """
    Given a models dict containing subapp names as keys and models as a list of values
    return an aggregated list of all models
    """
    
    all_models = []
    
    if isinstance(models, dict):
        
        for _, app_models in list(models.items()):
            all_models.extend(app_models)

    else:
        all_models = models

    return all_models


def get_model_record_counts(db_session, models):
    "returns record counts for given models"

    record_counts = {}

    for model in models:
        record_counts[model.__tablename__] = db_session.query(model).count()

    return record_counts