class Error(Exception):
    def __init__(self, errors, msg=None):
        self.msg = msg or 'Colander validation error'
        self.errors = errors
        super(Error, self).__init__(self.msg)
