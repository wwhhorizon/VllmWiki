# vllm-project/vllm#30660: [Bug]: [Elastic EP]: AssertionError in replicate_experts during DP4 → DP2 scale-down

| 字段 | 值 |
| --- | --- |
| Issue | [#30660](https://github.com/vllm-project/vllm/issues/30660) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Elastic EP]: AssertionError in replicate_experts during DP4 → DP2 scale-down

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug During Elastic EP (Elastic Expert Parallelism) scale-down from data parallelism degree 4 to 2, an AssertionError occurs in the replicate_experts function when calculating expert rebalancing. The assertion assert num_redundant >= 0 fails during the expert redistribution process, indicating a negative redundant expert count calculation. Sample Code: ```bash vllm serve /ssd3/models/Qwen3-30B-A3B \ --trust-remote-code \ --disable-log-requests \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.9 \ --max-model-len 16384 \ --no-enable-prefix-caching \ --enable-expert-parallel \ --all2all-backend pplx \ --enable-elastic-ep \ --enable-eplb \ --eplb-config.num_redundant_experts 0 \ --eplb-config.min_replica 1 \ --data-parallel-backend ray \ --data-parallel-size 4 \ --data-parallel-size-local 4 \ --data-parallel-start-rank 0 \ --host 0.0.0.0 \ --port 8006 ``` ```bash python scale_script.py --host 0.0.0.0 --port 8006 --new-dp-size 2 ``` Error Message: ```bash (APIServer pid=666598) (DPEngineCoreActor pid=666982) ERROR 12-14 17:43:10 [core.py:1525] EngineCore encountered a fatal error. (APIServer pid=666598) (DPEngineCoreActor pid=666982...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: occurs in the replicate_experts function when calculating expert rebalancing. The assertion assert num_redundant >= 0 fails during the expert redistribution process, indicating a negative redundant expert count calculat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t ### 🐛 Describe the bug During Elastic EP (Elastic Expert Parallelism) scale-down from data parallelism degree 4 to 2, an AssertionError occurs in the replicate_experts function when calculating expert rebalancing. The...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: dundant expert count calculation. Sample Code: ```bash vllm serve /ssd3/models/Qwen3-30B-A3B \ --trust-remote-code \ --disable-log-requests \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.9 \ --max-model-len 163...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: [Elastic EP]: AssertionError in replicate_experts during DP4 → DP2 scale-down bug;stale ### Your current environment ### 🐛 Describe the bug During Elastic EP (Elastic Expert Parallelism) scale-down from data para...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: EP]: AssertionError in replicate_experts during DP4 → DP2 scale-down bug;stale ### Your current environment ### 🐛 Describe the bug During Elastic EP (Elastic Expert Parallelism) scale-down from data parallelism degree 4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
