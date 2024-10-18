from grass.gunittest.case import TestCase
from grass.gunittest.gmodules import SimpleModule
from grass.gunittest.gmodules import call_module

# region set is the default NC location
# downloaded from the website
ans1 = """34300:270:0:640445:215235:640445:215235
34300:910:0:640435:215215:640435:215215
39000:217:0:637165:215865:637165:215865
39000:262:0:637175:215845:637175:215845
39000:405:0:630905:220755:630905:220755
39000:862:0:630895:220745:630895:220745
43600:405:0:630965:219455:630965:219455
43600:862:0:630955:219455:630955:219455
39000:270:90:644905:228125:644995:228125
39000:910:809.5677859204:637245:215395:638015:215145
43600:217:873.2124598286:631015:219335:631865:219135
34300:946:922.6592003551:640425:215205:639505:215275
39000:720:1116.2884931773:635165:227195:634105:227545
39000:946:1246.194206374:637245:215395:638435:215025
39000:583:1388.5243966168:630945:220925:630025:221965
39000:921:2137.1242359769:634335:215295:632215:215025
34300:262:2261.083810919:640425:215205:638275:215905
43600:583:2616.811036357:630765:219455:630025:221965
43600:921:3178.0497164141:630755:219295:630055:216195
34300:217:3260.1380338875:640425:215205:637165:215175
39000:766:3510:635155:227115:631645:227115
39000:948:3645.065157168:633815:216615:630535:215025
43600:948:4060.7881008494:630755:219295:630055:215295
39000:945:4110.0121654321:633815:216615:630025:215025
43600:945:4331.9510615888:630755:219295:630025:215025
43600:262:6604.4606138579:631035:219435:637535:218265
43600:766:7416.8726563155:631035:219455:631535:226855
43600:910:7869.2439281039:631015:219335:638705:217665
43600:270:8002.0247437758:631035:219435:639035:219255
34300:921:8211.9729663462:640425:215205:632215:215025
43600:720:8217.4752813744:631035:219455:633905:227155
43600:946:8569.5857542824:631005:219295:638435:215025
34300:405:8750.2799955201:640425:215205:631675:215275
34300:862:9298.6074226198:640425:215205:631135:215605
34300:948:9891.6378825754:640425:215205:630535:215025
34300:945:10401.5575756711:640425:215205:630025:215025
34300:583:12384.4458899056:640585:215495:630025:221965
34300:720:13428.00059577:640585:215495:633925:227155
34300:766:14498.0343495248:640585:215495:631615:226885
"""

ans2 = """34300:270:0:640445:215235:640445:215235:Dam/Weir:CZig
34300:910:0:640435:215215:640435:215215:Dam/Weir:CZbg
39000:217:0:637165:215865:637165:215865:Lake/Pond:CZfg
39000:262:0:637175:215845:637175:215845:Lake/Pond:CZlg
39000:405:0:630905:220755:630905:220755:Lake/Pond:CZbg
39000:862:0:630895:220745:630895:220745:Lake/Pond:CZam
43600:405:0:630965:219455:630965:219455:Reservoir:CZbg
43600:862:0:630955:219455:630955:219455:Reservoir:CZam
39000:270:90:644905:228125:644995:228125:Lake/Pond:CZig
39000:910:809.5677859204:637245:215395:638015:215145:Lake/Pond:CZbg
43600:217:873.2124598286:631015:219335:631865:219135:Reservoir:CZfg
34300:946:922.6592003551:640425:215205:639505:215275:Dam/Weir:CZam
39000:720:1116.2884931773:635165:227195:634105:227545:Lake/Pond:CZam
39000:946:1246.194206374:637245:215395:638435:215025:Lake/Pond:CZam
39000:583:1388.5243966168:630945:220925:630025:221965:Lake/Pond:CZve
39000:921:2137.1242359769:634335:215295:632215:215025:Lake/Pond:Km
34300:262:2261.083810919:640425:215205:638275:215905:Dam/Weir:CZlg
43600:583:2616.811036357:630765:219455:630025:221965:Reservoir:CZve
43600:921:3178.0497164141:630755:219295:630055:216195:Reservoir:Km
34300:217:3260.1380338875:640425:215205:637165:215175:Dam/Weir:CZfg
39000:766:3510:635155:227115:631645:227115:Lake/Pond:CZg
39000:948:3645.065157168:633815:216615:630535:215025:Lake/Pond:CZam
43600:948:4060.7881008494:630755:219295:630055:215295:Reservoir:CZam
39000:945:4110.0121654321:633815:216615:630025:215025:Lake/Pond:CZbg
43600:945:4331.9510615888:630755:219295:630025:215025:Reservoir:CZbg
43600:262:6604.4606138579:631035:219435:637535:218265:Reservoir:CZlg
43600:766:7416.8726563155:631035:219455:631535:226855:Reservoir:CZg
43600:910:7869.2439281039:631015:219335:638705:217665:Reservoir:CZbg
43600:270:8002.0247437758:631035:219435:639035:219255:Reservoir:CZig
34300:921:8211.9729663462:640425:215205:632215:215025:Dam/Weir:Km
43600:720:8217.4752813744:631035:219455:633905:227155:Reservoir:CZam
43600:946:8569.5857542824:631005:219295:638435:215025:Reservoir:CZam
34300:405:8750.2799955201:640425:215205:631675:215275:Dam/Weir:CZbg
34300:862:9298.6074226198:640425:215205:631135:215605:Dam/Weir:CZam
34300:948:9891.6378825754:640425:215205:630535:215025:Dam/Weir:CZam
34300:945:10401.5575756711:640425:215205:630025:215025:Dam/Weir:CZbg
34300:583:12384.4458899056:640585:215495:630025:221965:Dam/Weir:CZve
34300:720:13428.00059577:640585:215495:633925:227155:Dam/Weir:CZam
34300:766:14498.0343495248:640585:215495:631615:226885:Dam/Weir:CZg
"""

