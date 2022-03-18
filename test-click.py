import click
import sys

@click.group()
def cli():
    """minimal click test example"""

@cli.command()
@click.argument(
    "a",
    type=click.File("r", encoding="UTF-8"),
    required=False,
    default="-",
)
@click.argument(
    "b",
    type=click.File("w", encoding="UTF-8"),
    required=False,
    default="-",
)
def delme(a, b):
    print(type(a), file=sys.stderr)
    a = map(str.strip, a)
    for l in a:
        print(l, file=b)

if __name__ == "__main__":
    cli()
