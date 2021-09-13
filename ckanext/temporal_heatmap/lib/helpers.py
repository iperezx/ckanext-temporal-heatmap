import re
import os
import logging
import json

log = logging.getLogger('ckanext.temporal-heatmap.lib.helpers')


def get_temporal_extent(resource):
    return None

def get_generated_temporal_data(resource):
    temporal_extent = resource.get('temporal extent')
    if temporal_extent is not None:
        temporal_data = generate_temporal_data(temporal_extent)
        return temporal_data
    return None
