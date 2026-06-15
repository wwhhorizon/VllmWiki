# vllm-project/vllm#35089: [RFC]: In-Tree AMD Zen CPU Backend via zentorch

| 字段 | 值 |
| --- | --- |
| Issue | [#35089](https://github.com/vllm-project/vllm/issues/35089) |
| 状态 | closed |
| 标签 | rocm;RFC;stale;cpu |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;gemm_linear;hardware_porting;model_support |
| 子分类 | throughput |
| Operator 关键词 | activation;cuda;gemm;kernel;operator |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: In-Tree AMD Zen CPU Backend via zentorch

### Issue 正文摘录

### Motivation. - Provide first-class AMD Zen CPU path under vLLM platform selection. - Keep vLLM-facing logic in-tree (detection, dispatch, pass orchestration). - Support both freezing modes: enabled and disabled controlled via `TORCHINDUCTOR_FREEZING` - Port only the minimum optimization surface required for LLM inference from [`zentorch`](https://github.com/amd/ZenDNN-pytorch-plugin). - Maintain feature and performance parity (~10%) with the out of tree plugin. ### Proposed Change. ## Summary This RFC proposes an in-tree Zen CPU backend in vLLM that keeps orchestration in vLLM and uses zentorch only for kernel/ops implementation. The design has four parts: 1. Platform detection and configuration via `ZenCpuPlatform` (PyTorch backports, Inductor pass injection). 2. Runtime linear dispatch to `torch.ops.zentorch.zentorch_linear_unary` when `ZenCpuPlatform` is active, with optional eager weight prepacking controlled via `VLLM_ZENTORCH_WEIGHT_PREPACK`. 3. Compile-time graph passes via `ZenOptimizePass`: embedding replacement (`aten.embedding` -> `zentorch.zentorch_embedding`) and 11 post-op fusion patterns (binary-binary, unary-binary, unary) applied in sequence. 4. Use `CustomOps`...

## 现有链接修复摘要

#35970 In-Tree AMD Zen CPU Backend via zentorch [1/N]

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: irst-class AMD Zen CPU path under vLLM platform selection. - Keep vLLM-facing logic in-tree (detection, dispatch, pass orchestration). - Support both freezing modes: enabled and disabled controlled via `TORCHINDUCTOR_FR...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [RFC]: In-Tree AMD Zen CPU Backend via zentorch rocm;RFC;stale;cpu ### Motivation. - Provide first-class AMD Zen CPU path under vLLM platform selection. - Keep vLLM-facing logic in-tree (detection, dispatch, pass orches...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [RFC]: In-Tree AMD Zen CPU Backend via zentorch rocm;RFC;stale;cpu ### Motivation. - Provide first-class AMD Zen CPU path under vLLM platform selection. - Keep vLLM-facing logic in-tree (detection, dispatch, pass orches...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: x, residual, self.weight.data, self.variance_epsilon ) else: return rms_norm(x, self.weight.data, self.variance_epsilon) ``` This is identical to the existing `forward_cuda` implementation. The `rms_norm` and `fused_add...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: s implementation. The design has four parts: 1. Platform detection and configuration via `ZenCpuPlatform` (PyTorch backports, Inductor pass injection). 2. Runtime linear dispatch to `torch.ops.zentorch.zentorch_linear_u...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35970](https://github.com/vllm-project/vllm/pull/35970) | mentioned | 0.6 | In-Tree AMD Zen CPU Backend via zentorch [1/N] | orm detection, GEMM dispatch, and Dockerfile targets described in RFC #35089. Fusion passes and other optimizations will follow in subsequent PRs. - Introduces `ZenCpuPlatform`, a… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
