import time
import traceback

import gazerbeam.ipc

class Logger(object):
    store = []

    @staticmethod
    def stamp(cutpoint, args, kw, retval):
        obj = (
            time.time(),
            time.clock(),
            cutpoint,
            traceback.extract_stack(),
            args,
            kw,
            retval,
        )

        Logger.store.append(obj) # Perhaps no need to store here?
        gazerbeam.ipc.Queue.send(obj)
