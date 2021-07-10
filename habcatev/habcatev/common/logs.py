import os
import logging
import logging.config

class Logs(object):
    def __init__(self):
        super(Logs, self).__init__()
        self.conffile=''
        self._getConfigFile()
        logging.config.fileConfig('logging.conf')
        self.logger = logging.getLogger('habcatLogger')

    def _getConfigFile(self):
        try:
            osenv = os.environ['HABCATEV_LOGCONFIG']
            if osenv and os.path.isfile(osenv):
                self.conffile = osenv
            print(osenv)
        except Exception as e:
            pass
    