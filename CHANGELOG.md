# Changelog

Notable changes to this project.

## 0.1.0 - 2026-10-23

- First release.
- Fixed the `mm1` option binding: `--lambda` reached the callback as an
  unexpected keyword and the only command crashed on every invocation.
- Added `pythonpath = ["src"]` so tests run without installing.
- Added a CLI regression test covering the full `mm1` invocation.
