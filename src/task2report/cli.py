"""Command Line Interface."""
from .task2report import runParser

import subprocess

import copier
import typer

app = typer.Typer()


@app.command()
def run() -> None:
    """Run command."""
    print("Hello World")

@app.command()
def task2report(filename:str) -> None:
    """"""
    with open(filename,'r') as file:
        runParser(file)


@app.callback(no_args_is_help=True)
def main() -> None:
    """CLI for task2report Parser Library."""
typer_click_object = typer.main.get_command(app)
