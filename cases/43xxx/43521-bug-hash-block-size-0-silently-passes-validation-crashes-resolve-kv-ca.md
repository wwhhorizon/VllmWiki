# vllm-project/vllm#43521: [Bug]: --hash-block-size 0 silently passes validation, crashes resolve_kv_cache_block_sizes with ZeroDivisionError

| 字段 | 值 |
| --- | --- |
| Issue | [#43521](https://github.com/vllm-project/vllm/issues/43521) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: --hash-block-size 0 silently passes validation, crashes resolve_kv_cache_block_sizes with ZeroDivisionError

### Issue 正文摘录

### Your current environment OS : macOS 26.5 (arm64) Python : 3.12.11 PyTorch : 2.11.0 vLLM : 0.1.dev1+g4438b6e7d (git sha: 4438b6e7d, matches current main) Transformers : 5.9.0 Built from source via VLLM_TARGET_DEVICE=empty pip install -e . against pinned upstream commit 4438b6e7d. The bug is in pure-Python config/ KV-cache resolver code; no kernel build needed. ### 🐛 Describe the bug `--hash-block-size 0` is accepted by argparse, passes through `CacheConfig` (which uses `SkipValidation[int]`), and crashes engine init with `ZeroDivisionError` at `vllm/v1/core/kv_cache_utils.py:628` (`bs % hash_block_size` in `resolve_kv_cache_block_sizes`). The adjacent `Invalid hash_block_size=…` `ValueError` two lines later is never reached. Same shape as #43496; same one-line fix shape as #43514. ## Reproduction Reachable for multi-group KV caches (hybrid Mamba+Attention models — Falcon-Mamba, RecurrentGemma, Zamba) with `--enable-prefix-caching` or a KV transfer connector. Single-group setups early-return at `kv_cache_utils.py:577`. Minimal isolated reproducer (exercises the crash site without model loading): ```python from unittest.mock import MagicMock import vllm.v1.core.kv_cache_utils as...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ansformers : 5.9.0 Built from source via VLLM_TARGET_DEVICE=empty pip install -e . against pinned upstream commit 4438b6e7d. The bug is in pure-Python config/ KV-cache resolver code; no kernel build needed. ### 🐛 Descri...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: -e . against pinned upstream commit 4438b6e7d. The bug is in pure-Python config/ KV-cache resolver code; no kernel build needed. ### 🐛 Describe the bug `--hash-block-size 0` is accepted by argparse, passes through `Cach...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ut cfg.cache_config.enable_prefix_caching = True cfg.parallel_config.decode_context_parallel_size = 1 cfg.parallel_config.prefill_context_parallel_size = 1 cfg.kv_transfer_config = None kvu.resolve_kv_cache_block_sizes(...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: inst pinned upstream commit 4438b6e7d. The bug is in pure-Python config/ KV-cache resolver code; no kernel build needed. ### 🐛 Describe the bug `--hash-block-size 0` is accepted by argparse, passes through `CacheConfig`...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: roup setups early-return at `kv_cache_utils.py:577`. Minimal isolated reproducer (exercises the crash site without model loading): ```python from unittest.mock import MagicMock import vllm.v1.core.kv_cache_utils as kvu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
