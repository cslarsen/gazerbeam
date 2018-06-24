import gazerbeam
import aspectlib


@aspectlib.Aspect(bind=True)
def _trace_call(cutpoint, *args, **kw):
    gazerbeam.stamp(cutpoint, args, kw, None)
    retval = yield aspectlib.Proceed
    gazerbeam.stamp(cutpoint, args, kw, retval)
    yield aspectlib.Return(retval)


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
