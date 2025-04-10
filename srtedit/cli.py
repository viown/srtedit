import os
from srt import SRTParseError
import click
from srtedit.subtitle import Srt


def error(message):
    click.echo(f"{click.style('Error:', fg='red')} {message}")


def warn(message):
    click.echo(f"{click.style('Warning:', fg=(255, 191, 0))} {message}")


@click.command()
@click.option('--select', '-s', help="Select a subtitle element", default=None, type=int)
@click.option('--view', '-v', is_flag=True, help="View the contents of the selected element(s)")
@click.option('--edit', '-e', help="Edit the contents of the selected element(s)")
@click.option('--remove', '-r', is_flag=True, help="Removes the selected element(s)")
@click.option('--offset', '-m', help="Offset the selected element(s) in milliseconds.", type=int)
@click.option('--count', '-c', is_flag=True, help="Count the number of subtitle elements.")
@click.option('--output', '-o', help="Output path", type=click.Path())
@click.argument('path', type=click.Path())
def srtedit(path, select, view, edit, remove, offset, count, output):
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

    selected_elements = []

    if select is None:
        selected_elements = list(range(0, len(srt)))
    else:
        element = int(select) - 1
        selected_elements.append(element)

        if element > len(srt) or element < 0:
            error("Selected value goes beyond the available subtitle elements")
            return

    for element in selected_elements:
        if edit:
            srt.edit(element, edit)
        if offset:
            srt.offset(element, offset)
        if remove:
            srt.remove(element)
        if view:
            if srt.subtitles[element-1] is None:
                warn(f"Attempting to view deleted element ({element})")
            else:
                click.echo(srt.view(element))

    if count:
        click.echo(srt.count())

    if output:
        with open(output, "w") as f:
            f.write(srt.output())
