# vllm-project/vllm#36221: [Bug]: Two-node deployment of kimi2-5, runtime crash

| 字段 | 值 |
| --- | --- |
| Issue | [#36221](https://github.com/vllm-project/vllm/issues/36221) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;gemm;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Two-node deployment of kimi2-5, runtime crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Kimi 2-5 Dual-Machine Deployment Crash under High Concurrency (H100 + MP Mode)，Models run normally under low concurrency but crash under high concurrency. This issue also occurs with two-machine deployed models such as GLM, and the error messages are identical across all cases. ## Environment H100 GPUs, vLLM, Kimi 2-5 model, two-node deployment with MP (Model Parallelism) mode ## Core Issue Model works normally under low concurrency but crashes with `EngineDeadError` when concurrency increases ### 1. Deployment Command ```bash # Node 0 command vllm serve \ /workspace/kimi/model/Kimi-K2.5 \ --served-model-name kimi-k2-5-thinking \ --enable-log-requests \ --mm-encoder-tp-mode data \ --compilation_config.pass_config.fuse_allreduce_rms true \ --gpu-memory-utilization=0.9 \ --max-model-len 128000 \ --port 8000 \ --trust-remote-code \ --enable-auto-tool-choice \ --tool-call-parser kimi_k2 \ --reasoning-parser kimi_k2 \ --tensor-parallel-size 8 \ --data-parallel-size 2 \ --nnodes 2 --node-rank 0 \ --master-addr {ip_address} # Node 1 command vllm serve \ /workspace/kimi/model/Kimi-K2.5 \ --served-model-name kimi-k2-5-thinking \ --enable-...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: the bug Kimi 2-5 Dual-Machine Deployment Crash under High Concurrency (H100 + MP Mode)，Models run normally under low concurrency but crash under high concurrency. This issue also occurs with two-machine deployed models...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding cache;cuda;gemm;operator;q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: -5 Dual-Machine Deployment Crash under High Concurrency (H100 + MP Mode)，Models run normally under low concurrency but crash under high concurrency. This issue also occurs with two-machine deployed models such as GLM, a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -06 10:49:56 [shm_broadcast.py:548] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: /model/Kimi-K2.5 \ --served-model-name kimi-k2-5-thinking \ --enable-log-requests \ --mm-encoder-tp-mode data \ --compilation_config.pass_config.fuse_allreduce_rms true \ --gpu-memory-utilization=0.9 \ --max-model-len 1...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
