#!/usr/bin/env python3
"""Windows bootstrap and compatibility checks for the repo."""
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def ensure_python_version() -> None:
    if sys.version_info[:2] < (3, 12):
        raise SystemExit("Windows support requires Python 3.12 or newer.")


def ensure_runtime_dir(root: Path) -> Path:
    runtime = root / ".runtime"
    runtime.mkdir(exist_ok=True)
    return runtime


def install_lockfile(root: Path) -> None:
    lockfile = root / "requirements-windows.lock"
    if not lockfile.exists():
        lockfile.write_text(
            "# Windows compatibility requirements\n"
            "pytest>=8.0,<9\n"
            "pyyaml>=6.0\n"
            "requests>=2.31\n"
            "beautifulsoup4>=4.12,<5\n"
            "jinja2>=3.1,<4\n"
            "pandas>=2.2,<3\n",
            encoding="utf-8",
        )


def maybe_install_requirements(root: Path, skip_pip: bool) -> None:
    if skip_pip:
        return
    lockfile = root / "requirements-windows.lock"
    if not lockfile.exists():
        return
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", str(lockfile)],
        cwd=str(root),
    )


def write_install_state(runtime: Path) -> None:
    state = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        "platform": sys.platform,
        "mode": "windows-compatibility-bootstrap",
    }
    (runtime / "windows-install.json").write_text(json.dumps(state, indent=2), encoding="utf-8")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    ensure_python_version()
    install_lockfile(root)
    runtime = ensure_runtime_dir(root)
    maybe_install_requirements(root, skip_pip="--skip-pip" in sys.argv)
    write_install_state(runtime)
    print(f"Windows bootstrap complete for {root}")
    print("Python:", sys.version)
    print("Runtime directory:", runtime)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
