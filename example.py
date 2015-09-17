#!./env/bin/python
import sys
import FrameMonitor
import importlib

if __name__ == "__main__":
    app = FrameMonitor.getApp(sys.argv)

    # point to a config file, this config file has to define a frame and a "reaction"
    # name of the file could be made an input argument...
    loader = importlib.machinery.SourceFileLoader('', "config.py")
    m = loader.load_module()

    # ex seems to be important
    ex = FrameMonitor.FrameMonitor(m.FRAME, m.FUNC)

    # wait with the exit until the app has stopped
    sys.exit(app.exec_())
