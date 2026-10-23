# Usage

## Commands

| Command | Purpose |
|---|---|
| `eventsim mm1 --lambda L --mu M --time T` | Run an M/M/1 simulation for `T` time units |
| `eventsim --version` | Print the installed version |

`--lambda` is the arrival rate and `--mu` the service rate; utilization is
`lambda / mu` for a stable M/M/1 queue.

## Examples

```shell
eventsim mm1 --lambda 0.5 --mu 1.0 --time 1000
eventsim mm1 --lambda 0.9 --mu 1.0 --time 10000
```

## Exit codes

- `0` - the command completed successfully
- `1` - click reported a usage error (missing or invalid option)
- `2` - click could not parse the command line

## Output

Output is rendered with `rich` and written to stdout, so it can be captured or
piped. Example runs are committed under `results/`.
