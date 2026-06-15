# vllm-project/vllm#30114: [Bug]: Speculative decoding support for mamba models

| 字段 | 值 |
| --- | --- |
| Issue | [#30114](https://github.com/vllm-project/vllm/issues/30114) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Speculative decoding support for mamba models

### Issue 正文摘录

### Your current environment (EngineCore_0 pid=469) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_model_runner.py", line 3077, in get_kv_cache_spec (EngineCore_0 pid=469) raise NotImplementedError( (EngineCore_0 pid=469) NotImplementedError: Mamba with speculative decoding is not supported yet. Is this in motion for next release? Curious if there are any hurdles to getting this to work, I had assumed it would be straightforward. ### 🐛 Describe the bug (EngineCore_0 pid=469) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_model_runner.py", line 3077, in get_kv_cache_spec (EngineCore_0 pid=469) raise NotImplementedError( (EngineCore_0 pid=469) NotImplementedError: Mamba with speculative decoding is not supported yet. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: et. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Speculative decoding support for mamba models bug ### Your current environment (EngineCore_0 pid=469) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_model_runner.py", line 3077, in get_kv_cache_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Speculative decoding support for mamba models bug ### Your current environment (EngineCore_0 pid=469) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_model_runner.py", line 3077, in get_kv_cache_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
