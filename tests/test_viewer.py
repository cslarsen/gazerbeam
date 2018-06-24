import time

import gazerbeam
import gazerbeam.ipc
import gazerbeam.process


if __name__ == "__main__":
    print("Starting viewer")
    gazerbeam.start_viewer()

    queue = gazerbeam.ipc.Queue

    count = 0
    start = time.time()

    try:
        while gazerbeam.process.Process.is_alive():
            now = time.time()
            if (now - start) >= 1.0:
                # Send every second
                queue.send(count)
                count += 1
                start = now
            else:
                time.sleep(0.01)

            #if count >= 5:
                #gazerbeam.stop_viewer()
                #break
    except KeyboardInterrupt:
        queue.send("STOP")
        # The STOP signal is never handled, we just kill it off here.
        # Problem, as always, I believe, is that the subprocess also attempts
        # to handle the keyboardinterrupt. Perhaps we could mask the signal or
        # something, but Python's handling of keyboardinterrupt is really
        # weird. So just kill that process right away, and do this better later
        # on. When we kill it, it doesn't have a chance (most of the time) to
        # even throw any exceptions because of the bad behavior it gets in.
        gazerbeam.process.Process.process.terminate()
        gazerbeam.process.Process.process.join()

    print("Done")
