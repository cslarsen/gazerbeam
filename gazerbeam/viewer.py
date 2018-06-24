import multiprocessing
import queue
import time

QUEUE = None

class Process(object):
    process = None

    @staticmethod
    def _run_canvas():
        name = multiprocessing.current_process().name
        print("Booting canvas in process %s" % name)

        try:
            print("Starting canvas in %s" % name)
            foo()
            print("Canvas done... in %s" % name)
        except Exception as e:
            print("Process %s error: %s" % (name, e))

    @staticmethod
    def start():
        global QUEUE
        QUEUE = multiprocessing.Queue()
        name = multiprocessing.current_process().name
        print("Booting subprocess from %s" % name)
        Process.process = multiprocessing.Process(target=Process._run_canvas)
        Process.process.start()
        print("Subprocess away")

    @staticmethod
    def send(obj):
        print("Sending %s" % obj)
        try:
            QUEUE.put(obj)
        except queue.Full:
            print("Queue is full")
            pass

    @staticmethod
    def join():
        print("Waiting for subprocess to stop")
        Process.process.join()
        print("Subprocess stopped")

def foo():
    # This is a bit lame, but vispy has global state (well, so do we, duh!), so
    # only import it in the subprocess. Also, all this stuff is done solely
    # because GUI stuff always needs to run in the main thread, which won't
    # work for us. So we'll just spawn a real subprocess and use IPC to
    # communicate (i.e., a multiprocessing queue). Can clean up this code
    # later.

    import vispy
    import vispy.app
    import vispy.gloo

    class Canvas(vispy.app.Canvas):
        def __init__(self):
            vispy.app.Canvas.__init__(self,
                    title="Gazerbeam",
                    keys="interactive",
                    size=(1200, 800),
                    vsync=True,
                    resizable=True)
            vispy.gloo.set_clear_color((0, 36.0/255.0, 51.0/255.0))

            self.timer = vispy.app.Timer("auto", connect=self.update, start=True)
            self.show()

        def update(self, event=None):
            vispy.app.Canvas.update(self, event)
            self.check_queue()

        def on_draw(self, event):
            import random
            vispy.gloo.set_clear_color((
                random.randint(0,255)/255.0,
                random.randint(0,255)/255.0,
                random.randint(0,255)/255.0,))
            vispy.gloo.clear(color=True)

        def check_queue(self):
            try:
                self.receive(QUEUE.get_nowait())
            except queue.Empty:
                pass

        def run(self):
            vispy.app.run()

        def receive(self, obj):
            print("Canvas received object %s" % obj)

    name = multiprocessing.current_process().name
    print("canvas = Canvas() in %s" % name)
    global global_canvas
    global_canvas = Canvas()
    print("canvas.run() in %s" % name)
    global_canvas.run()
    print("canvas.run() done in %s" % name)


if __name__ == "__main__":
    Process.start()
    count = 0
    while Process.process.is_alive():
        print("waiting ...")
        time.sleep(1)
        count += 1
        Process.send(count)
    Process.join()
    print("Exiting...")
