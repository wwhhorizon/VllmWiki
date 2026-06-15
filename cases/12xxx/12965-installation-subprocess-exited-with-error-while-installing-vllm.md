# vllm-project/vllm#12965: [Installation]: subprocess-exited-with-error while installing vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#12965](https://github.com/vllm-project/vllm/issues/12965) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: subprocess-exited-with-error while installing vllm

### Issue 正文摘录

### Your current environment while doing pip install vllm on vscode running on windows machine. Getting below error for pytorch specific version installation. ``` Collecting vllm Using cached vllm-0.7.2.tar.gz (5.4 MB) Installing build dependencies ... error error: subprocess-exited-with-error × pip subprocess to install build dependencies did not run successfully. │ exit code: 1 ╰─> [12 lines of output] Collecting cmake>=3.26 Using cached cmake-3.31.4-py3-none-win_amd64.whl.metadata (6.5 kB) Collecting ninja Using cached ninja-1.11.1.3-py3-none-win_amd64.whl.metadata (5.3 kB) Collecting packaging Using cached packaging-24.2-py3-none-any.whl.metadata (3.2 kB) Collecting setuptools>=61 Using cached setuptools-75.8.0-py3-none-any.whl.metadata (6.7 kB) Collecting setuptools-scm>=8.0 Using cached setuptools_scm-8.1.0-py3-none-any.whl.metadata (6.6 kB) ERROR: Could not find a version that satisfies the requirement torch==2.5.1 (from versions: 2.6.0) ERROR: No matching distribution found for torch==2.5.1 [end of output] note: This error originates from a subprocess, and is likely not a problem with pip. [notice] A new release of pip is available: 24.2 -> 25.0 [notice] To update, run: py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: subprocess-exited-with-error while installing vllm installation;stale ### Your current environment while doing pip install vllm on vscode running on windows machine. Getting below error for pytorch specif
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ing cmake>=3.26 Using cached cmake-3.31.4-py3-none-win_amd64.whl.metadata (6.5 kB) Collecting ninja Using cached ninja-1.11.1.3-py3-none-win_amd64.whl.metadata (5.3 kB) Collecting packaging Using cached packaging-24.2-p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lation]: subprocess-exited-with-error while installing vllm installation;stale ### Your current environment while doing pip install vllm on vscode running on windows machine. Getting below error for pytorch specific ver...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
