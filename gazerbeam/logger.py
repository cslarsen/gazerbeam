import time
import traceback

class Logger(object):
    store = []

    @staticmethod
    def stamp(cutpoint, args, kw, retval):
        Logger.store.append((
            time.time(),
            time.clock(),
            cutpoint,
            traceback.extract_stack(),
            args,
            kw,
            retval))
