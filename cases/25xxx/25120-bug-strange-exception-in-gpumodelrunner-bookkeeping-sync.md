# vllm-project/vllm#25120: [Bug]: Strange exception in `GPUModelRunner._bookkeeping_sync`

| 字段 | 值 |
| --- | --- |
| Issue | [#25120](https://github.com/vllm-project/vllm/issues/25120) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Strange exception in `GPUModelRunner._bookkeeping_sync`

### Issue 正文摘录

### Your current environment vllm==0.10 torch=2.7.0 ### 🐛 Describe the bug I got a very strange exception message out of `GPUModelRunner._bookkeeping_sync`: `AssertionError: Sampled token IDs exceed the max model length. Total number of tokens: 1281 > max_model_len: 1280` at https://github.com/vllm-project/vllm/blob/e95084308b2032748e226f420e93becaf3af64d5/vllm/v1/worker/gpu_model_runner.py#L1983-L1986 It's as if for some reason, the model managed to generate more tokens than `max_model_len` allows. But it's not supposed to happen, right? vllm usually just stops and returns partial response, not fails for extra-generated tokens ``` ERROR 09-13 02:50:25 [core.py:634] EngineCore encountered a fatal error. ERROR 09-13 02:50:25 [core.py:634] Traceback (most recent call last): ERROR 09-13 02:50:25 [core.py:634] File "/tmp/ray/session_2025-09-12_18-34-34_574746_110018/runtime_resources/working_dir_files/_ray_pkg_83ec426c3cf029b3/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 625, in run_engine_core ERROR 09-13 02:50:25 [core.py:634] engine_core.run_busy_loop() ERROR 09-13 02:50:25 [core.py:634] File "/tmp/ray/session_2025-09-12_18-34-34_574746_110018/runtime_resources/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Strange exception in `GPUModelRunner._bookkeeping_sync` bug ### Your current environment vllm==0.10 torch=2.7.0 ### 🐛 Describe the bug I got a very strange exception message out of `GPUModelRunner._bookkeeping_sy...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: el_with_error_logging ERROR 09-13 02:50:25 [core.py:634] return model_fn(scheduler_output) ERROR 09-13 02:50:25 [core.py:634] ^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 09-13 02:50:25 [core.py:634] File "/tmp/ray/session_2025-09-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
