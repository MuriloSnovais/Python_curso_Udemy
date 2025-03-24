# from log import LogFileMixin,LogPrintMixin
# lp = LogPrintMixin()
# lp.log_error('Qualquer coisa')
# lp.log_success('Bacana')
# lf = LogFileMixin()
# lf.log_error('Qualquer coisa')
# lf.log_success('Bacana')
from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('Iphone')

galaxy_s.ligar()
iphone.desligar()

