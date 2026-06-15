# vllm-project/vllm#13692: [Installation]: vLLM wheel names are broken in recent versions

| 字段 | 值 |
| --- | --- |
| Issue | [#13692](https://github.com/vllm-project/vllm/issues/13692) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: vLLM wheel names are broken in recent versions

### Issue 正文摘录

### How you are installing vllm ```sh export VLLM_VERSION=0.7.0 export PYTHON_VERSION=38 pip install --force-reinstall https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu118-cp${PYTHON_VERSION}-cp${PYTHON_VERSION}-manylinux1_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu118 ``` Results in: ERROR: HTTP error 404 while getting https://github.com/vllm-project/vllm/releases/download/v0.7.0/vllm-0.7.0+cu118-cp38-cp38-manylinux1_x86_64.whl It works fine if I change VLLM_VERSION to 0.6.1.post1 but I need the new version ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: vLLM wheel names are broken in recent versions installation;stale ### How you are installing vllm ```sh export VLLM_VERSION=0.7.0 export PYTHON_VERSION=38 pip install --force-reinstall https://github.com/
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ion ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: stallation]: vLLM wheel names are broken in recent versions installation;stale ### How you are installing vllm ```sh export VLLM_VERSION=0.7.0 export PYTHON_VERSION=38 pip install --force-reinstall https://github.com/vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
