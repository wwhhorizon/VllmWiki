# vllm-project/vllm#26899: [Bug]: qwen3-235b-a22b-instruct-2507 fails on multi-node deployment

| 字段 | 值 |
| --- | --- |
| Issue | [#26899](https://github.com/vllm-project/vllm/issues/26899) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen3-235b-a22b-instruct-2507 fails on multi-node deployment

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to serve [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507) on 2 nodes (8x A100s each), but the vllm serving randomly stops and crashes. Steps: 1. Start ray on both nodes using `ray start --head` and `ray start --address="..."` 2. Serve the model on the head node using vllm serve: `vllm serve Qwen/Qwen3-235B-A22B-Instruct-2507 --tensor-parallel-size 8 --pipeline-parallel-size 2 --max-model-len 1010000 --enable-chunked-prefill --gpu-memory-utilization 0.95 --api-key "abc" --distributed-executor-backend ray --host 0.0.0.0 --port 8000 --enable-expert-parallel --enforce-eager` The model gets loaded correctly and the FastAPI server is made available, but after a few inference requests, the serving crashes. I'm not sure if this is a vllm bug or ray bug. Initially I assumed it was due to the number of requests I was sending concurrently, so I reduced to 1 request at a time, but that doesn't fix the issue either. I've experimented with different gpu memory utilization settings and disabling 'enforce-eager' as well. ### Before submitting a new issue... - [x] Make sure you already searched...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: qwen3-235b-a22b-instruct-2507 fails on multi-node deployment bug;stale ### Your current environment ### 🐛 Describe the bug I'm trying to serve [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ttps://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507) on 2 nodes (8x A100s each), but the vllm serving randomly stops and crashes. Steps: 1. Start ray on both nodes using `ray start --head` and `ray start --address=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen3-235b-a22b-instruct-2507 fails on multi-node deployment bug;stale ### Your current environment ### 🐛 Describe the bug I'm trying to serve [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ill --gpu-memory-utilization 0.95 --api-key "abc" --distributed-executor-backend ray --host 0.0.0.0 --port 8000 --enable-expert-parallel --enforce-eager` The model gets loaded correctly and the FastAPI server is made av...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
