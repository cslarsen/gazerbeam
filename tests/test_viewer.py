import time

import gazerbeam.ipc
import gazerbeam.process


if __name__ == "__main__":
    print("Starting viewer")
    process = gazerbeam.process.Process
    process.start()

    queue = gazerbeam.ipc.Queue

    try:
        count = 0
        start = time.time()

        while process.is_alive():
            now = time.time()
            if (now - start) >= 1.0:
                # Send every second
                queue.send(count)
                count += 1
                start = now
    except KeyboardInterrupt:
        pass

    print("Closing and joining queue")
    gazerbeam.ipc.Queue.queue.close()

    print("Joining process (may need server to shut down)")
    gazerbeam.process.Process.join()

    print("Done")
