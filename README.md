### Windows 兼容说明（实验性）

本仓库已补齐一层最小的 Windows 入口，用于在 Windows x64 + Python 3.12 环境中做本地自检和启动，不包含真实聊天、数据库或密钥。

```cmd
Install.cmd
SelfTest.cmd
wechat.cmd hub home
wechat.cmd reader status --pretty
```

这层兼容性改动的目标不是让所有功能在 Windows 上完全等价于 macOS/Linux，而是让项目在 Windows 上更容易完成：

- Python 3.12 检查与 bootstrapping
- `.runtime` 目录和 Windows 依赖锁文件
- `Install.cmd` / `SelfTest.cmd` / `wechat.cmd` 统一入口
- 对 macOS-only 功能（Notification Center、AppleScript、某些 shell 细节）的显式降级说明

真实微信数据库读取仍需要本地授权材料、合法使用范围、密钥和用户确认；不要把未授权的数据库或聊天内容放入仓库。Windows 版应保留 AGPL-3.0-only、NOTICE 和上游署名，并遵循原项目的隐私边界。

详细说明见 [`docs/WINDOWS-ACCESS.md`](docs/WINDOWS-ACCESS.md)。
