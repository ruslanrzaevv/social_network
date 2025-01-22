from rest_framework import routers

class CustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix':'List'},
        ),

        routers.Route(
            url=r'^{prefix}/lookup$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=False,
            initkwargs={'suffix':'Detail'},
        ),    

    ]