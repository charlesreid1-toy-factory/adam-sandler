class AdamSandlerMovie(object):
    def __init__(self, title):
        self.title = title

class GoodAdamSandlerMovie(AdamSandlerMovie):
    def __init__(self, *args, **kwargs):
        raise NotImplementedError()

class BadAdamSandlerMovie(AdamSandlerMovie):
    pass
