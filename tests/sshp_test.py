# flake8: noqa: S603
from __future__ import annotations

import logging
import subprocess
import sys
from pathlib import Path

logger = logging.getLogger(__name__)


def test_help() -> None:
    sshp_bin = Path(sys.executable).parent / "sshp"
    assert sshp_bin.exists(), f"sshp binary not found at {sshp_bin}"
    result = subprocess.run([sshp_bin, "--help"], check=False, capture_output=True, text=True)
    if result.returncode != 0:
        logger.error(result.stderr)
        msg = f"Error running {sshp_bin} --help"
        raise AssertionError(msg)
