# vllm-project/vllm#17881: [Bug]: object has no attribute 'finished_req_ids'

| 字段 | 值 |
| --- | --- |
| Issue | [#17881](https://github.com/vllm-project/vllm/issues/17881) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: object has no attribute 'finished_req_ids'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are running with the following components: * KubeAI 0.20.0 * vLLM 0.8.5 * Ray 2.43.0 * AKS v1.30.9 using Standard_NC80adis_H100_v5 (2 x H100) vms. We are testing distributed inferencing of a **gemma-3-27b-it** model over 3 nodes (pipeline parallel of 3) with 2 GPUs per node (tensor parallel of 2). We have successfully run this over 2 nodes without issue. However with 3 nodes we are seeing the following exception. ``` INFO 05-08 20:04:39 [loggers.py:111] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 4092.7 tokens/s, Running: 803 reqs, Waiting: 168 reqs, GPU KV cache usage: 99.9%, Prefix cache hit rate: 0.0% DEBUG 05-08 20:04:40 [async_llm.py:467] Called check_health. INFO: 10.43.33.166:37956 - "GET /health HTTP/1.1" 200 OK DEBUG 05-08 20:04:40 [async_llm.py:467] Called check_health. INFO: 10.43.33.166:37970 - "GET /health HTTP/1.1" 200 OK INFO 05-08 20:04:49 [loggers.py:111] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 3880.0 tokens/s, Running: 766 reqs, Waiting: 204 reqs, GPU KV cache usage: 100.0%, Prefix cache hit rate: 0.0% DEBUG 05-08 20:04:50 [async_llm.py:467]...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: object has no attribute 'finished_req_ids' bug;stale ### Your current environment ### 🐛 Describe the bug We are running with the following components: * KubeAI 0.20.0 * vLLM 0.8.5 * Ray 2.43.0 * AKS v1.30.9 using...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: dard_NC80adis_H100_v5 (2 x H100) vms. We are testing distributed inferencing of a **gemma-3-27b-it** model over 3 nodes (pipeline parallel of 3) with 2 GPUs per node (tensor parallel of 2). We have successfully run this...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: xception on is from vLLM. Our model arguments are as follows: ``` - --dtype=bfloat16 - --tensor-parallel-size=2 - --pipeline-parallel-size=3 - --no-enable-prefix-caching - --gpu-memory-utilization=0.95 - --distributed-e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: I 0.20.0 * vLLM 0.8.5 * Ray 2.43.0 * AKS v1.30.9 using Standard_NC80adis_H100_v5 (2 x H100) vms. We are testing distributed inferencing of a **gemma-3-27b-it** model over 3 nodes (pipeline parallel of 3) with 2 GPUs per...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: fix-caching - --gpu-memory-utilization=0.95 - --distributed-executor-backend=ray - --trust-remote-code - --max-num-batched-tokens=32768 - --enable-chunked-prefill ``` Our model environment variables are as follows: ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
