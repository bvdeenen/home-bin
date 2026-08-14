from powerline_shell.utils import BasicSegment
import re, subprocess
from os.path import *

cmd = ["/usr/bin/env", "python3", "-c" "import sys; print(sys.executable); print(sys.version)"]

class Segment(BasicSegment):
    def add_to_powerline(self):
        info = subprocess.check_output(cmd,
                stderr=subprocess.STDOUT).decode('utf-8').split('\n')
        m = re.search(r'\d\.\d+\.\d+', info[1])
        b=None
        try:
            b=basename(dirname(dirname(info[0])))
            if b==".local":
                b=None
        except:
            pass

        s = f"{m.group(0)}"
        if b:
            self.powerline.append(s, 7, 240)
        else:
            self.powerline.append(s, 7, 236)
