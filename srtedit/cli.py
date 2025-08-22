import os
from srt import SRTParseError
import click
from srtedit.subtitle import Srt
from srtedit.utils import create_range

def error(message: str):
    click.echo(f"{click.style('Error:', fg='red')} {message}")

def warn(message: str):
    click.echo(f"{click.style('Warning:', fg=(255, 191, 0))} {message}")

@click.command()
@click.option('--select', '-s', help="Select a subtitle element", default=None, type=str)
@click.option('--edit', '-e', help="Edit the contents of the selected element(s)")
@click.option('--remove', '-r', is_flag=True, help="Removes the selected element(s)", type=str)
@click.option('--offset', '-m', help="Offset the selected element(s) in milliseconds.", type=int)
@click.option('--count', '-c', is_flag=True, help="Count the number of subtitle elements.")
@click.option('--output', '-o', help="Output path", type=click.Path())
@click.argument('path', type=click.Path())
def srtedit(
    path: str,
    select: str | None,
    edit: str | None,
    remove: str | None,
    offset: int | None,
    count: bool | None,
    output: str | None
):
    if output and os.path.realpath(path) == os.path.realpath(output):
        error("Input and output path cannot be the same")
        return
    if output and os.path.exists(output):
        error(f"A file already exists at {output}")
        return
    if not os.path.exists(path):
        error("Specified path does not exist")
        return

    try:
        srt = Srt(path)
    except SRTParseError:
        error("Parse error. Possibly invalid SRT file.")
        return

    start_index, end_index = create_range(srt, select)

    if start_index < 0 or end_index > len(srt):
        error("Invalid select statement")
        return

    if not edit and not offset and not remove:
        srt.slice(start_index, end_index)

    if edit:
        srt.edit((start_index, end_index), edit)

    if offset:
        srt.offset((start_index, end_index), offset)

    if remove:
        srt.remove((start_index, end_index))

    if count:
        click.echo(srt.count())
        return

    srt_output = srt.output()

    if not output:
        click.echo(srt_output)
    else:
        with open(output, "w", encoding='utf-8') as f:
            f.write(srt_output)
