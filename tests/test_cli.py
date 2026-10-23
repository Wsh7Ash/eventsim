from click.testing import CliRunner
from eventsim.cli import main


def test_mm1_command_runs():
    res = CliRunner().invoke(
        main, ["mm1", "--lambda", "0.5", "--mu", "1.0", "--time", "200"]
    )
    assert res.exit_code == 0, res.output
    assert "Utilization" in res.output
    assert "Avg wait" in res.output
