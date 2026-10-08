#!/usr/bin/env python3
"""Smoke test for Windows compatibility bootstrap."""
from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    required = [
        root / "projects" / "rion-wechat-reader" / "rion_wechat_reader.py",
        root / "projects" / "wechat-intelligence-hub" / "wechat_intelligence_hub.py",
        root / "scripts" / "install.sh",
        root / "README.md",
    ]
    missing = [str(p.relative_to(root)) for p in required if not p.exists()]
    if missing:
        for item in missing:
            print(f"Missing required project file: {item}")
        return 1

    print("Windows smoke test passed.")
    print(f"Repo root: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
