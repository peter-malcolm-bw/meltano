"""Reusable CLI `--environment` option."""

import click

environment_option = click.option(
    "--environment",
    envvar="MELTANO_ENV",
    help="Meltano environment",
)
