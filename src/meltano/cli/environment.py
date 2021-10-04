"""Reusable CLI `--environment` option."""

import click

environment_option = click.option(
    "--environment",
    "environment_name",
    envvar="MELTANO_ENV",
    help="Meltano environment",
)
