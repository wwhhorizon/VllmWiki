# vllm-project/vllm#32962: [Performance]: Custom Helion Kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#32962](https://github.com/vllm-project/vllm/issues/32962) |
| 状态 | open |
| 标签 | performance |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;gemm_linear;model_support;moe;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;fp8;kernel;moe;operator;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Custom Helion Kernels

### Issue 正文摘录

### Proposal to improve performance This is the sub issue from the vLLM Helion Integration Project https://github.com/vllm-project/vllm/issues/32219 proposed by @gmagogsfm. This issue lists down vLLM kernels that are good candidates to explore, implement, and benchmark with Helion. The progress and results will be tracked here. ### Scope ### * This Issue focuses on kernels integrated into vLLM via the [CustomOp](https://docs.vllm.ai/en/latest/design/custom_op/) framework (potentially getting replaced by the new vLLM IR framework, https://github.com/vllm-project/vllm/issues/32358) * Attention kernels are intentionally out of scope, since they are integrated through a different mechanism and are tracked separately, https://github.com/vllm-project/vllm/pull/27293. * For fused kernels, we only consider those already present in vLLM. A separate list of proposed new fusions exists and is tracked in https://github.com/vllm-project/vllm/issues/25179; those are out of scope for now. * We will start with common, broadly used kernels. Kernels specific to certain model architectures or features (e.g., MoE, LoRA) are out of scope for now. ### Kernels ### #### Linear #### - [x] scaled_mm - Trac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e for now. * We will start with common, broadly used kernels. Kernels specific to certain model architectures or features (e.g., MoE, LoRA) are out of scope for now. ### Kernels ### #### Linear #### - [x] scaled_mm - Tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: nally out of scope, since they are integrated through a different mechanism and are tracked separately, https://github.com/vllm-project/vllm/pull/27293. * For fused kernels, we only consider those already present in vLL...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: ts down vLLM kernels that are good candidates to explore, implement, and benchmark with Helion. The progress and results will be tracked here. ### Scope ### * This Issue focuses on kernels integrated into vLLM via the [...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: LoRA) are out of scope for now. ### Kernels ### #### Linear #### - [x] scaled_mm - Tracked in https://github.com/vllm-project/vllm/pull/33651 - [x] scaled_mm_blockwise - Tracked in https://github.com/vllm-project/vllm/p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: h.compile (H100) | Speedup against torch.ops._C (H100) | Speedup against CUTLASS (H100) | Speedup against torch.compile (B200) | Speedup against torch.ops._C (B200) | Speedup against CUTLASS (B200) | |---|---:|---:|---:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
