# vllm-project/vllm#21219: [Bug]: Middleware crashes vLLM on startup w/latest commit

| 字段 | 值 |
| --- | --- |
| Issue | [#21219](https://github.com/vllm-project/vllm/issues/21219) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Middleware crashes vLLM on startup w/latest commit

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Starting up vLLM with a middleware and the below args works on 0.9.2, but fails on the latest commit: **ARGS:** ``` VllmWorker rank=0 pid=454) INFO 07-18 22:45:56 [gpu_model_runner.py:2321] Graph capturing finished in 67 secs, took 2.01 GiB INFO 07-18 22:45:56 [core.py:178] init engine (profile, create kv cache, warmup model) took 165.37 seconds INFO 07-18 22:46:02 [loggers.py:137] Engine 000: vllm cache_config_info with initialization after num_gpu_blocks is: 209027 Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 1752, in uvloop.run(run_server(args)) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: .12/dist-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t: **ARGS:** ``` VllmWorker rank=0 pid=454) INFO 07-18 22:45:56 [gpu_model_runner.py:2321] Graph capturing finished in 67 secs, took 2.01 GiB INFO 07-18 22:45:56 [core.py:178] init engine (profile, create kv cache, warm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Middleware crashes vLLM on startup w/latest commit bug ### Your current environment ### 🐛 Describe the bug Starting up vLLM with a middleware and the below args works on 0.9.2, but fails on the latest commit: **A...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 2.01 GiB INFO 07-18 22:45:56 [core.py:178] init engine (profile, create kv cache, warmup model) took 165.37 seconds INFO 07-18 22:46:02 [loggers.py:137] Engine 000: vllm cache_config_info with initialization after num_g...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
