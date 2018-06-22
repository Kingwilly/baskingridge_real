from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class TwinBrooksSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""

    def items(self):
        # Return list of url names for views to include in sitemap
        return [
            'home_static',
            'history_static',
            'membership_static',
            'guests_static',
            'events_static',
            'contact_static',
        ]

    def location(self, item):
        return reverse(item)


sitemaps = {'views': TwinBrooksSitemap}
