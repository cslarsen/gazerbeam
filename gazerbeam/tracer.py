import aspectlib
import vispy

@aspectlib.Aspect(bind=True)
def _trace_call(cutpoint, *args, **kw):
    name = cutpoint.__name__
    print("-- %s args=%r kw=%r" % (name, args, kw))
    result = yield aspectlib.Proceed
    print("-- %s args=%r kw=%r ==> %r" % (name, args, kw, result))
    yield aspectlib.Return(result)


def tracer(what=None):
    """
    Decorator that traces all function calls in realtime.

    Args:
        what: Which function, class, module to trace. Pass a tuple to specify
              several.
    """
    def decorator(function):
        def wrap(*args, **kw):
            target = what if what is not None else function
            with aspectlib.weave(target, _trace_call):
                return function(*args, **kw)
        return wrap

    return decorator
