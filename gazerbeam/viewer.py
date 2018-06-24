import vispy
import vispy.app
import vispy.gloo


class Canvas(vispy.app.Canvas):
    def __init__(self):
        vispy.app.Canvas.__init__(self,
                title="Gazerbeam",
                keys="interactive",
                size=(1200, 800))
        vispy.gloo.set_clear_color((0, 36.0/255.0, 51.0/255.0))
        self.show()

    def on_draw(selv, event):
        vispy.gloo.clear(color=True)

    def run(self):
        vispy.app.run()


if __name__ == "__main__":
    # Oops, this needs to run in the main thread. The only solution to make
    # this possible is to start a separate process and do IPC.
    canvas = Canvas()
    canvas.run()
