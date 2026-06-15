# vllm-project/vllm#26957: [Bug]: Python 3.9 compatibility issue in 0.11.0

| 字段 | 值 |
| --- | --- |
| Issue | [#26957](https://github.com/vllm-project/vllm/issues/26957) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Python 3.9 compatibility issue in 0.11.0

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug After trying to upgrade to use v0.11.0 getting following stack trace which looks like python 3.9 is not supported anymore? Looks like union type operator was introduced in Python 3.10? ``` Internal: TypeError: unsupported operand type(s) for |: 'type' and 'NoneType' At: vllm/model_executor/models/registry.py(442): _LazyRegisteredModel vllm/model_executor/models/registry.py(426): importlib._bootstrap: _call_with_frames_removed importlib._bootstrap_external: exec_module vllm/model_executor/models/__init__.py(11): vllm/entrypoints/chat_utils.py(48): vllm/entrypoints/openai/protocol.py(52): vllm/reasoning/basic_parsers.py(8): vllm/engine/arg_utils.py(42): vllm/entrypoints/llm.py(19): vllm/__init__.py(68): __getattr__ ... ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: RegisteredModel vllm/model_executor/models/registry.py(426): importlib._bootstrap: _call_with_frames_removed importlib._bootstrap_external: exec_module vllm/model_executor/models/__init__.py(11): vllm/entrypoints/chat_u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Error: unsupported operand type(s) for |: 'type' and 'NoneType' At: vllm/model_executor/models/registry.py(442): _LazyRegisteredModel vllm/model_executor/models/registry.py(426): importlib._bootstrap: _call_with_frames_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Python 3.9 compatibility issue in 0.11.0 bug;stale ### Your current environment N/A ### 🐛 Describe the bug After trying to upgrade to use v0.11.0 getting following stack trace which looks like python 3.9 is not s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
