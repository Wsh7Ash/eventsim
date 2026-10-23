# Architecture

## Modules

- `eventsim.simulator` - `simulate_mm1(lambd, mu, sim_time, seed)` runs the
  event loop and returns `utilization`, `avg_wait` and `served`.
- `eventsim.cli` - `click` group exposing `mm1`.

## Data flow

CLI flags -> `simulate_mm1` event loop (arrival/departure events over simulated time) -> statistics dictionary -> `rich` console output.

## Design decisions

- The simulator is a pure function with an explicit seed, so tests can
  assert stable numbers and users can reproduce reported results.
- Time advances to the next event rather than in fixed steps, so results do
  not depend on a step size.
- The CLI only formats; all logic lives in `simulator.py`.

## Testing strategy

- Unit tests cover the core logic (the event loop and the statistics it reports).
- CLI tests use `click.testing.CliRunner`, so command wiring is exercised
  without a real terminal or subprocess.
- `pyproject.toml` sets `pythonpath = ["src"]`, so `python3 -m pytest -q` works
  from a fresh clone.
