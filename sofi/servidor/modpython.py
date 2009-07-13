mport os
import sys

from os.path import abspath, dirname, join
from site import addsitedir

from django.core.handlers.modpython import ModPythonHandler

PROJECT_ROOT = abspath(join(dirname(__file__), "../"))

class SofiModPythonHandler(ModPythonHandler):
    def __call__(self, req):
        path = addsitedir(join(PROJECT_ROOT, "apps"), set())
        if path:
            sys.path = list(path) + sys.path

        return super(SofiModPythonHandler, self).__call__(req)

def handler(req):
    # mod_python hooks into this function.
    return SofiModPythonHandler()(req)

