#!/usr/bin/env python
import pkg_resources
pkg_resources.require("TurboGears")

import cherrypy
from os.path import *
import sys

from turbogears import toolbox

root = toolbox.Toolbox()
cherrypy.root = root
print "Toolbox Development Mode"
cherrypy.config.update({"global" : {
    "server.socketPort" : 7654,
    "server.environment" : "development",
    "server.logToScreen" : True,
    "autoreload.package" : "turbogears",
    "logDebugInfoFilter.on" : False
    }})

cherrypy.server.start()
