# vllm-project/vllm#8235: [Bug]: Missing TextTokenPrompts class

| 字段 | 值 |
| --- | --- |
| Issue | [#8235](https://github.com/vllm-project/vllm/issues/8235) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Missing TextTokenPrompts class

### Issue 正文摘录

### 🐛 Describe the bug I tried to pull a vllm docker image and run it on my 4060 GPU bit I am encountering this error: File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/opt/vllm/lib64/python3.11/site-packages/vllm_tgis_adapter/__main__.py", line 43, in from .grpc import run_grpc_server File "/opt/vllm/lib64/python3.11/site-packages/vllm_tgis_adapter/grpc/__init__.py", line 1, in from .grpc_server import run_grpc_server File "/opt/vllm/lib64/python3.11/site-packages/vllm_tgis_adapter/grpc/grpc_server.py", line 23, in from vllm.inputs import TextTokensPrompt ImportError: cannot import name 'TextTokensPrompt' from 'vllm.inputs' (/opt/vllm/lib64/python3.11/site-packages/vllm/inputs/__init__.py) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: enPrompts class bug;stale ### 🐛 Describe the bug I tried to pull a vllm docker image and run it on my 4060 GPU bit I am encountering this error: File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: py) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Missing TextTokenPrompts class bug;stale ### 🐛 Describe the bug I tried to pull a vllm docker image and run it on my 4060 GPU bit I am encountering this error: File " ", line 198, in _run_module_as_main File " ",...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
