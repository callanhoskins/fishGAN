activate_this = '/home/ubuntu/fishGAN/venv/bin/activate_this.py'
with open(activate_this) as f:
	exec(f.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/html/fishGAN/')
from fishGAN import app as application
