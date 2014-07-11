"""
Models related utility functions
"""

import importlib


def get_models(application, get_app_models=True, return_dict=False):
    """
    Processes the passed application package and returns all SQLAlchemy models for the application.

    :param get_app_models: Indicates if the apps present in the application should also be searched for models (default True)

    """

    if return_dict:
        all_models = {}
    else:
        all_models = []

    if hasattr(application, 'models') and hasattr(application.models, '__all__'):

        if return_dict:
            all_models['__main__'] = []

        for M in application.models.__all__:
            models_module = __import__(application.models.__name__, globals(), locals(), ['__all__'], -1)
            M = getattr(models_module, M)
            if hasattr(M, '__tablename__'):
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

            models_module = __import__(application.apps.__name__ + '.' + app_name + '.models', globals(), locals(), ['__all__'], -1)
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

    for col in model.__table__.columns.keys():

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
