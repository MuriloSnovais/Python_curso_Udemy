# Abstração
# Log
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self,msg):
        raise NotImplementedError('implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'ERROR: {msg}')
    
    def log_success(self, msg):
        return self._log(f'SUCCESS: {msg}')
    
class LogFileMixin(Log):
    def _log(self,msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print("SALVANDO NO LOG:" , msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
    
class LogPrintMixin(Log):
    def _log(self,msg):
        print(f"{msg} ({self.__class__.__name__})")



if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_success('Bacana')
    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Bacana')
    print(LOG_FILE)

