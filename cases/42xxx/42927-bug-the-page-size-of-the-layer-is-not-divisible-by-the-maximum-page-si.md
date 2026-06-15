# vllm-project/vllm#42927: [Bug]: "The page size of the layer is not divisible by the maximum page size" When serving Qwen3.5 MoE with custom "VLLM_PP_LAYER_PARTITION"

| 字段 | 值 |
| --- | --- |
| Issue | [#42927](https://github.com/vllm-project/vllm/issues/42927) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "The page size of the layer is not divisible by the maximum page size" When serving Qwen3.5 MoE with custom "VLLM_PP_LAYER_PARTITION"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving Qwen3.5-122B-A10B, whenever I add `VLLM_PP_LAYER_PARTITION=7,7,7,3,3,3,3,3,3,3,3,3` or values alike, the following exception would raise: ``` (EngineCore pid=14704) ERROR 05-18 12:49:15 [core.py:1159] EngineCore failed to start. (EngineCore pid=14704) ERROR 05-18 12:49:15 [core.py:1159] Traceback (most recent call last): (EngineCore pid=14704) ERROR 05-18 12:49:15 [core.py:1159] File "/root/swift/erepo/vllm/vllm/v1/engine/core.py", line 1133, in run_engine_core (EngineCore pid=14704) ERROR 05-18 12:49:15 [core.py:1159] engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore pid=14704) ERROR 05-18 12:49:15 [core.py:1159] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=14704) ERROR 05-18 12:49:15 [core.py:1159] File "/root/swift/erepo/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore pid=14704) ERROR 05-18 12:49:15 [core.py:1159] return func(*args, **kwargs) (EngineCore pid=14704) ERROR 05-18 12:49:15 [core.py:1159] ^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=14704) ERROR 05-18 12:49:15 [core.py:1159] File "/root/swift/erepo/vllm/vllm/v1/engine/core.py", line 899,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ROR 05-18 12:49:15 [core.py:1159] File "/root/swift/erepo/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore pid=14704) ERROR 05-18 12:49:15 [core.py:1159] return func(*args, **kwargs) (EngineCore pid=147...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: "The page size of the layer is not divisible by the maximum page size" When serving Qwen3.5 MoE with custom "VLLM_PP_LAYER_PARTITION" bug ### Your current environment ### 🐛 Describe the bug When serving Qwen3.5-1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ize of the layer is not divisible by the maximum page size" When serving Qwen3.5 MoE with custom "VLLM_PP_LAYER_PARTITION" bug ### Your current environment ### 🐛 Describe the bug When serving Qwen3.5-122B-A10B, whenever...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: he maximum page size. Cannot unify by adjusting block_size. ``` I have searched for related issues and most seems to be fixed already, but in my case using an uneven pipeline parallel config will still reproduce it. I h...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: he layer is not divisible by the maximum page size" When serving Qwen3.5 MoE with custom "VLLM_PP_LAYER_PARTITION" bug ### Your current environment ### 🐛 Describe the bug When serving Qwen3.5-122B-A10B, whenever I add `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
