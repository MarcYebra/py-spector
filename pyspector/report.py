from rich.console import Console
from rich.table import Table

def print_report(functions):
    console = Console()
    table = Table(title="CodeSage Report")

    table.add_column("Function", style="cyan")
    table.add_column("Line No.", style="green")
    table.add_column("Length", style="yellow")
    table.add_column("Docstring?", style="red")

    for func in functions:
        table.add_row(
            func.name,
            str(func.lineno),
            str(func.length),
            "Yes" if func.has_docstring else "No"
        )

    console.print(table)
