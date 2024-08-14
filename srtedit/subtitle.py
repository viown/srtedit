from datetime import timedelta
import srt


class Srt:
    def __init__(self, path):
        self.path = path
        with open(path, "r") as f:
            self.subtitles = list(srt.parse(f.read()))

    def __len__(self):
        return len(self.subtitles)

    def view(self, index):
        s = f"{index+1}\n"
        s += f"{self.subtitles[index].start.total_seconds()}s --> {self.subtitles[index].end.total_seconds()}s\n"
        s += self.subtitles[index].content + '\n'

        return s

    def edit(self, index, new_content):
        self.subtitles[index].content = new_content

    def remove(self, index):
        self.subtitles[index] = None

    def offset(self, index, ms):
        offset_value = timedelta(milliseconds=ms)

        self.subtitles[index].start = self.subtitles[index].start + offset_value
        self.subtitles[index].end = self.subtitles[index].end + offset_value

    def count(self):
        i = 0
        for elem in self.subtitles:
            if elem is not None:
                i += 1
        return i

    def output(self):
        return srt.compose([srt for srt in self.subtitles if srt is not None])
