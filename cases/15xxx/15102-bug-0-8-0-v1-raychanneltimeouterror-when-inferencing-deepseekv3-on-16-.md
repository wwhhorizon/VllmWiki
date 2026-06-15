# vllm-project/vllm#15102: [Bug]: 0.8.0(V1) RayChannelTimeoutError when inferencing DeepSeekV3 on 16 H20 with large batch size

| 字段 | 值 |
| --- | --- |
| Issue | [#15102](https://github.com/vllm-project/vllm/issues/15102) |
| 状态 | open |
| 标签 | bug;ray;stale |
| 评论 | 44; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.8.0(V1) RayChannelTimeoutError when inferencing DeepSeekV3 on 16 H20 with large batch size

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Firstly I follow the doc https://docs.vllm.ai/en/latest/serving/distributed_serving.html to setup the distributed environment(2 nodes with 8 GPUs per node), and then run the api_server as below: ```bash python3 -m vllm.entrypoints.openai.api_server --port 18011 --model /models/DeepSeek-V3 --tensor-parallel-size 16 --gpu-memory-utilization 0.92 --dtype auto --served-model-name deepseekv3 --max-num-seqs 50 --max-model-len 16384 --trust-remote-code --disable-log-requests --enable-chunked-prefill --enable-prefix-caching ``` Then I got the RayChannelTimeoutError in Ray module within the call `execute_model` to run ray dag. ```text INFO 03-14 00:00:55 [async_llm.py:169] Added request cmpl-49612d570051487899170dc9fc843162-0. INFO 03-14 00:00:59 [loggers.py:80] Avg prompt throughput: 102.5 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.2%, Prefix cache hit rate: 13.4% ERROR 03-14 00:01:05 [core.py:337] EngineCore hit an exception: Traceback (most recent call last): ERROR 03-14 00:01:05 [core.py:337] File "/usr/local/lib/python3.12/dist-packages/ray/dag/compiled_dag_node.py", lin...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: rror when inferencing DeepSeekV3 on 16 H20 with large batch size bug;ray;stale ### Your current environment ### 🐛 Describe the bug Firstly I follow the doc https://docs.vllm.ai/en/latest/serving/distributed_serving.html...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: 0.8.0(V1) RayChannelTimeoutError when inferencing DeepSeekV3 on 16 H20 with large batch size bug;ray;stale ### Your current environment ### 🐛 Describe the bug Firstly I follow the doc https://docs.vllm.ai/en/late...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 0.1 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.2%, Prefix cache hit rate: 13.4% ERROR 03-14 00:01:05 [core.py:337] EngineCore hit an exception: Traceback (most recent call las...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: # 🐛 Describe the bug Firstly I follow the doc https://docs.vllm.ai/en/latest/serving/distributed_serving.html to setup the distributed environment(2 nodes with 8 GPUs per node), and then run the api_server as below: ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
