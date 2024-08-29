"""Command Line Interface."""
from .task2report import runParser
import typer
import subprocess

app = typer.Typer()


@app.command()
def run() -> None:
    """Run command."""
    print("Hello World")

@app.command()
def mkreport(infile:str,outfile:str,genpdf:bool=True) -> None:
    """Generate reports from taskwiki"""
    runParser(infile,outfile)
    if genpdf:
        cmd="pandoc --toc --from=markdown+lists_without_preceding_blankline -F pandoc-imagine -o report.pdf -s".split(' ')
        cmd.append(outfile)
        subprocess.run(cmd)



@app.callback(no_args_is_help=True)
def main() -> None:
    """CLI for task2report Parser Library."""
typer_click_object = typer.main.get_command(app)
