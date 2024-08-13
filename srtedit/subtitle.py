from datetime import timedelta
import srt

class Srt:
    def __init__(self, path):
        with open(path, "r") as f:
            self.subtitles = list(srt.parse(f.read()))

    def __len__(self):
        return len(self.subtitles)

    def view(self, index):
        s = f"{index}\n"
        s += f"{self.subtitles[index-1].start.total_seconds()}s --> {self.subtitles[index-1].end.total_seconds()}s\n"
        s += self.subtitles[index-1].content + '\n'

        return s
    
    def edit(self, index, new_content):
        self.subtitles[index-1].content = new_content

    def remove(self, index):
        self.subtitles[index-1] = None

    def offset(self, index, ms):
        offset_value = timedelta(milliseconds=ms)

        self.subtitles[index-1].start = self.subtitles[index-1].start + offset_value
        self.subtitles[index-1].end = self.subtitles[index-1].end + offset_value

    def count(self):
        i = 0
        for elem in self.subtitles:
            if elem is not None:
                i += 1
        return i

    def output(self):
        return srt.compose([srt for srt in self.subtitles if srt is not None])
    