class Station:
    def __init__(self, station_id, name, url):
        self.station = {
            "station_id": station_id,
            "name": name,
            "url": url
        }

    def __getitem__(self, item):
        return self.station[item]

    def get_station_id(self):
        return self.__getitem__("station")

    def get_name(self):
        return self.__getitem__("name")

    def get_url(self):
        return self.__getitem__("url")
