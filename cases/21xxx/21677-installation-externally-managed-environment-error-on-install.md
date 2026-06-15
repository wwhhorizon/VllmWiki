# vllm-project/vllm#21677: [Installation]: Externally Managed Environment error on install

| 字段 | 值 |
| --- | --- |
| Issue | [#21677](https://github.com/vllm-project/vllm/issues/21677) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Externally Managed Environment error on install

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` There is none as your script doesn't support Python 3 ``` OS: Debian 12 Desktop: Wayland Plasma Python Version: Python 3.11.2 error: externally-managed-environment × This environment is externally managed ╰─> To install Python packages system-wide, try apt install python3-xyz, where xyz is the package you are trying to install. If you wish to install a non-Debian-packaged Python package, create a virtual environment using python3 -m venv path/to/venv. Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make sure you have python3-full installed. If you wish to install a non-Debian packaged Python application, it may be easiest to use pipx install xyz, which will manage a virtual environment for you. Make sure you have pipx installed. See /usr/share/doc/python3.11/README.venv for more information. I get that when I follow your instructions: "pip install vllm" ### How you are installing vllm ```sh pip install -vvv vllm ``` error: externally-managed-environment × This environment is externally managed ╰─> To install Python packages system-wide, try apt install python3-xyz, where xyz is the package you ar...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Externally Managed Environment error on install installation;stale ### Your current environment ```text The output of `python collect_env.py` There is none as your script doesn't support Python 3 ``` OS:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ur script doesn't support Python 3 ``` OS: Debian 12 Desktop: Wayland Plasma Python Version: Python 3.11.2 error: externally-managed-environment × This environment is externally managed ╰─> To install Python packages sy...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: installed. See /usr/share/doc/python3.11/README.venv for more information. I get that when I follow your instructions: "pip install vllm" ### How you are installing vllm ```sh pip install -vvv vllm ``` error: externally...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tallation]: Externally Managed Environment error on install installation;stale ### Your current environment ```text The output of `python collect_env.py` There is none as your script doesn't support Python 3 ``` OS: Deb...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
