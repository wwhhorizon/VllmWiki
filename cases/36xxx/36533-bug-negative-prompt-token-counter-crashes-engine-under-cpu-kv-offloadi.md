# vllm-project/vllm#36533: [Bug]: Negative prompt token counter crashes engine under CPU KV offloading + high concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#36533](https://github.com/vllm-project/vllm/issues/36533) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | attention;cache |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Negative prompt token counter crashes engine under CPU KV offloading + high concurrency

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run server with: ``` vllm serve nvidia/Llama-3.3-70B-Instruct-FP4 --host 0.0.0.0 --port 8888 --config /workspace/results/config.yaml --max-num-seqs 1024 --gpu-memory-utilization 0.9 --tensor-parallel-size 1 --attention-config.use_trtllm_attention=0 --kv_offloading_backend native --kv_offloading_size 100 --disable-hybrid-kv-cache-manager ``` Run basic multiturn benchmark client against server with concurrency equal to 2048 (and `--max-num-seqs` set accordingly). Observe error: ``` (APIServer pid=1327397) INFO 03-09 14:34:35 [loggers.py:259] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 770.3 tokens/s, Running: 256 reqs, Waiting: 764 reqs, GPU KV cache usage: 97.5%, Prefix cache hit rate: 4.3%, External prefix cache hit rate: 0.0% (APIServer pid=1327397) INFO 03-09 14:34:35 [metrics.py:103] KV Transfer metrics: CPU_to_GPU_total_bytes=810024960, CPU_to_GPU_total_time=0.19331251902878285, GPU_to_CPU_total_bytes=55050240, GPU_to_CPU_total_time=0.0010710399970412254 (APIServer pid=1327397) INFO: 127.0.0.1:58324 - "GET /metrics HTTP/1.1" 200 OK (APIServer pid=1327397) INFO: 127.0.0.1:58324 - "GET /metrics H...

## 现有链接修复摘要

#36638 [WIP][Bugfix] Fix negative prompt token counter crash under KV offloading

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: Negative prompt token counter crashes engine under CPU KV offloading + high concurrency bug ### Your current environment ### 🐛 Describe the bug Run server with: ``` vllm serve nvidia/Llama-3.3-70B-Instruct-FP4 --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tokens/s, Avg generation throughput: 770.3 tokens/s, Running: 256 reqs, Waiting: 764 reqs, GPU KV cache usage: 97.5%, Prefix cache hit rate: 4.3%, External prefix cache hit rate: 0.0% (APIServer pid=1327397) INFO 03-09...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e the bug Run server with: ``` vllm serve nvidia/Llama-3.3-70B-Instruct-FP4 --host 0.0.0.0 --port 8888 --config /workspace/results/config.yaml --max-num-seqs 1024 --gpu-memory-utilization 0.9 --tensor-parallel-size 1 --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nment ### 🐛 Describe the bug Run server with: ``` vllm serve nvidia/Llama-3.3-70B-Instruct-FP4 --host 0.0.0.0 --port 8888 --config /workspace/results/config.yaml --max-num-seqs 1024 --gpu-memory-utilization 0.9 --tensor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ding_size 100 --disable-hybrid-kv-cache-manager ``` Run basic multiturn benchmark client against server with concurrency equal to 2048 (and `--max-num-seqs` set accordingly). Observe error: ``` (APIServer pid=1327397) I...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36638](https://github.com/vllm-project/vllm/pull/36638) | closes_keyword | 0.95 | [WIP][Bugfix] Fix negative prompt token counter crash under KV offloading | Fix engine crash (`ValueError: Counters can only be incremented by non-negative amounts`) that occurs under high concurrency with CPU KV offloading enabled (GitHub issue #36533). |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
