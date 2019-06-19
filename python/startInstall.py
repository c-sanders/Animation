# from os.path import dirname, abspath, join
import sys

# THIS_DIR = dirname(__file__)
# CODE_DIR = abspath(join(THIS_DIR, "..", "python"))
# sys.path.append(CODE_DIR)

import ConfigureScriptAgent


configureScriptAgent = ConfigureScriptAgent.ConfigureScriptAgent()

configureScriptAgent.run()
