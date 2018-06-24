import multiprocessing
import random

import gazerbeam.ipc

import numpy as np

import vispy
import vispy.app
import vispy.color
import vispy.scene


class Canvas(object):
    def __init__(self):
        self.scene = vispy.scene.SceneCanvas(
                        title="Gazerbeam",
                        keys="interactive",
                        show=True,
                        size=(1200, 800),
                        vsync=True,
                        resizable=True)

        self.view = self.scene.central_widget.add_view()
        self.view.camera = 'panzoom'
        self.view.camera.aspect = 1

        self.nodes = np.array([[0,0,0]])
        self.markers = vispy.scene.Markers(
                pos=self.nodes,
                symbol='o',
                parent=self.view.scene)

        self.view.camera.set_range()

        self.received = []
        self.timer = vispy.app.Timer("auto", connect=self._check_queue, start=True)

    #def update(self, event=None):
        #vispy.app.Canvas.update(self, event)

        #self._check_queue()

    def _check_queue(self, event=None):
        obj = gazerbeam.ipc.Queue.receive()

        if obj is not None:
            name = multiprocessing.current_process().name
            self.received.append(obj)
            print("%s: Received object %s (%d objs)" % (name, obj,
                len(self.received)))

            if obj == "STOP":
                if hasattr(self, "timer"):
                    self.timer.stop()
                gazerbeam.ipc.Queue.queue.close()
                gazerbeam.ipc.Queue.queue.join_thread()
                vispy.app.quit()

    def on_draw(self, event):
        # Just flash the screen for now
        pass

    def run(self):
        try:
            vispy.app.run()
        except KeyboardInterrupt:
            vispy.app.quit()


def start():
    canvas = Canvas()
    canvas.run() # blocks
