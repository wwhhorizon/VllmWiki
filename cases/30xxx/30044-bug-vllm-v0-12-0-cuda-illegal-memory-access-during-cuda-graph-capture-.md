# vllm-project/vllm#30044: [Bug]: vLLM v0.12.0: CUDA Illegal Memory Access During CUDA Graph Capture on Multi-Node GH200 (TP=4, PP=2)

| 字段 | 值 |
| --- | --- |
| Issue | [#30044](https://github.com/vllm-project/vllm/issues/30044) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM v0.12.0: CUDA Illegal Memory Access During CUDA Graph Capture on Multi-Node GH200 (TP=4, PP=2)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With vLLM version 0.12.0, running on a 2-node setup (8 GPUs total) using tensor parallelism 4 and pipeline parallelism 2, the system crashes with a `cudaErrorIllegalAddress` during startup. vLLM version 0.11.0 works fine under the same setup (but without flash infer) if the environment variable `VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TYPE=shm` is set, as mentioned in [issue #15332](https://github.com/vllm-project/vllm/issues/15332). Moreover, when starting vLLM 0.12.0 with the `--enforce-eager` option, vllm starts successfully but crashes again after processing roughly 1000 requests. Strangely enough, using the same setup (but with tp=2, pp=2), but on a single node (I tested both mp and ray), does work. Hardware: 2 nodes × 4× NVIDIA GH200 (8 GPUs total) vLLM: v0.12.0 (fails), v0.11.0 (works) Model: openai/gpt-oss-120b Parallelism: --tensor-parallel-size 4 --pipeline-parallel-size 2 Overall Setup: ```bash --distributed-executor-backend ray --gpu-memory-utilization 0.90 --dtype bfloat16 --enable-prefix-caching --max-model-len 8192 export VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TYPE=shm export RAY_CGRAPH_read_iteration_timeout_s=10 ``` ### Bef...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: stale ### Your current environment ### 🐛 Describe the bug With vLLM version 0.12.0, running on a 2-node setup (8 GPUs total) using tensor parallelism 4 and pipeline parallelism 2, the system crashes with a `cudaErrorIll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: bash --distributed-executor-backend ray --gpu-memory-utilization 0.90 --dtype bfloat16 --enable-prefix-caching --max-model-len 8192 export VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TYPE=shm export RAY_CGRAPH_read_iteration_time...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vLLM v0.12.0: CUDA Illegal Memory Access During CUDA Graph Capture on Multi-Node GH200 (TP=4, PP=2) bug;stale ### Your current environment ### 🐛 Describe the bug With vLLM version 0.12.0, running on a 2-node setu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ry Access During CUDA Graph Capture on Multi-Node GH200 (TP=4, PP=2) bug;stale ### Your current environment ### 🐛 Describe the bug With vLLM version 0.12.0, running on a 2-node setup (8 GPUs total) using tensor parallel...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -pipeline-parallel-size 2 Overall Setup: ```bash --distributed-executor-backend ray --gpu-memory-utilization 0.90 --dtype bfloat16 --enable-prefix-caching --max-model-len 8192 export VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TY...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
