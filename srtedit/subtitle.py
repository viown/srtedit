from datetime import timedelta
import srt


class Srt:
    def __init__(self, path):
        self.path = path
        with open(path, 'r', encoding='utf-8') as f:
            self.subtitles = list(srt.parse(f.read()))

    def __len__(self):
        return len(self.subtitles)
    
    def slice(self, start_index: int, end_index: int):
        self.subtitles = self.subtitles[start_index:end_index]

    def edit(self, indices: tuple[int, int], new_content: str):
        for i in range(indices[0], indices[1]):
            self.subtitles[i].content = new_content

    def remove(self, indices: tuple[int, int]):
        del self.subtitles[indices[0]:indices[1]]

    def offset(self, indices: tuple[int, int], ms: int):
        for i in range(indices[0], indices[1]):
            offset_value = timedelta(milliseconds=ms)

            self.subtitles[i].start = self.subtitles[i].start + offset_value
            self.subtitles[i].end = self.subtitles[i].end + offset_value

    def count(self):
        i = 0
        for elem in self.subtitles:
            if elem is not None:
                i += 1
        return i

    def output(self):
        return srt.compose([srt for srt in self.subtitles if srt is not None])
