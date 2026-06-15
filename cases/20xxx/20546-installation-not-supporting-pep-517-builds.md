# vllm-project/vllm#20546: [Installation]: not supporting PEP 517 builds

| 字段 | 值 |
| --- | --- |
| Issue | [#20546](https://github.com/vllm-project/vllm/issues/20546) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: not supporting PEP 517 builds

### Issue 正文摘录

### Your current environment OS: macOS Sequoia, Version 15.5 Chip: Apple M2 python --version: 3.13.3 pipx --version: 1.7.1 poetry --version: (version 2.1.3) ### How you are installing vllm When I try to execute the installing command, there is a error about `not supporting PEP 517 builds`. First, install all the dependencies: ```sh % sudo poetry install -v The "poetry.dev-dependencies" section is deprecated and will be removed in a future version. Use "poetry.group.dev.dependencies" instead. Found: /Users/mac/.pyenv/versions/3.13.3/bin/python Found: /Users/mac/.pyenv/versions/3.13.3/bin/python Creating virtualenv aiseo in /Users/mac/Projects/solvely-seo/.venv Using virtualenv: /Users/mac/Projects/solvely-seo/.venv Checking keyring availability: Available Installing dependencies from lock file Finding the necessary packages for the current system Package operations: 93 installs, 0 updates, 0 removals - Installing attrs (23.2.0) - Installing rpds-py (0.18.0) - Installing six (1.16.0) - Installing vine (5.1.0) - Installing wcwidth (0.2.13) - Installing python-dateutil (2.9.0.post0) - Installing asgiref (3.8.1) - Installing click (8.1.7) - Installing urllib3 (2.2.1) - Installing promp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: not supporting PEP 517 builds installation ### Your current environment OS: macOS Sequoia, Version 15.5 Chip: Apple M2 python --version: 3.13.3 pipx --version: 1.7.1 poetry --version: (version 2.1.3) ###
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Installing numpy (1.26.4): Failed PEP517 build of a dependency failed Backend subprocess exited when trying to invoke build_wheel | Command '['/tmp/tmpjasr_5y8/.venv/bin/python', '/Users/mac/.local/pipx/venvs/poetry/lib...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tallation ### Your current environment OS: macOS Sequoia, Version 15.5 Chip: Apple M2 python --version: 3.13.3 pipx --version: 1.7.1 poetry --version: (version 2.1.3) ### How you are installing vllm When I try to execut...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: am python found: YES (/tmp/tmpjasr_5y8/.venv/bin/python) | Found pkg-config: /opt/homebrew/bin/pkg-config (2.5.1) | Run-time dependency python found: YES 3.13 | Has header "Python.h" with dependency python-3.13: YES | C...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: g billiard (4.2.0) - Installing ptyprocess (0.7.0) - Installing pure-eval (0.2.2) - Installing pyasn1 (0.6.0) - Installing pycparser (2.22) - Installing soupsieve (2.5) - Installing traitlets (5.14.3) - Installing tzdat...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
