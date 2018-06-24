import multiprocessing


class Process(object):
    process = None

    @staticmethod
    def start():
        """Starts viewer in subprocess.

        Communicate using ``gazerbeam.ipc.Queue.send``.
        """
        Process.process = multiprocessing.Process(target=Process._start_viewer)
        Process.process.start()

    @staticmethod
    def join():
        Process.process.join()

    @staticmethod
    def _start_viewer():
        # This runs in subprocess. Start viewer only there, because vispy needs
        # to initialize global stuff in a main thread.
        import gazerbeam.viewer
        gazerbeam.viewer.start()

    @staticmethod
    def is_alive():
        return Process.process.is_alive()
