import morepath
from .errors import Error


class App(morepath.App):
    pass


@App.json(model=Error)
def validation_error_default(self, request):
    @request.after
    def adjust_status(response):
        response.status = 422
    return self.errors
