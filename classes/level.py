class Level:
    def __init__(self, level, exp):
        self.level = {
            "level": level,
            "exp": exp
        }

    def __getitem__(self, key):
        return self.level[key]

    def __setitem__(self, key, value):
        return

    def get_exp(self):
        return self.__getitem__("exp")
