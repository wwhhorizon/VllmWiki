# vllm-project/vllm#17395: [Bug]: vllm.entrypoints.api_server throw exception when startup in v0.8.5

| 字段 | 值 |
| --- | --- |
| Issue | [#17395](https://github.com/vllm-project/vllm/issues/17395) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm.entrypoints.api_server throw exception when startup in v0.8.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug python3 -m vllm.entrypoints.api_server --model Qwen/Qwen2-7B-Instruct --tensor-parallel-size=2 --gpu-memory-utilization 0.95 --port 21131 --enforce-eager --trust-remote-code Whenever the above command is executed, the following exception will be thrown. This issue did not occur before v0.8.5. ```text (VllmWorker rank=0 pid=47465) (VllmWorker rank=0 pid=47465) INFO 04-29 22:59:27 [loader.py:458] Loading weights took 3.59 seconds (VllmWorker rank=0 pid=47465) INFO 04-29 22:59:27 [gpu_model_runner.py:1347] Model loading took 7.1217 GiB and 170.700889 seconds INFO 04-29 22:59:31 [kv_cache_utils.py:634] GPU KV cache size: 473,184 tokens INFO 04-29 22:59:31 [kv_cache_utils.py:637] Maximum concurrency for 32,768 tokens per request: 14.44x INFO 04-29 22:59:31 [kv_cache_utils.py:634] GPU KV cache size: 473,184 tokens INFO 04-29 22:59:31 [kv_cache_utils.py:637] Maximum concurrency for 32,768 tokens per request: 14.44x INFO 04-29 22:59:31 [core.py:159] init engine (profile, create kv cache, warmup model) took 3.96 seconds INFO 04-29 22:59:31 [core_client.py:439] Core engine process 0 ready. INFO 04-29 22:59:31 [launcher.py:28] Available rou...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 10/site-packages/vllm/entrypoints/api_server.py", line 177, in asyncio.run(run_server(args)) File "/data/miniconda3/envs/env-3.10/lib/python3.10/asyncio/runners.py", line 44, in run return loop.run_until_complete(main)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ent ### 🐛 Describe the bug python3 -m vllm.entrypoints.api_server --model Qwen/Qwen2-7B-Instruct --tensor-parallel-size=2 --gpu-memory-utilization 0.95 --port 21131 --enforce-eager --trust-remote-code Whenever the above...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: :59:31 [kv_cache_utils.py:637] Maximum concurrency for 32,768 tokens per request: 14.44x INFO 04-29 22:59:31 [kv_cache_utils.py:634] GPU KV cache size: 473,184 tokens INFO 04-29 22:59:31 [kv_cache_utils.py:637] Maximum...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: okens per request: 14.44x INFO 04-29 22:59:31 [core.py:159] init engine (profile, create kv cache, warmup model) took 3.96 seconds INFO 04-29 22:59:31 [core_client.py:439] Core engine process 0 ready. INFO 04-29 22:59:3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
