# vllm-project/vllm#43532: [Bug]: --max-model-len 0 silently accepted; engine starts cleanly, requests scheduled with negative num_new_tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#43532](https://github.com/vllm-project/vllm/issues/43532) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: --max-model-len 0 silently accepted; engine starts cleanly, requests scheduled with negative num_new_tokens

### Issue 正文摘录

### Your current environment OS : macOS 26.5 (arm64) Python : 3.12.11 PyTorch : 2.11.0 vLLM : 0.1.dev1+g4438b6e7d (git sha: 4438b6e7d, matches current main) Transformers : 5.9.0 Built from source via VLLM_TARGET_DEVICE=empty pip install -e . against pinned upstream commit 4438b6e7d. The bug is in pure-Python config / scheduler arithmetic; no kernel build needed. ### 🐛 Describe the bug `--max-model-len 0` is silently accepted by the entire config-validation chain. `ModelConfig` keeps the field as `0` after `__post_init__` and the engine even logs **`Using max model len 0`** as if it's a valid configuration. The 0 then reaches`vllm/v1/core/sched/scheduler.py:397`: ```python num_new_tokens = min(num_new_tokens, self.max_model_len - 1 - request.num_computed_tokens) ``` For a fresh request (`num_computed_tokens = 0`), the rhs is `-1`, so `num_new_tokens` becomes negative. It passes the `if num_new_tokens == 0:` early-return at line 425 (it's `-1`, not `0`), flows into `kv_cache_manager.allocate_slots`, and reaches `cdiv(-1, block_size) = 0`, which returns 0 silently, not raises. The engine schedules the request with negative tokens and zero KV-cache blocks. Same bug *class* as #43521 /...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Transformers : 5.9.0 Built from source via VLLM_TARGET_DEVICE=empty pip install -e . against pinned upstream commit 4438b6e7d. The bug is in pure-Python config / scheduler arithmetic; no kernel build needed. ### 🐛 Descr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `: ```python @field_validator("max_model_len", mode="after") @classmethod def _check_positive_or_sentinel(cls, v): if v is None or v == -1: return v if v <= 0: raise ValueError( f"max_model_len must be a positive intege...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: t raises. The engine schedules the request with negative tokens and zero KV-cache blocks. Same bug *class* as #43521 / #43496 (CLI int param with insufficient validation flowing into arithmetic), but a strictly more dan...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: at line 425 (it's `-1`, not `0`), flows into `kv_cache_manager.allocate_slots`, and reaches `cdiv(-1, block_size) = 0`, which returns 0 silently, not raises. The engine schedules the request with negative tokens and zer...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: --max-model-len 0 silently accepted; engine starts cleanly, requests scheduled with negative num_new_tokens bug ### Your current environment OS : macOS 26.5 (arm64) Python : 3.12.11 PyTorch : 2.1

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
