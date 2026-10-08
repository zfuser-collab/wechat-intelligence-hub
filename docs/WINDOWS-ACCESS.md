# Windows compatibility notes

This repo is a fork of the upstream WeChat Intelligence Hub and keeps the AGPL-3.0-only license and upstream notice intact.

Windows support is intentionally conservative. The code is still primarily Linux/macOS-oriented because the project ships bash installers and some upstream docs assume Unix-only tooling (for example shell scripts, `chmod`, and macOS notification preview features).

What this repo adds
- Install.cmd: bootstrap script for a Windows x64 Python 3.12 environment.
- SelfTest.cmd: a smoke test that verifies the repo structure and key entrypoints.
- wechat.cmd: small launcher for the `reader` and `hub` subcommands.
- requirements-windows.lock: a minimal Windows dependency file for the compatibility bootstrap.

Current status
- The Windows bootstrap layer is designed to make local testing and validation easier on Windows.
- Real WeChat database access still requires valid local database files, access materials, and user authorization.
- Media extraction and some advanced access paths remain subject to platform-specific validation; do not assume full feature parity with the Unix/macOS setup.

Recommended usage

```cmd
Install.cmd
SelfTest.cmd
wechat.cmd hub home
wechat.cmd reader status --pretty
```

If a dependency is missing, install Python 3.12.x first and rerun the bootstrap scripts. For actual database-backed usage, follow the upstream authorization guidance and only add local access materials that you are legally and technically allowed to use.
