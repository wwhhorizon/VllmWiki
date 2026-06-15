# vllm-project/vllm#33534: [Installation]: vllm with ray in AWS cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#33534](https://github.com/vllm-project/vllm/issues/33534) |
| 状态 | open |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: vllm with ray in AWS cluster

### Issue 正文摘录

### Your current environment ```text vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 --tensor-parallel-size 1 --pipeline-parallel-size 2 --host 0.0.0.0 --port 8000 --distributed-executor-backend ray --gpu-memory-utilization 0.9 --max-model-len 4096 --max-num-seqs 50 --max-num-batched-tokens 4096 --block-size 16 --dtype half (APIServer pid=23643) INFO 02-01 17:54:53 [api_server.py:1272] vLLM API server version 0.14.1 (APIServer pid=23643) INFO 02-01 17:54:53 [utils.py:263] non-default args: {'model_tag': 'Qwen/Qwen3-VL-30B-A3B-Instruct-FP8', 'host': '0.0.0.0', 'model': 'Qwen/Qwen3-VL-30B-A3B-Instruct-FP8', 'dtype': 'half', 'max_model_len': 4096, 'distributed_executor_backend': 'ray', 'pipeline_parallel_size': 2, 'block_size': 16, 'max_num_batched_tokens': 4096, 'max_num_seqs': 50} (APIServer pid=23643) INFO 02-01 17:55:00 [model.py:530] Resolved architecture: Qwen3VLMoeForConditionalGeneration (APIServer pid=23643) WARNING 02-01 17:55:00 [model.py:1869] Casting torch.bfloat16 to torch.float16. (APIServer pid=23643) INFO 02-01 17:55:00 [model.py:1545] Using max model len 4096 (APIServer pid=23643) INFO 02-01 17:55:00 [scheduler.py:229] Chunked prefill is enabled with max_num_batched_t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: vllm with ray in AWS cluster installation;stale ### Your current environment ```text vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 --tensor-parallel-size 1 --pipeline-parallel-size 2 --host 0.0.0.0 --port
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: r current environment ```text vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 --tensor-parallel-size 1 --pipeline-parallel-size 2 --host 0.0.0.0 --port 8000 --distributed-executor-backend ray --gpu-memory-utilization 0.9...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ster installation;stale ### Your current environment ```text vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 --tensor-parallel-size 1 --pipeline-parallel-size 2 --host 0.0.0.0 --port 8000 --distributed-executor-backend ra...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Installation]: vllm with ray in AWS cluster installation;stale ### Your current environment ```text vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 --tensor-parallel-size 1 --pipeline-parallel-size 2 --host 0.0.0.0 --por...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: peline-parallel-size 2 --host 0.0.0.0 --port 8000 --distributed-executor-backend ray --gpu-memory-utilization 0.9 --max-model-len 4096 --max-num-seqs 50 --max-num-batched-tokens 4096 --block-size 16 --dtype half (APISer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
