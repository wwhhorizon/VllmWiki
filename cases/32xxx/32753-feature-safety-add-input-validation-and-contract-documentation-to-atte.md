# vllm-project/vllm#32753: [Feature]: ​[Safety] Add input validation and contract documentation to attention kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#32753](https://github.com/vllm-project/vllm/issues/32753) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api |
| 子分类 | shape_align |
| Operator 关键词 | attention;cuda;kernel;operator |
| 症状 | mismatch |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: ​[Safety] Add input validation and contract documentation to attention kernels

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [Safety] Add input validation and contract documentation to attention kernels Body: The Problem: Silent Contract Violations Current attention kernels assume perfect inputs, but real deployments frequently encounter: * Mis-shaped tensors from user code * Incorrect strides from view/transpose operations * Device mismatches in heterogeneous environments * Out-of-bounds values in seq_lens or block_tables When these violate kernel assumptions, the failures are: * Silent (computation proceeds with wrong memory addresses) * Cryptic (CUDA illegal memory access with no stack trace) * Hard to debug (no context on which tensor caused the issue) Proposed Solution: Defense at the Interface 1. Explicit Contract Documentation Move implicit assumptions into explicit code contracts. // BEFORE: Nothing // AFTER: // CONTRACT: // - `query` must be contiguous or have stride [q_stride, head_size, 1] // - `block_tables` device must match `key_cache` device // - `head_size` must be multiple of 16 (for vectorized loads) 2. Runtime Validation Strategy I propose a tiered validation approach to balance safety and performance: Tier 1: Lightweight Checks (Always On) Chec...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: frequently encounter: * Mis-shaped tensors from user code * Incorrect strides from view/transpose operations * Device mismatches in heterogeneous environments * Out-of-bounds values in seq_lens or block_tables When thes...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ser code * Incorrect strides from view/transpose operations * Device mismatches in heterogeneous environments * Out-of-bounds values in seq_lens or block_tables When these violate kernel assumptions, the failures are: *...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 2 checks will be strictly optional/conditional, ensuring no performance regression in the hot path for production workloads. I can implement Phase 1 as a starting point if this direction aligns with the project's goals....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: user code * Incorrect strides from view/transpose operations * Device mismatches in heterogeneous environments * Out-of-bounds values in seq_lens or block_tables When these violate kernel assumptions, the failures are:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: or caused the issue) Proposed Solution: Defense at the Interface 1. Explicit Contract Documentation Move implicit assumptions into explicit code contracts. // BEFORE: Nothing // AFTER: // CONTRACT: // - `query` must be...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
