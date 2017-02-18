from functools import partial
from colander import (
    Schema,
    Invalid
)
from .errors import Error


def load(schema, request):
    try:
        return schema.deserialize(request.json)
    except Invalid as e:
        raise Error(e.asdict(), e.msg)


def loader(schema):
    """Create a load function based on schema instance.

    :param schema: a Colander schema instance. You
      can also pass in a Colander schema class.

    You can plug this ``load`` function into a json view.

    Returns a ``load`` function that takes a request JSON body
    and uses the schema to deserialize it. This function raises
    :class:`more.colander.ValidationError` if it cannot do
    the deserialization.
    """
    if not isinstance(schema, Schema):
        # try to instantiate the schema class
        schema = schema()
    return partial(load, schema)


def context_loader(schema_factory, context_factory):
    """Create a load function based on schema class and context.

    :param schema_factory: a Colander schema factory, typically
      the schema class itself.
    :param context_factory: a schema context factory. This is a function that
      gets the request as an argument and returns a context dictionary that can
      then be used within the Colander schema.

    Returns a ``load`` function that takes the request JSON body
    and uses the schema created ``schema_factory`` to deserialize it.
    This function raises a :class:`more.colander.ValidationError``
    if it cannot do the deserialization.
    """
    def load_with_context(request):
        context = context_factory(request)
        schema = schema_factory().bind(**context)
        return load(schema, request)
    return load_with_context


def request_context_factory(request):
    return {'request': request}


request_loader = partial(
    context_loader,
    context_factory=request_context_factory
)
request_loader.__doc__ = """\
Create a load function based on schema class. Put request in context.

:param schema_factory: a Colander schema factory, typically
  the schema class itself.

The context dict that can be used in the Colander schema contains
the request as an entry.

Returns a ``load`` function that takes the request JSON body
and uses the schema created ``schema_factory`` to deserialize it.
This function raises a :class:`more.colander.ValidationError``
if it cannot do the deserialization.
"""
