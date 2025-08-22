from srtedit.subtitle import Srt

def create_range(srt: Srt, select: str | None) -> tuple[int, int]:
    start_index, end_index = 0, 0
    if select is None:
        start_index = 0
        end_index = len(srt)
    elif ':' in select:
        args = select.split(':')
        start_index = int(args[0]) - 1
        end_index = int(args[1])
    else:
        element = int(select) - 1
        start_index, end_index = element, element + 1

    return (start_index, end_index)
