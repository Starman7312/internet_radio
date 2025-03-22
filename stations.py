class stations:
    def __init__(self):
        self._stations = {}

        radio_1 = {'BBC Radio 1': [
            ['Cloudfront Global 96 Kbps', 'http://as-hls-ww.live.cf.md.bbci.co.uk/pool_01505109/live/ww/bbc_radio_one/bbc_radio_one.isml/bbc_radio_one-audio%3d96000.norewind.m3u8'],
            ['Cloudfront Global 48 Kbps', 'http://as-hls-ww.live.cf.md.bbci.co.uk/pool_01505109/live/ww/bbc_radio_one/bbc_radio_one.isml/bbc_radio_one-audio%3d48000.norewind.m3u8'],
            ['Akamai Global Adaptive', 'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/hls/nonuk/pc_hd_abr_v2/ak/bbc_radio_one.m3u8'],
            ['Akamai Global 96 Kbps', 'http://as-hls-ww-live.akamaized.net/pool_01505109/live/ww/bbc_radio_one/bbc_radio_one.isml/bbc_radio_one-audio%3d96000.norewind.m3u8'],
            ['Akamai Global 48 Kbps', 'http://as-hls-ww-live.akamaized.net/pool_01505109/live/ww/bbc_radio_one/bbc_radio_one.isml/bbc_radio_one-audio%3d48000.norewind.m3u8'],
            ['Akamai Global 48-96 Kbps', 'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/dash/nonuk/pc_hd_abr_v2/ak/bbc_radio_one.mpd'],
            ['Cloudfront Global 48-96 Kbps',
             'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/dash/nonuk/pc_hd_abr_v2/cf/bbc_radio_one.mpd']
        ]
        }
        radio_2 = {'BBC Radio 2': [
            ['Cloudfront Global 96 Kbps', 'http://as-hls-ww.live.cf.md.bbci.co.uk/pool_74208725/live/ww/bbc_radio_two/bbc_radio_two.isml/bbc_radio_two-audio%3d96000.norewind.m3u8'],
            ['Cloudfront Global 48 Kbps', 'http://as-hls-ww.live.cf.md.bbci.co.uk/pool_74208725/live/ww/bbc_radio_two/bbc_radio_two.isml/bbc_radio_two-audio%3d48000.norewind.m3u8'],
            ['Akamai UK 320 Kbps', 'http://as-hls-uk-live.akamaized.net/pool_74208725/live/uk/bbc_radio_two/bbc_radio_two.isml/bbc_radio_two-audio%3d320000.norewind.m3u8'],
            ['Akamai UK 128 Kbps', 'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/hls/nonuk/pc_hd_abr_v2/ak/bbc_radio_two.m3u8'],
            ['Akamai Global Adaptive', 'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/hls/nonuk/pc_hd_abr_v2/ak/bbc_radio_two.m3u8'],
            ['Akamai Global 96 Kbps', 'http://as-hls-ww-live.akamaized.net/pool_74208725/live/ww/bbc_radio_two/bbc_radio_two.isml/bbc_radio_two-audio%3d96000.norewind.m3u8'],
            ['Akamai Global 48 Kbps', 'http://as-hls-ww-live.akamaized.net/pool_74208725/live/ww/bbc_radio_two/bbc_radio_two.isml/bbc_radio_two-audio%3d48000.norewind.m3u8'],
            ['Akamai Global 48-96 Kbps', 'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/dash/nonuk/pc_hd_abr_v2/ak/bbc_radio_two.mpd'],
            ['Cloudfront Global 48-96 Kbps',
             'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/dash/nonuk/pc_hd_abr_v2/cf/bbc_radio_two.mpd']
        ]
        }
        radio_3 = {'BBC Radio 3': [
            ['Cloudfront Global 96 Kbps', 'http://as-hls-ww.live.cf.md.bbci.co.uk/pool_23461179/live/ww/bbc_radio_three/bbc_radio_three.isml/bbc_radio_three-audio%3d96000.norewind.m3u8'],
            ['Cloudfront Global 48 Kbps', 'http://as-hls-ww.live.cf.md.bbci.co.uk/pool_23461179/live/ww/bbc_radio_three/bbc_radio_three.isml/bbc_radio_three-audio%3d48000.norewind.m3u8'],
            ['Akamai Global Adaptive', 'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/hls/nonuk/pc_hd_abr_v2/ak/bbc_radio_three.m3u8'],
            ['Akamai Global 96 Kbps', 'http://as-hls-ww-live.akamaized.net/pool_23461179/live/ww/bbc_radio_three/bbc_radio_three.isml/bbc_radio_three-audio%3d96000.norewind.m3u8'],
            ['Akamai Global 48 Kbps', 'http://as-hls-ww-live.akamaized.net/pool_23461179/live/ww/bbc_radio_three/bbc_radio_three.isml/bbc_radio_three-audio%3d48000.norewind.m3u8'],
            ['Akamai Global 48-96 Kbps', 'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/dash/nonuk/pc_hd_abr_v2/ak/bbc_radio_three.mpd'],
            ['Cloudfront Global 48-96 Kbps',
             'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/dash/nonuk/pc_hd_abr_v2/cf/bbc_radio_three.mpd']
        ]
        }
        radio_4 = {'BBC Radio 4': [
            ['Cloudfront Global 96 Kbps', 'http://as-hls-ww.live.cf.md.bbci.co.uk/pool_55057080/live/ww/bbc_radio_fourfm/bbc_radio_fourfm.isml/bbc_radio_fourfm-audio%3d96000.norewind.m3u8'],
            ['Cloudfront Global 48 Kbps', 'http://as-hls-ww.live.cf.md.bbci.co.uk/pool_55057080/live/ww/bbc_radio_fourfm/bbc_radio_fourfm.isml/bbc_radio_fourfm-audio%3d48000.norewind.m3u8'],
            ['Akamai Global Adaptive', 'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/hls/nonuk/pc_hd_abr_v2/ak/bbc_radio_fourfm.m3u8'],
            ['Akamai Global 96 Kbps', 'http://as-hls-ww-live.akamaized.net/pool_55057080/live/ww/bbc_radio_fourfm/bbc_radio_fourfm.isml/bbc_radio_fourfm-audio%3d96000.norewind.m3u8'],
            ['Akamai Global 48 Kbps', 'http://as-hls-ww-live.akamaized.net/pool_55057080/live/ww/bbc_radio_fourfm/bbc_radio_fourfm.isml/bbc_radio_fourfm-audio%3d48000.norewind.m3u8'],
            ['Akamai Global 48-96 Kbps', 'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/dash/nonuk/pc_hd_abr_v2/ak/bbc_radio_fourfm.mpd'],
            ['Cloudfront Global 48-96 Kbps',
             'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/dash/nonuk/pc_hd_abr_v2/cf/bbc_radio_fourfm.mpd']
        ]
        }
        radio_5 = {'BBC Radio 5 Live': [
            ['Cloudfront Global 96 Kbps', 'http://as-hls-ww.live.cf.md.bbci.co.uk/pool_89021708/live/ww/bbc_radio_five_live/bbc_radio_five_live.isml/bbc_radio_five_live-audio%3d96000.norewind.m3u8'],
            ['Cloudfront Global 48 Kbps', 'http://as-hls-ww.live.cf.md.bbci.co.uk/pool_89021708/live/ww/bbc_radio_five_live/bbc_radio_five_live.isml/bbc_radio_five_live-audio%3d48000.norewind.m3u8'],
            ['Akamai Global Adaptive', 'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/hls/nonuk/pc_hd_abr_v2/ak/bbc_radio_five_live.m3u8'],
            ['Akamai Global 96 Kbps', 'http://as-hls-ww-live.akamaized.net/pool_89021708/live/ww/bbc_radio_five_live/bbc_radio_five_live.isml/bbc_radio_five_live-audio%3d96000.norewind.m3u8'],
            ['Akamai Global 48 Kbps', 'http://as-hls-ww.live.cf.md.bbci.co.uk/pool_89021708/live/ww/bbc_radio_five_live/bbc_radio_five_live.isml/bbc_radio_five_live-audio%3d48000.norewind.m3u8'],
            ['Akamai Global 48-96 Kbps', 'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/dash/nonuk/pc_hd_abr_v2/ak/bbc_radio_five_live.mpd'],
            ['Cloudfront Global 48-96 Kbps',
             'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/dash/nonuk/pc_hd_abr_v2/cf/bbc_radio_five_live.mpd']
        ]
        }
        radio_5_extra = {'BBC Radio 5 Live Sports Extra': [
            ['Cloudfront UK Only 96 Kbps', 'http://as-hls-uk.live.cf.md.bbci.co.uk/pool_904/live/uk/bbc_radio_five_live_sports_extra/bbc_radio_five_live_sports_extra.isml/bbc_radio_five_live_sports_extra-audio%3d96000.norewind.m3u8'],
            ['Cloudfront UK Only 48 Kbps', 'http://as-hls-uk.live.cf.md.bbci.co.uk/pool_904/live/uk/bbc_radio_five_live_sports_extra/bbc_radio_five_live_sports_extra.isml/bbc_radio_five_live_sports_extra-audio%3d48000.norewind.m3u8'],
            ['Akamai UK Only Adaptive', 'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/hls/uk/pc_hd_abr_v2/ak/bbc_radio_five_live_sports_extra.m3u8'],
            ['Akamai UK Only 96 Kbps', 'hhttp://as-hls-uk-live.akamaized.net/pool_904/live/uk/bbc_radio_five_live_sports_extra/bbc_radio_five_live_sports_extra.isml/bbc_radio_five_live_sports_extra-audio%3d96000.norewind.m3u8'],
            ['Akamai UK Only 48 Kbps', 'http://as-hls-uk-live.akamaized.net/pool_904/live/uk/bbc_radio_five_live_sports_extra/bbc_radio_five_live_sports_extra.isml/bbc_radio_five_live_sports_extra-audio%3d48000.norewind.m3u8'],
            ['Akamai UK Only 48-96 Kbps', 'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/dash/uk/pc_hd_abr_v2/ak/bbc_radio_five_live_sports_extra.mpd'],
            ['Cloudfront UK Only 48-96 Kbps',
             'http://a.files.bbci.co.uk/ms6/live/3441A116-B12E-4D2F-ACA8-C1984642FA4B/audio/simulcast/dash/uk/pc_hd_abr_v2/cf/bbc_radio_five_live_sports_extra.mpd']
        ]
        }
        hereford = {'BBC Hereford & Worcester': [
            ['Unknown 96 Kbps', 'http://lstn.lv/bbcradio.m3u8?station=bbc_radio_hereford_worcester&bitrate=96000'],
            ['Akamai 96 Kbps', 'http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_hereford_worcester/bbc_radio_hereford_worcester.isml/bbc_radio_hereford_worcester-audio%3d96000.norewind.m3u8']
        ]
        }
        york = {'UoY Radio': [
            ['UoY Radio 192 Kbps', 'http://uryfs1.york.ac.uk/live-high'],
            ['UoY Radio 128 Kbps', 'http://uryfs1.york.ac.uk/live-high-ogg'],
            ['UoY Radio 48 Kbps', 'http://uryfs1.york.ac.uk/live-mobile']
        ]
        }

        # Adds radio stations defined above to the dictionary of all stations
        self._stations.update(radio_1)
        self._stations.update(radio_2)
        self._stations.update(radio_3)
        self._stations.update(radio_4)
        self._stations.update(radio_5)
        self._stations.update(radio_5_extra)
        self._stations.update(hereford)
        self._stations.update(york)

    def add(self, stations: dict):
        """Allows for a new station to be added to an instance
        Note anything added will be forgotten in a new stations instance

        Args:
            stations (dict): station as dictionary, using format above {station_name: [connection_type (string), radio_URL]}
        """
        self._stations.update(stations)

    @property
    def get(self):
        """Gets all stations

        Returns:
            dict: returns all stations as a dictionary
        """
        return self._stations
