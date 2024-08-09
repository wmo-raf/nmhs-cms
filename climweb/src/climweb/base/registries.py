import logging

from .registry import Registry, Instance

logger = logging.getLogger(__name__)


class Plugin(Instance):

    def get_urls(self):
        """
        If needed root urls related to the plugin can be added here.

        Example:

            def get_urls(self):
                from . import api_urls

                return [
                    path('some-url/', include(api_urls, namespace=self.type)),
                ]

            # api_urls.py
            from django.urls import re_path

            urlpatterns = [
                url(r'some-view^$', SomeView.as_view(), name='some_view'),
            ]

        :return: A list containing the urls.
        :rtype: list
        """

        return []

    def get_home_subpage_types(self):
        """
        If needed wagtail page types related to the plugin, to be added to under homepage,  can be added here.

        Example:

            def get_home_subpage_types(self):
                return ["plugin.PluginPage"]

        :return: A list containing the home subpage types.
        :rtype: list
        """

        return []


class PluginRegistry(Registry):
    """
    With the plugin registry it is possible to register new plugins. A plugin is an
    abstraction made specifically for ClimWeb. It allows to extend and develop specific functionalities on top of ClimWeb.
    """

    name = "plugin"

    @property
    def urls(self):
        """
        Returns a list of all the urls that are in the registered instances. They
        are going to be added to the root url config.

        :return: The urls of the registered instances.
        :rtype: list
        """

        urls = []
        for types in self.registry.values():
            urls += types.get_urls()
        return urls

    @property
    def home_subpage_types(self):
        """
        Returns a list of all the home subpage types that are in the registered instances.

        :return: The home subpage types of the registered instances.
        :rtype: list
        """

        home_subpage_types = []
        for types in self.registry.values():
            home_subpage_types += types.get_home_subpage_types()
        return home_subpage_types


plugin_registry = PluginRegistry()
