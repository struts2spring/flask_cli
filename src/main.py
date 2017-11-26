

import sys

import click
from . import __version__

def get_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    message = 'Flask CLI %(version)s\nPython %(python_version)s'
    click.echo(message % {
        'version': __version__,
        'python_version': sys.version,
    }, color=ctx.color)
    ctx.exit()

@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--version', help='Show the flask cli version', expose_value=False, callback=get_version, is_flag=True, is_eager=True)
def cli(verbose):
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello World")






if __name__ == '__main__':

    print('hi')
