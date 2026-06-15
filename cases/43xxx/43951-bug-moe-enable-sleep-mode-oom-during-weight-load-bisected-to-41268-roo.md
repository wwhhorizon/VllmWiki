# vllm-project/vllm#43951: [Bug]: MoE + --enable-sleep-mode OOM during weight load — bisected to #41268, root cause in cumem MemPool reclaim (pytorch#159674)

| 字段 | 值 |
| --- | --- |
| Issue | [#43951](https://github.com/vllm-project/vllm/issues/43951) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;moe;operator;quantization |
| 症状 | crash;oom |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: MoE + --enable-sleep-mode OOM during weight load — bisected to #41268, root cause in cumem MemPool reclaim (pytorch#159674)

### Issue 正文摘录

### Your current environment - vLLM: `0.21.0` (also reproduced on 0.21.x). Clean on `0.18.0 / 0.19.1 / 0.20.0 / 0.20.1 / 0.20.2`. - GPU: 4x NVIDIA GB200 (184 GiB), TP=4. Also matches the single-H100 report in #34877. - Model: `Qwen3-235B-A22B-Instruct-2507` (128-expert MoE), `--enable-sleep-mode`, `--gpu-memory-utilization 0.93 --max-num-seqs 1024`. ### 🐛 Describe the bug Loading a large MoE model with `--enable-sleep-mode` OOMs **during weight loading** (the per-expert FlashInfer/TRTLLM block-layout swizzle), at `csrc/cumem_allocator.cpp`. `Profiling CUDA graph memory` is never reached. ``` torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB. GPU 3 has a total capacity of 184.31 GiB of which 21.50 MiB is free. ... 181.80 GiB is allocated by PyTorch, with 71.20 GiB allocated in private pools (e.g., CUDA Graphs), and 13.63 MiB is reserved by PyTorch but unallocated. ``` The traceback points at `convert_moe_weights_to_flashinfer_trtllm_block_layout`. **This is the same root cause as #34877** (gpt-oss-120b mxfp4 swizzle, single H100, sleep mode) — same `cumem_allocator.cpp` OOM signature, same ~70 GiB stranded private pool. ### Bisection (5 clean / 3 OOM, 4 distin...

## 现有链接修复摘要

#41268 [UX][Bugfix] Fix OOM by setting PyTorch `max_split_size_mb` during model loading

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: : CUDA out of memory. Tried to allocate 20.00 MiB. GPU 3 has a total capacity of 184.31 GiB of which 21.50 MiB is free. ... 181.80 GiB is allocated by PyTorch, with 71.20 GiB allocated in private pools (e.g., CUDA Graph...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Clean on `0.18.0 / 0.19.1 / 0.20.0 / 0.20.1 / 0.20.2`. - GPU: 4x NVIDIA GB200 (184 GiB), TP=4. Also matches the single-H100 report in #34877. - Model: `Qwen3-235B-A22B-Instruct-2507` (128-expert MoE), `--enable-sleep-mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: GB200 (184 GiB), TP=4. Also matches the single-H100 report in #34877. - Model: `Qwen3-235B-A22B-Instruct-2507` (128-expert MoE), `--enable-sleep-mode`, `--gpu-memory-utilization 0.93 --max-num-seqs 1024`. ### 🐛 Describe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: m_block_layout`. **This is the same root cause as #34877** (gpt-oss-120b mxfp4 swizzle, single H100, sleep mode) — same `cumem_allocator.cpp` OOM signature, same ~70 GiB stranded private pool. ### Bisection (5 clean / 3...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: p-mode` OOMs **during weight loading** (the per-expert FlashInfer/TRTLLM block-layout swizzle), at `csrc/cumem_allocator.cpp`. `Profiling CUDA graph memory` is never reached. ``` torch.OutOfMemoryError: CUDA out of memo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41268](https://github.com/vllm-project/vllm/pull/41268) | mentioned | 0.45 | [UX][Bugfix] Fix OOM by setting PyTorch `max_split_size_mb` during model loading | lated - #34877 — same root cause (gpt-oss-120b mxfp4, single h100) - #41268 — the pr that introduced the regression for moe - pytorch/pytorch#159674 (open) — mempool no reclaim-on… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
