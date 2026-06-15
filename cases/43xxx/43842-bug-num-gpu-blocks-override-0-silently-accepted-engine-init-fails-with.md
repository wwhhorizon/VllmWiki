# vllm-project/vllm#43842: [Bug]: `--num-gpu-blocks-override 0` silently accepted; engine init fails with bare `AssertionError` in `BlockPool.__init__`

| 字段 | 值 |
| --- | --- |
| Issue | [#43842](https://github.com/vllm-project/vllm/issues/43842) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `--num-gpu-blocks-override 0` silently accepted; engine init fails with bare `AssertionError` in `BlockPool.__init__`

### Issue 正文摘录

### Summary `--num-gpu-blocks-override 0` (and any non-positive value) passes through `CacheConfig` without validation. The override then replaces the profiled `num_gpu_blocks`, and `BlockPool.__init__` fails with a bare `AssertionError` (no message) at [`vllm/v1/core/block_pool.py:157`](../blob/main/vllm/v1/core/block_pool.py#L157). This is the same class of UX defect as #43496 / #43521 / #43532 (all recently closed by #43794), and has the same one-line fix shape. ### Repro (against current `main`, commit `6cc8577` at time of filing) ```python from unittest.mock import MagicMock from vllm.config.cache import CacheConfig from vllm.v1.core.kv_cache_utils import may_override_num_blocks from vllm.v1.core.block_pool import BlockPool # Step 1 — CacheConfig silently accepts 0 (and -1). assert CacheConfig(num_gpu_blocks_override=0).num_gpu_blocks_override == 0 assert CacheConfig(num_gpu_blocks_override=-1).num_gpu_blocks_override == -1 # Step 2 — the override replaces a positive profiled num_blocks. vllm_cfg = MagicMock() vllm_cfg.cache_config = CacheConfig(num_gpu_blocks_override=0) assert may_override_num_blocks(vllm_cfg, num_blocks=4096) == 0 # Step 3 — BlockPool asserts, with no usef...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: `--num-gpu-blocks-override 0` silently accepted; engine init fails with bare `AssertionError` in `BlockPool.__init__` ### Summary `--num-gpu-blocks-override 0` (and any non-positive value) passes through `CacheCo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: through `CacheConfig` without validation. The override then replaces the profiled `num_gpu_blocks`, and `BlockPool.__init__` fails with a bare `AssertionError` (no message) at [`vllm/v1/core/block_pool.py:157`](../blob/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: main`, commit `6cc8577` at time of filing) ```python from unittest.mock import MagicMock from vllm.config.cache import CacheConfig from vllm.v1.core.kv_cache_utils import may_override_num_blocks from vllm.v1.core.block_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: gpu-blocks-override 0` (and any non-positive value) passes through `CacheConfig` without validation. The override then replaces the profiled `num_gpu_blocks`, and `BlockPool.__init__` fails with a bare `AssertionError`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
