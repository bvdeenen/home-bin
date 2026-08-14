from powerline_shell.utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        mesg = os.environ.get("DIRENV_MESG")
        if mesg:
            self.powerline.append(f" ⊂{mesg}⊃ ", 16, 46)
        else:
            p = os.environ.get("DIRENV_DIR")
            if p:
                self.powerline.append('Δ', 16, 46)

