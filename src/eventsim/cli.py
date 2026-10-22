#!/usr/bin/env python3
import click
from rich.console import Console
from .simulator import simulate_mm1

console = Console()

@click.group()
@click.version_option()
def main(): pass

@main.command()
@click.option('--lambda', type=float, default=0.5)
@click.option('--mu', type=float, default=1.0)
@click.option('--time', type=float, default=1000)
def mm1(lambd, mu, time):
    res = simulate_mm1(lambd, mu, time)
    console.print(f"[green]Utilization:[/green] {res['utilization']:.3f}")
    console.print(f"[blue]Avg wait:[/blue] {res['avg_wait']:.3f}")

if __name__ == '__main__': main()
