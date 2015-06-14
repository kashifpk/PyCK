import os
from pyramid.response import FileResponse
from pyramid.view import view_config


@view_config(route_name="favicon")
def favicon_view(request):
    "Favorite icon display"

    here = os.path.dirname(__file__)
    icon = os.path.join(here, "static", "favicon.ico")
    return FileResponse(icon, request=request)


def application_routes(config):
    "Routes for the main application, excluding sub-app routes"

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route("favicon", "/favicon.ico")

    config.add_route('home', '/')
    config.add_route('contact', '/contact')

    config.add_route('pyckauth_login', '/login')
    config.add_route('pyckauth_logout', '/logout')
    config.add_route('pyckauth_change_pass', '/change_password')
    config.add_route('pyckauth_manager', '/auth')
    config.add_route('pyckauth_users', '/auth/users')
    config.add_route('pyckauth_permissions', '/auth/permissions')
    config.add_route('pyckauth_routes', '/auth/routes')
