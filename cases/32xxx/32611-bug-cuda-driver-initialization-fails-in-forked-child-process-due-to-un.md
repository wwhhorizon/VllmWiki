# vllm-project/vllm#32611: [Bug]: CUDA driver initialization fails in forked child process due to undetected cuInit() call from pynvml

| 字段 | 值 |
| --- | --- |
| Issue | [#32611](https://github.com/vllm-project/vllm/issues/32611) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA driver initialization fails in forked child process due to undetected cuInit() call from pynvml

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Your current environment - vLLM version: 0.14.0rc2.dev148+gaa7f37ccf - PyTorch version: 2.9.1+cu130 - CUDA version: 13.0 (Driver 580.126.09) - Python version: 3.12.12 - OS: Ubuntu Linux (x86_64) - GPU: NVIDIA RTX A6000 x8 ## Describe the bug When using vLLM with the default `fork` multiprocessing method (`VLLM_WORKER_MULTIPROC_METHOD=fork`), the EngineCore child process fails to initialize CUDA with the error: ``` RuntimeError: CUDA driver initialization failed, you might not have a CUDA gpu. ``` This happens even though: - `nvidia-smi` shows all GPUs are available - `torch.cuda.is_available()` returns `True` - `torch.cuda.is_initialized()` returns `False` before forking ## Root Cause Analysis The issue is caused by **pynvml initializing the CUDA driver** before the fork, but this initialization is **not detected** by vLLM's `_maybe_force_spawn()` function. ### Proof of root cause: ```python import ctypes import multiprocessing # Calling cuInit() before fork (simulating what pynvml does) cuda = ctypes.CDLL('libcuda.so.1') result = cuda.cuInit(0) print('Parent: cuInit result:', result) # Returns 0 (success) def test_cuda_in_chi...

## 现有链接修复摘要

#44252 [Bugfix] Detect driver-level CUDA init before fork

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ironment ### 🐛 Describe the bug ## Your current environment - vLLM version: 0.14.0rc2.dev148+gaa7f37ccf - PyTorch version: 2.9.1+cu130 - CUDA version: 13.0 (Driver 580.126.09) - Python version: 3.12.12 - OS: Ubuntu Linu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUDA driver initialization fails in forked child process due to undetected cuInit() call from pynvml bug ### Your current environment ### 🐛 Describe the bug ## Your current environment - vLLM version: 0.14.0rc2.d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency #44252 [Bugfix] Detect driver-level CUDA init before fork Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: /__init__.py` - Any other library calls `cuInit()` directly ## Steps to reproduce ```python # test_vllm_fork_bug.py from vllm import LLM model_path = "any-valid-model-path" llm = LLM(model=model_path, trust_remote_code=...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s_available()` returns `True` - `torch.cuda.is_initialized()` returns `False` before forking ## Root Cause Analysis The issue is caused by **pynvml initializing the CUDA driver** before the fork, but this initialization...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#44252](https://github.com/vllm-project/vllm/pull/44252) | closes_keyword | 0.95 | [Bugfix] Detect driver-level CUDA init before fork | Fixes #32611 ## Purpose `_maybe_force_spawn()` currently decides whether to avoid `fork` from `torch.cuda.is_initialized()`. That misses a real case from #32611: a parent pro |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
