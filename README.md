# srtedit

A command-line tool for quickly editing subtitle (.srt) files.

## Installation

```
pip install srtedit
```

## Basic Usage

### Offset subtitles in milliseconds

```
srtedit subtitles.srt --offset 1000
```

Will add exactly 1 second to all subtitle elements. Conversely:

```
srtedit subtitles.srt --offset -1000
```

Will subtract 1 second from all subtitle elements.

The modified subtitles will be printed to stdout. Use `-o` to specify an output file:

```
srtedit subtitles.srt --offset 500 -o new.srt
```

### Selecting

The `-s/--select` option allows you to select a single or range of subtitle elements to modify. This can work alongside other options such as `--remove`, `--edit`, and `--offset`.

On its own, it can be used to select a portion of the subtitles:

```bash
srtedit subtitles.srt -s 1:10   # Grab the first 10 elements 
```

Single element:
```bash
srtedit subtitles.srt -s 4  # Grab the 4th element
```

### Remove subtitle element

Use the `-r/--remove` option to remove a selected element.

```
srtedit subtitles.srt -s 1 --remove
```

### Edit subtitle element

```
srtedit subtitles.srt -s 1 --edit "New text"
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
