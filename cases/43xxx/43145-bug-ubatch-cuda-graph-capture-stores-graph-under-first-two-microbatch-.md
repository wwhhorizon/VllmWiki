# vllm-project/vllm#43145: [Bug]: UBatch CUDA graph capture stores graph under first-two-microbatch token count when ubatch_size > 2

| 字段 | 值 |
| --- | --- |
| Issue | [#43145](https://github.com/vllm-project/vllm/issues/43145) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;kernel;moe |
| 症状 | build_error;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: UBatch CUDA graph capture stores graph under first-two-microbatch token count when ubatch_size > 2

### Issue 正文摘录

### Summary When `ubatch_size > 2` and FULL CUDA graph capture is active, `UBatchWrapper.__call__()` uses the total token count across all ubatches as the graph cache lookup key, but `_capture_ubatches()` stores the captured graph under the sum of only `ubatch_metadata[0]` and `ubatch_metadata[1]`. This causes captured graphs to be stored under the wrong key for 3+ microbatches. ### Environment - vLLM commit: `12421962955ac28b6f80a0307f554fad939174dd` - vLLM version: `0.1.dev1+g124219629.d20260519` - OS: Ubuntu 24.04.4 LTS x86_64 - Python: 3.12.3 - PyTorch: `2.11.0+cu130` - CUDA used to build PyTorch: 13.0 - NVIDIA driver: 580.126.20 - GPU: NVIDIA A100-SXM4-40GB `vllm collect-env` was run. The A100 was later split into MIG `3g.20gb` instances only to run an isolated wrapper harness after the full server path was blocked. ### Reproducer I first tried to reproduce through `vllm serve` with current main plus logging instrumentation in `vllm/v1/worker/gpu_ubatch_wrapper.py`. `--ubatch-size` is user-visible: ```bash vllm serve --help=all | grep -i ubatch ``` Single-DP dense model attempt: ```bash VLLM_LOGGING_LEVEL=DEBUG vllm serve facebook/opt-125m \ --dtype half \ --max-model-len 102...

## 现有链接修复摘要

#43161 [Bugfix] Fix UBatchWrapper CUDA graph key to sum all ubatches, not just first two

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: onment - vLLM commit: `12421962955ac28b6f80a0307f554fad939174dd` - vLLM version: `0.1.dev1+g124219629.d20260519` - OS: Ubuntu 24.04.4 LTS x86_64 - Python: 3.12.3 - PyTorch: `2.11.0+cu130` - CUDA used to build PyTorch: 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: UBatch CUDA graph capture stores graph under first-two-microbatch token count when ubatch_size > 2 ### Summary When `ubatch_size > 2` and FULL CUDA graph capture is active, `UBatchWrapper.__call__()` uses the tot...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ture_ubatches()` stores the captured graph under the sum of only `ubatch_metadata[0]` and `ubatch_metadata[1]`. This causes captured graphs to be stored under the wrong key for 3+ microbatches. ### Environment - vLLM co...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: an isolated wrapper harness after the full server path was blocked. ### Reproducer I first tried to reproduce through `vllm serve` with current main plus logging instrumentation in `vllm/v1/worker/gpu_ubatch_wrapper.py`...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: le: ```bash vllm serve --help=all | grep -i ubatch ``` Single-DP dense model attempt: ```bash VLLM_LOGGING_LEVEL=DEBUG vllm serve facebook/opt-125m \ --dtype half \ --max-model-len 1024 \ --max-num-seqs 64 \ --max-num-b...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43161](https://github.com/vllm-project/vllm/pull/43161) | closes_keyword | 0.95 | [Bugfix] Fix UBatchWrapper CUDA graph key to sum all ubatches, not just first two | Fix CUDA graph cache miss in `UBatchWrapper._capture_ubatches()` when `ubatch_size > 2` (#43145). ## Test Plan Repro script that extracts the actual key formula from the inst |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
