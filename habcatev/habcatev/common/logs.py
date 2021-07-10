import os
import logging

class Logs(object):
    def __init__(self):
        super(Logs, self).__init__()
        self.conffile=''
        self.log = logging
        self._getConfigFile()
        self.log.config.fileConfig('logging.conf')

    def _getConfigFile(self):
        osenv = os.environ['HABCATEV_LOGCONFIG']
        if osenv and os.path.isfile(osenv):
            self.conffile = osenv
    