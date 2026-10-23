# eventsim

Deterministic single-server (M/M/1) queue simulator with reproducible utilization and wait statistics.

## Problem

Queueing intuition is hard to build from formulas alone: it is unclear how arrival rate, service rate and run length actually move utilization and waiting time. eventsim runs a seeded event simulation you can rerun and compare, without a spreadsheet or a notebook.

## Features

- Event-driven M/M/1 simulation (arrival and service times are exponential)
- Reports server utilization, average wait time and customers served
- Seeded random stream, so identical arguments give identical numbers
- `--lambda`, `--mu` and `--time` are plain CLI flags
- Captured run committed at `results/demo-output.txt`

## Example

```shell
PYTHONPATH=src python3 -m eventsim.cli mm1 --lambda 0.5 --mu 1.0 --time 1000
```

```text
Utilization: 0.470
Avg wait: 1.062
```

A captured run of the same command is committed at `results/demo-output.txt`.

## Architecture

Two modules:

- `src/eventsim/simulator.py` holds the event loop: it tracks the next arrival, the next departure and a FIFO queue, advances time to the earlier event, and accumulates wait time and served count. It returns a dictionary of statistics and depends only on `random`.
- `src/eventsim/cli.py` parses the three flags and prints the statistics with `rich`.

## Requirements

- Python 3.10 or newer
- `click`, `rich`

## Installation

```shell
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

On Windows activate the environment with `.venv/Scripts/activate` instead.

## Quick start

```shell
PYTHONPATH=src python3 -m eventsim.cli mm1 --lambda 0.5 --mu 1.0 --time 1000

# after `pip install -e .`:
eventsim mm1 --lambda 0.8 --mu 1.0 --time 5000
```

## Configuration

No config file. Defaults are `--lambda 0.5`, `--mu 1.0`, `--time 1000`. The random seed is fixed at 42 inside `simulate_mm1`, which keeps runs reproducible.

## Testing

```shell
python3 -m pytest -q
```

Tests run from a clean clone: `pyproject.toml` sets pytest's `pythonpath` to
`src`, so no install step is needed to run them.

## Project structure

```text
eventsim/
|-- src/eventsim/
|   |-- simulator.py      # event loop and statistics
|   `-- cli.py            # click command group
|-- tests/
|   |-- test_sim.py       # simulation invariants
|   `-- test_cli.py       # end-to-end command test
|-- results/              # captured demo output
|-- docs/                 # ARCHITECTURE.md, USAGE.md
`-- pyproject.toml
```

## Limitations

- Single-server FIFO only: no multi-server, priority or balking behaviour.
- Utilization is estimated from completed services divided by run length, so
  it slightly under-reports near the end of a run.
- No warm-up period is discarded, so short runs are biased.
- The seed is fixed, so repeated runs are identical - good for regression
  checks, not for confidence intervals. Pass `seed=` to `simulate_mm1` for
  that.

## Roadmap

- `--seed` flag on the CLI
- M/M/c (multi-server) variant and a utilization-versus-lambda sweep
- Percentile wait-time output and CSV export
- JSON output for plotting

## Security notes

Pure computation: no file access, no network access, no state on disk.

## License

MIT - see [LICENSE](LICENSE).
