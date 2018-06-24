import multiprocessing
import random

import gazerbeam.ipc

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

        self.received = []
        self.timer = vispy.app.Timer("auto", connect=self.update, start=True)
        self.show()

    def update(self, event=None):
        vispy.app.Canvas.update(self, event)

        self._check_queue()

    def _check_queue(self):
        obj = gazerbeam.ipc.Queue.receive()

        if obj is not None:
            name = multiprocessing.current_process().name
            self.received.append(obj)
            print("%s: Received object %s (%d objs)" % (name, obj,
                len(self.received)))

    def on_draw(self, event):
        # Just flash the screen for now
        vispy.gloo.set_clear_color((
            random.randint(0,255)/255.0,
            random.randint(0,255)/255.0,
            random.randint(0,255)/255.0,))
        vispy.gloo.clear(color=True)

    def run(self):
        vispy.app.run()


def start():
    canvas = Canvas()
    canvas.run() # blocks
