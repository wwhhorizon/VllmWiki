# vllm-project/vllm#44210: [Bug]: DeepSeek-V4 initialization fails with AttributeError: module 'cutlass.cute.arch' has no attribute 'fmin'

| 字段 | 值 |
| --- | --- |
| Issue | [#44210](https://github.com/vllm-project/vllm/issues/44210) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | gemm_linear;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V4 initialization fails with AttributeError: module 'cutlass.cute.arch' has no attribute 'fmin'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to run the DeepSeek-V4-Flash model on an H100 node with CUDA 12.9, the engine fails to start and all workers crash during the CUDA graph profiling/warmup phase. The root cause is an AttributeError thrown during the JIT compilation of the TileLang/CUTLASS kernel (mhc_pre_big_fuse_with_norm_tilelang). Specifically, the code in sparse_attn_compress_cutedsl.py attempts to call cute.arch.fmin, which does not exist in the installed version of the nvidia-cutlass-dsl library. Error Logs ```Bash (Worker_DP6_EP6 pid=4848) ERROR 06-01 12:34:00 [multiproc_executor.py:962] File "/usr/local/lib/python3.12/dist-packages/vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py", line 290, in then_block_21 (Worker_DP6_EP6 pid=4848) ERROR 06-01 12:34:00 [multiproc_executor.py:962] if warp_id == self.nope_blocks: # ... [skipping some AST executor traces] ... (Worker_DP6_EP6 pid=4848) ERROR 06-01 12:34:00 [multiproc_executor.py:962] File "/usr/local/lib/python3.12/dist-packages/vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py", line 323, in else_block_16 (Worker_DP6_EP6 pid=4848) ERROR 06-01 12:34:00 [mult...

## 现有链接修复摘要

#44225 fix: resolve issue #44210 — [Bug]: DeepSeek-V4 initialization fails with AttributeError: | #44236 fix: resolve CUTLASS fmin compatibility for DeepSeek-V4 init

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: of the TileLang/CUTLASS kernel (mhc_pre_big_fuse_with_norm_tilelang). Specifically, the code in sparse_attn_compress_cutedsl.py attempts to call cute.arch.fmin, which does not exist in the installed version of the nvidi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: epSeek-V4 initialization fails with AttributeError: module 'cutlass.cute.arch' has no attribute 'fmin' bug ### Your current environment ### 🐛 Describe the bug When attempting to run the DeepSeek-V4-Flash model on an H10...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: epseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py", line 290, in then_block_21 (Worker_DP6_EP6 pid=4848) ERROR 06-01 12:34:00 [multiproc_executor.py:962] if warp_id == self.nope_blocks: # ... [skipping some AST execu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 9, the engine fails to start and all workers crash during the CUDA graph profiling/warmup phase. The root cause is an AttributeError thrown during the JIT compilation of the TileLang/CUTLASS kernel (mhc_pre_big_fuse_wit...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: DeepSeek-V4 initialization fails with AttributeError: module 'cutlass.cute.arch' has no attribute 'fmin' bug ### Your current environment ### 🐛 Describe the bug When attempting to run the DeepSeek-V4-Flash model...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#44225](https://github.com/vllm-project/vllm/pull/44225) | closes_keyword | 0.95 | fix: resolve issue #44210 — [Bug]: DeepSeek-V4 initialization fails with AttributeError: | Fixes #44210 This PR resolves the reported issue: **[Bug]: DeepSeek-V4 initialization fails with AttributeError: module 'cutlass.cute.arch' has no attribute 'fmin'** Changes were |
| [#44236](https://github.com/vllm-project/vllm/pull/44236) | closes_keyword | 0.95 | fix: resolve CUTLASS fmin compatibility for DeepSeek-V4 init | Fixes #44210 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
