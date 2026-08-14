from powerline_shell.utils import BasicSegment
from subprocess import check_output
from os.path import basename, dirname


class Segment(BasicSegment):
    def add_to_powerline(self):

        s=check_output(["which", "python"]).decode('utf8').strip()
        env = basename(dirname(dirname(dirname(s))))
        if env=='':
            return
        bg = self.powerline.theme.VIRTUAL_ENV_BG
        fg = self.powerline.theme.VIRTUAL_ENV_FG
        self.powerline.append(" " + env + " ", fg, bg)
