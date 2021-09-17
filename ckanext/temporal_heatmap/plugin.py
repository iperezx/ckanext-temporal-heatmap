import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.temporal_heatmap.lib.helpers import (get_generated_temporal_data)

class TemporalHeatmapPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer,inherit=True)
    plugins.implements(plugins.IResourceView, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)


    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'temporal-heatmap')


    # ITemplateHelpers
    def get_helpers(self):
        return {'get_generated_temporal_data': get_generated_temporal_data}