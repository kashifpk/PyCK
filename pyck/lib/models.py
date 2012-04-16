"""
Models related utility functions
"""

import importlib

def get_models(application, get_app_models=True):
    """
    Processes the passed application package and returns all SQLAlchemy models for the application.
    
    :param get_app_models: Indicates if the apps present in the application should also be searched for models (default True)
    
    """
    
    all_models = []
    
    if hasattr(application, 'models') and hasattr(application.models, '__all__'):
        for M in application.models.__all__:
            models_module = __import__(application.models.__name__, globals(), locals(), ['__all__'], -1)
            M = getattr(models_module, M)
            if hasattr(M, '__tablename__'):
                all_models.append(M)
    
    if get_app_models:
        for app in application.apps.enabled_apps:
            models_module = __import__(application.apps.__name__ + '.' + app + '.models', globals(), locals(), ['__all__'], -1)
            
            for M in models_module.__all__:
                #models_module = __import__(application.models.__name__, globals(), locals(), ['__all__'], -1)
                M = getattr(models_module, M)
                if hasattr(M, '__tablename__'):
                    all_models.append(M)
    
    
    return all_models