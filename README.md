# srtedit

A command-line tool for quickly editing subtitle (.srt) files.

## Installation

```
pip install srtedit
```

## Basic Usage

### Offset subtitles in milliseconds

```
srtedit subtitles.srt --offset 1000 -o modified.srt
```

Will add exactly 1 second to all subtitle elements. Conversely:

```
srtedit subtitles.srt --offset -1000 -o modified.srt
```

Will subtract 1 second from all subtitle elements.

### Offset individual subtitle element

Use the `-s/--select` option to select an individual element to offset. Example:

```
srtedit subtitles.srt -s 1 --offset 2000 -o modified.srt
```

Will add 2s to the first subtitle element only.

### View contents of subtitle element

```
srtedit subtitles.srt -s 1 --view
```

Will display the start/end times and the content of the selected element. Omitting the `-s` option will display all subtitle elements in the file.

Note: The output from `--view` is not compatible with the .srt format. You should use the `-o/--output` option when writing any files.

### Remove subtitle element

Use the `-r/--remove` option to remove a selected element.

```
srtedit subtitles.srt -s 1 --remove -o modified.srt
```

### Edit subtitle element

```
srtedit subtitles.srt -s 1 --edit "New text" -o modified.srt
```

### Count number of elements

```
srtedit subtitles.srt --count
```

### Multiple options

You can use multiple options together like this:

```
srtedit subtitles.srt -s 1 --edit "New text" --offset 1000 --view -o modified.srt
```

Will set the text of the first element to "New text" then add 1 second to the start and end times and then display the new values to the terminal and then finally write it to `modified.srt`

### Disclaimer

Note that srtedit will select all subtitle elements by default. Omitting the `-s/--select` option will result in the specified operation (`--edit`/`--remove`/`--offset`) being applied to all elements.

Without specifying an output path, you can use the `--view` flag in conjuction with any of the operations above to see your changes before writing.