# vllm-project/vllm#43496: [Bug]: --block-size 0 silently passes validation, crashes engine init with ZeroDivisionError

| 字段 | 值 |
| --- | --- |
| Issue | [#43496](https://github.com/vllm-project/vllm/issues/43496) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cache;cuda;kernel |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --block-size 0 silently passes validation, crashes engine init with ZeroDivisionError

### Issue 正文摘录

### Your current environment ### System Info OS : macOS 26.5 (arm64) GCC version : Could not collect Clang version : 21.0.0 (clang-2100.1.1.101) CMake version : version 4.3.2 Libc version : N/A ### PyTorch Info PyTorch version : 2.11.0 Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ### Python Environment Python version : 3.12.11 (main, Jun 3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)] (64-bit runtime) Python platform : macOS-26.5-arm64-arm-64bit ### CPU Info Apple M4 Pro ### Versions of relevant libraries [pip3] numpy==2.3.5 [pip3] pyzmq==27.1.0 [pip3] torch==2.11.0 [pip3] torchaudio==2.11.0 [pip3] torchvision==0.26.0 [pip3] transformers==5.9.0 ### vLLM Info vLLM Version : 0.1.dev1+g4438b6e7d (git sha: 4438b6e7d) vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; XPU: Disabled GPU Topology: Could not collect ### Environment Variables PYTORCH_NVML_BASED_CUDA_CHECK=1 TORCHINDUCTOR_COMPILE_THREADS=1 TORCHINDUCTOR_CACHE_DIR=/var/folders/.../T/torchinductor_ Notes: - Built from source via VLLM_TARGET_DEVICE=empty pip install -e . against pinned upstream commit 4438b6e (Python-only install — the bug is...

## 现有链接修复摘要

#43514 [Bugfix] Reject non-positive block_size in CacheConfig | #43524 [Bugfix] Reject non-positive/non-int hash_block_size in CacheConfig | #43623 [Bugfix] Reject invalid block_size, hash_block_size, and max_model_len

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ## System Info OS : macOS 26.5 (arm64) GCC version : Could not collect Clang version : 21.0.0 (clang-2100.1.1.101) CMake version : version 4.3.2 Libc version : N/A ### PyTorch Info PyTorch ve
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 6: [Bug]: --block-size 0 silently passes validation, crashes engine init with ZeroDivisionError bug ### Your current environment ### System Info OS : macOS 26.5 (arm64) GCC version : C
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: h version : 2.11.0 Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ### Python Environment Python version : 3.12.11 (main, Jun 3 2025, 15:41:47) [...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: llm/v1/kv_cache_interface.py:218` | `KVCacheSpec.max_memory_usage_bytes` evaluates `cdiv(max_model_len, self.block_size) * page_size_bytes`. `cdiv(N, 0)` is `-(N // -0)`, which raises `ZeroDivisionError`. Traceback abov...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: = FullAttentionSpec( block_size=0, num_kv_heads=12, head_size=64, dtype=torch.float16, ) max_model_len = 2048 cdiv(max_model_len, spec.block_size) * spec.page_size_bytes ``` Output: ```text Traceback (most recent call l...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43514](https://github.com/vllm-project/vllm/pull/43514) | closes_keyword | 0.95 | [Bugfix] Reject non-positive block_size in CacheConfig | Fixes #43496. `--block-size 0` (and equivalently `LLM(block_size=0)`) silently passed argparse and `CacheConfig` validation, then crashed engine init with a `ZeroDivisionError` in |
| [#43524](https://github.com/vllm-project/vllm/pull/43524) | mentioned | 0.6 | [Bugfix] Reject non-positive/non-int hash_block_size in CacheConfig | refix-caching` or a KV transfer connector. This is the same shape as #43496 (block_size=0), reported by the same ESBMC-Python formal-verification harness author. The fix follows t… |
| [#43623](https://github.com/vllm-project/vllm/pull/43623) | closes_keyword | 0.95 | [Bugfix] Reject invalid block_size, hash_block_size, and max_model_len | Fixes #43496, #43521, and #43532. - Reject non-positive or non-integer `block_size` and `hash_block_size` in `CacheConfig._apply_block_size_default` so users get a clear `ValueErr |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
