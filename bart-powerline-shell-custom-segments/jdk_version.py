from powerline_shell.utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        v = os.environ.get("JAVA_HOME")
        n=""
        if v:
            try:
                n = os.path.basename(v)
                n = os.readlink(v).split("-")[0]
            except Exception as e:
                pass
        self.powerline.append(f"𝄢{n} ",
                self.powerline.theme.AWS_PROFILE_FG,
                self.powerline.theme.AWS_PROFILE_BG)
