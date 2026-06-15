# vllm-project/vllm#39636: [Feature]: Add validation script and coverage analysis for FusedMoE tuning configs

| 字段 | 值 |
| --- | --- |
| Issue | [#39636](https://github.com/vllm-project/vllm/issues/39636) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add validation script and coverage analysis for FusedMoE tuning configs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Motivation The FusedMoE kernel has per-GPU tuning configs in JSON files under `vllm/model_executor/layers/fused_moe/configs/`. Currently there is no automated way to: - Validate that config files have correct keys and value ranges - Identify which GPU × model × dtype combinations lack configs - Detect obviously suboptimal parameters (e.g. num_warps not a power of 2) Following the FusedMoE refactor (#36286), validation tooling helps ensure config quality and completeness. ## Proposed Change 1. A validation script (`benchmarks/kernels/validate_moe_configs.py`) runnable without a GPU that audits all JSON configs 2. Schema validation (required keys, value ranges) 3. Coverage summary table (GPU × expert_config × dtype) 4. CI-friendly exit codes (0 = valid, 1 = errors found) ## Related - FusedMoE refactor: #36286 - Mamba tuning infrastructure: #33034 - Q1 2026 Roadmap: #32455 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/la...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: eature]: Add validation script and coverage analysis for FusedMoE tuning configs feature request ### 🚀 The feature, motivation and pitch ## Motivation The FusedMoE kernel has per-GPU tuning configs in JSON files under `...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: Add validation script and coverage analysis for FusedMoE tuning configs feature request ### 🚀 The feature, motivation and pitch ## Motivation The FusedMoE kernel has per-GPU tuning configs in JSON files under...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: quality and completeness. ## Proposed Change 1. A validation script (`benchmarks/kernels/validate_moe_configs.py`) runnable without a GPU that audits all JSON configs 2. Schema validation (required keys, value ranges) 3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: value ranges) 3. Coverage summary table (GPU × expert_config × dtype) 4. CI-friendly exit codes (0 = valid, 1 = errors found) ## Related - FusedMoE refactor: #36286 - Mamba tuning infrastructure: #33034 - Q1 2026 Roadma...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: files have correct keys and value ranges - Identify which GPU × model × dtype combinations lack configs - Detect obviously suboptimal parameters (e.g. num_warps not a power of 2) Following the FusedMoE refactor (#36286)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
