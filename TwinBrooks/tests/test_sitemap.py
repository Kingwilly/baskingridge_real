from TwinBrooks.sitemap import TwinBrooksSitemap


class TestTwinBrooksSitemap():
    def test_items(self):
        new_site_map = TwinBrooksSitemap()
        items = new_site_map.items()

        assert isinstance(items, list), 'Should output an array of views'

    def test_item_location(self):
        new_site_map = TwinBrooksSitemap()
        items = new_site_map.items()

        for link in items:
            new_site_map.location(link)

        assert isinstance(items, list), 'Every value in the items array should output a valid url'
