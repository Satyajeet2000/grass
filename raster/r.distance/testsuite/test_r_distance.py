from grass.gunittest.case import TestCase


class TestRDistance(TestCase):
    map = 'geology,lakes'
    separator = ':'
    sort = 'asc'
    map_list = map.split(',')
    map1, map2 = map_list

    @classmethod
    def setUpClass(cls):
        """Set up the test environment and raster maps."""
        cls.use_temp_region()
        cls.valid_maps = [
            "geology", "basins", "elevation", "elevation_shade",
            "lakes", "landuse", "limits_aspect",
            "limits_slope", "soils"
        ]
        cls.runModule('g.region', raster=cls.map1) ## this is where all of our valid maps go
        cls.runModule('g.region', raster=cls.map2) ## this is where all of our valid maps go

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests."""
        cls.runModule('g.remove', flags='f', type='raster', name='map1,map2')

    # def run_r_distance(self, map1, map2, separator, sort):
    #     """Helper method to run the r.distance command."""
    #     command = f"r.distance map={map1},{map2} separator={separator} sort={sort}"
    #     # Simulate running the command (for testing, we won't actually run it)
    #     print(f"Running command: {command}")
    #     # Uncomment the following line to actually run the command
    #     return subprocess.run(command, shell=True, check=True)

    def test_assert_rdistance(self):
        self.assertModule(
            "r.distance",
            map=(self.map1, self.map2),
            separator = self.separator,
            sort = self.sort
        )
        assert self.map1 in self.valid_maps, f"{map1} is not a valid map."
        assert self.map2 in self.valid_maps, f"{map2} is not a valid map."
        assert self.separator in [":", "|", ",", " ", "\t", "\n"], f"{separator} is not a valid separator."
        assert self.sort in ["asc", "desc"], f"{sort} is not a valid sort option."


if __name__ == '__main__':
    from grass.gunittest.main import test
    test()
