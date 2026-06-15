# vllm-project/vllm#40862: [Bug]: DeepSeek-V4-Pro H200 DP+EP router dtype mismatch in topk_hash_softplus_sqrt (Long/Int inconsistency)

| 字段 | 值 |
| --- | --- |
| Issue | [#40862](https://github.com/vllm-project/vllm/issues/40862) |
| 状态 | open |
| 标签 | bug;DSv4 |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;moe;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V4-Pro H200 DP+EP router dtype mismatch in topk_hash_softplus_sqrt (Long/Int inconsistency)

### Issue 正文摘录

### Your current environment Environment - vLLM image: `vllm/vllm-openai:deepseekv4-cu130` - Model: `deepseek-ai/DeepSeek-V4-Pro` - Hardware: NVIDIA H200 - Reproduced on: - single-node `8x H200` with `DP=8 + EP` - multi-node `16x H200` with `DP=16 + EP` - Fabric/network is healthy; other large-model runs on this cluster are fine ### 🐛 Describe the bug Observed failure The intended DeepSeek-V4-Pro `DP+EP` path fails during startup/profiling in the fused router path, with dtype mismatch errors around `topk_hash_softplus_sqrt`. Original failure: - `expected scalar type Long but found Int` The failing stack goes through: - `fused_topk_bias_router.py` - `ops.topk_hash_softplus_sqrt` - `torch.ops._moe_C.topk_softplus_sqrt` I tested a monkey-patch around `vllm._custom_ops.topk_hash_softplus_sqrt` to log dtypes and force suspected tensors to `torch.long`. Observed dtypes at the op boundary: - `topk_indices`: `torch.int64` - `input_tokens`: `torch.int64` - `hash_indices_table`: `torch.int64` - `token_expert_indices`: `torch.int32` After forcing the relevant integer tensors to `Long`, the error flipped to: - `expected scalar type Int but found Long` So a blanket “cast indices to Long” worka...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: _table`: `torch.int64` - `token_expert_indices`: `torch.int32` After forcing the relevant integer tensors to `Long`, the error flipped to: - `expected scalar type Int but found Long` So a blanket “cast indices to Long”...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: DeepSeek-V4-Pro H200 DP+EP router dtype mismatch in topk_hash_softplus_sqrt (Long/Int inconsistency) bug;DSv4 ### Your current environment Environment - vLLM image: `vllm/vllm-openai:deepseekv4-cu130` - Model: `d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: d failure The intended DeepSeek-V4-Pro `DP+EP` path fails during startup/profiling in the fused router path, with dtype mismatch errors around `topk_hash_softplus_sqrt`. Original failure: - `expected scalar type Long bu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: DeepSeek-V4-Pro H200 DP+EP router dtype mismatch in topk_hash_softplus_sqrt (Long/Int inconsistency) bug;DSv4 ### Your current environment Environment - vLLM image: `vllm/vllm-openai:deepseekv4-cu130` - Model: `d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: DeepSeek-V4-Pro H200 DP+EP router dtype mismatch in topk_hash_softplus_sqrt (Long/Int inconsistency) bug;DSv4 ### Your current environment Environment - vLLM image: `vllm/vllm-openai:deepseekv4-cu130` - Model: `d...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
