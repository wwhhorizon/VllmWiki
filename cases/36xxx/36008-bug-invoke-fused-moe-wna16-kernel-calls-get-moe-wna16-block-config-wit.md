# vllm-project/vllm#36008: [Bug]: invoke_fused_moe_wna16_*_kernel calls get_moe_wna16_block_config with bad parameters

| 字段 | 值 |
| --- | --- |
| Issue | [#36008](https://github.com/vllm-project/vllm/issues/36008) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | moe;sampling_logits |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;kernel;moe;sampling |
| 症状 | crash |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: invoke_fused_moe_wna16_*_kernel calls get_moe_wna16_block_config with bad parameters

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### [Bug] CUDA `moe_wna16_gemm` crash due to invalid `BLOCK_SIZE_K` configuration **Description** The CUDA `moe_wna16_gemm` kernel requires the ratio of `BLOCK_SIZE_K // group_size` to be within the set `{1, 2, 4, 8}`. However, the heuristic in `get_moe_wna16_block_config` can produce a `BLOCK_SIZE_K` that exceeds this limit (e.g., $512 / 32 = 16$), leading to a runtime crash. After careful examination, the root cause is identified. `num_experts` is erroneously passed as `B.size(1)` (Output dimension $N$) instead of `B.size(0)` (Expert dimension $E$) in the block configuration logic, which further distorts the block estimation. **Error Message** ```text RuntimeError: BLOCK_SIZE_K // group_size must be one of [1, 2, 4, 8] ``` **Proposed Fix** 1. Correct `num_experts` to use `B.size(0)` in `invoke_fused_moe_wna16_cuda_kernel`. 2. Correct `num_experts` to use `B.size(0)` in `invoke_fused_moe_wna16_triton_kernel`. 3. Add a clamp in `get_moe_wna16_block_config` to force a `max_block_size_k = group_size * 8` when `use_moe_wna16_cuda=True`. --- [https://github.com/vllm-project/vllm/blob/bb6888b8b1a03e683ff4ed5f1fb6df5a0582fd6f/vllm/mode...

## 现有链接修复摘要

#36026 [Bugfix] Fix wrong num_experts in invoke_fused_moe_wna16 kernels

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: invoke_fused_moe_wna16_*_kernel calls get_moe_wna16_block_config with bad parameters bug ### Your current environment ### 🐛 Describe the bug ### [Bug] CUDA `moe_wna16_gemm` crash due to invalid `BLOCK_SIZE_K` con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s bug ### Your current environment ### 🐛 Describe the bug ### [Bug] CUDA `moe_wna16_gemm` crash due to invalid `BLOCK_SIZE_K` configuration **Description** The CUDA `moe_wna16_gemm` kernel requires the ratio of `BLOCK_S...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: invoke_fused_moe_wna16_*_kernel calls get_moe_wna16_block_config with bad parameters bug ### Your current environment ### 🐛 Describe the bug ### [Bug] CUDA `moe_wna16_gemm` crash due to invalid `BLOCK_SIZE_K` con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: invoke_fused_moe_wna16_*_kernel calls get_moe_wna16_block_config with bad parameters bug ### Your current environment ### 🐛 Describe the bug ### [Bug] CUDA `moe_wna16_gemm` crash due to invalid `BLOCK_SIZE_K` con...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: . 2. Correct `num_experts` to use `B.size(0)` in `invoke_fused_moe_wna16_triton_kernel`. 3. Add a clamp in `get_moe_wna16_block_config` to force a `max_block_size_k = group_size * 8` when `use_moe_wna16_cuda=True`. ---...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36026](https://github.com/vllm-project/vllm/pull/36026) | closes_keyword | 0.95 | [Bugfix] Fix wrong num_experts in invoke_fused_moe_wna16 kernels | Fixes #36008 ## Test plan - The fix is a straightforward parameter correction (dimension 1 → dimension 0) with no behavioral change for correctly-shaped inputs - Verified that te |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