newrast_ref = """39000:100:0:630005:220195:630005:220195
43600:100:700:630705:219375:630005:219375
34300:100:4320:640675:215275:644995:215275
"""


class TestRDistance(TestCase):
    map1 = "lakes"
    map2 = "geology"
    separator = ":"
    sort = "asc"

    @classmethod
    def setUpClass(cls):
        """Ensures expected computational region"""
        cls.use_temp_region()
        cls.runModule("g.region", raster="elevation")

    @classmethod
    def tearDownClass(cls):
        new_rast = "new_rast"
        cls.runModule("g.remove", flags="f", type="raster", name=new_rast)
        cls.del_temp_region()

    def setUp(self):
        self.r_dist = SimpleModule(
            "r.distance", map=(self.map1, self.map2), separator=",", sort=self.sort
        )
        self.output = call_module(
            "r.distance", map=(self.map1, self.map2), separator=":", sort=self.sort
        )

    # asserting if the output of map=(lakes,geology)
    # from NC data is correct
    def test_check_correct_output(self):
        self.assertMultiLineEqual(ans1, self.output)
        # check if l flag gives correct output
        lflag_output = call_module(
            "r.distance",
            map=(self.map1, self.map2),
            separator=":",
            sort=self.sort,
            flags="l",
        )
        self.assertMultiLineEqual(ans2, lflag_output)


    ## creates a new raster map using r.mapcalc.simple
    ## and tests if output is correct
    def test_newraster_dist_correct(self):
        # test 1
        new_rast = "new_rast"
        self.runModule("r.mapcalc.simple", expression="100", output=new_rast)
        new_rast_ans = call_module(
            "r.distance",
            map=(self.map1, new_rast),
            sort = self.sort
        )
        self.assertMultiLineEqual(new_rast_ans, newrast_ref)

    #Raster maps elevation and elevation_shade can't be the arguments
    def test_rdistance_fail_when_elevation(self):
        self.assertRasterExists(self.map1)
        self.assertRasterExists(self.map2)
        self.assertModule(self.r_dist)

        ## elevation as one of the arguments is expected
        ## to fail
        self.assertModuleFail(
            "r.distance",
            map=("elevation","geology"), #invalid
            separator = self.separator,
            sort = self.sort,
            msg = "Raster map <elevation> is not CELL"
        )
        ## elevation as one of the arguments is expected
        ## to fail
        self.assertModuleFail(
            "r.distance",
            map=("geology", "elevation_shade"), #invalid
            separator = self.separator,
            sort = self.sort,
            msg = "Raster map <elevation_shade> is not CELL"
        )


if __name__ == "__main__":
    from grass.gunittest.main import test
    test()
