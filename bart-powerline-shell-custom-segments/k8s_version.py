from powerline_shell.utils import BasicSegment
import os, re, subprocess, yaml
from os.path import *


class Segment(BasicSegment):
    def add_to_powerline(self):
        return
        try:
            with open(expanduser("~/.config/gcloud/active_config")) as _f:
                active = _f.read()
            self.powerline.append(f"GKE {active}", 57, 254)
        except Exception as e:
                self.powerline.append(str(e), 57, 131)

        default_path= abspath(expanduser("~/.kube/config"))
        v = abspath(expanduser(os.environ.get("KUBECONFIG", default_path)))
        try:
            if v != default_path:
                self.powerline.append(f"CTX {basename(v).replace('.yaml','')}", 57, 244)

            with open(v) as _f:
                config = yaml.load(_f, Loader=yaml.FullLoader)

                ctx = config['current-context'].replace('yaml','')
                x = [c for c in config['contexts'] if c['name'] == config['current-context']][0]
                self.powerline.append(f"☯{ctx}", 57, 249)
                namespace = x['context']['namespace']
                self.powerline.append(f"∇{namespace}", 57, 247)
        except Exception as e:
                self.powerline.append(str(e), self.powerline.theme.USERNAME_FG, self.powerline.theme.USERNAME_ROOT_BG)

