# vllm-project/vllm#16637: [Feature]: support nvidia/Llama-3_1-Nemotron-Ultra-253B-v1

| 字段 | 值 |
| --- | --- |
| Issue | [#16637](https://github.com/vllm-project/vllm/issues/16637) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support nvidia/Llama-3_1-Nemotron-Ultra-253B-v1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When I tried to deploy demotron model with vllm , it throws error from the library: INFO 04-14 23:55:41 [config.py:585] This model supports multiple tasks: {'classify', 'generate', 'score', 'reward', 'embed'}. Defaulting to 'generate'. DEBUG 04-14 23:55:41 [arg_utils.py:1811] Setting max_num_batched_tokens to 8192 for OPENAI_API_SERVER usage context. DEBUG 04-14 23:55:41 [arg_utils.py:1819] Setting max_num_seqs to 1024 for OPENAI_API_SERVER usage context. INFO 04-14 23:55:41 [config.py:1697] Chunked prefill is enabled with max_num_batched_tokens=8192. Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 1066, in uvloop.run(run_server(args)) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: support nvidia/Llama-3_1-Nemotron-Ultra-253B-v1 feature request;stale ### 🚀 The feature, motivation and pitch When I tried to deploy demotron model with vllm , it throws error from the library: INFO 04-14 23:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: support nvidia/Llama-3_1-Nemotron-Ultra-253B-v1 feature request;stale ### 🚀 The feature, motivation and pitch When I tried to deploy demotron model with vllm , it throws error from the library: INFO 04-14 23:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: .12/dist-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
