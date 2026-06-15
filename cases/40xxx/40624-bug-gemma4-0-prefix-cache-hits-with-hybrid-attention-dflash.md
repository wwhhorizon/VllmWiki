# vllm-project/vllm#40624: [Bug]: Gemma4 0% prefix cache hits with hybrid attention + DFlash

| 字段 | 值 |
| --- | --- |
| Issue | [#40624](https://github.com/vllm-project/vllm/issues/40624) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma4 0% prefix cache hits with hybrid attention + DFlash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Gemma4 + DFlash speculative decoding produces **0% prefix cache hit rates** when the hybrid KV cache manager is enabled. This is the same EAGLE spiral block-dropping bug as #32802, which was partially fixed by #33524 — but the fix's `is_simple_hybrid` guard does not cover the Gemma4 + DFlash case. ```bash # Eval script used python tests/evals/gsm8k/gsm8k_eval.py # With DFlash: 0% prefix cache hit rate vllm serve RedHatAI/gemma-4-31B-it-speculator.dflash -tp 2 --attention-backend FLASH_ATTN # Prefix cache hit rate: 0.0% # Without DFlash: ~80% hit rate as expected vllm serve google/gemma-4-31B-it -tp 2 --attention-backend FLASH_ATTN # Prefix cache hit rate: 91.1% # Workaround: disable hybrid KV cache manager vllm serve RedHatAI/gemma-4-31B-it-speculator.dflash \ -tp 2 \ --attention-backend FLASH_ATTN \ --disable-hybrid-kv-cache-manager \ --max-model-len 40000 # Prefix cache hit rate: ~88.9% # max model length required to get model to fit on H100 ``` ### Root Cause The DFlash draft model (Qwen3-based) adds its own attention layers to the model. `get_kv_cache_spec()` (`gpu_model_runner.py:6887`) scans ALL attention layers — both the...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: en the hybrid KV cache manager is enabled. This is the same EAGLE spiral block-dropping bug as #32802, which was partially fixed by #33524 — but the fix's `is_simple_hybrid` guard does not cover the Gemma4 + DFlash case...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma4 0% prefix cache hits with hybrid attention + DFlash bug ### Your current environment ### 🐛 Describe the bug Gemma4 + DFlash speculative decoding produces **0% prefix cache hit rates** when the hybrid KV ca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: he Gemma4 + DFlash case. ```bash # Eval script used python tests/evals/gsm8k/gsm8k_eval.py # With DFlash: 0% prefix cache hit rate vllm serve RedHatAI/gemma-4-31B-it-speculator.dflash -tp 2 --attention-backend FLASH_ATT...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: Gemma4 0% prefix cache hits with hybrid attention + DFlash bug ### Your current environment ### 🐛 Describe the bug Gemma4 + DFlash speculative decoding produces **0% prefix cache hit rates** when the hybrid KV ca...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ### Your current environment ### 🐛 Describe the bug Gemma4 + DFlash speculative decoding produces **0% prefix cache hit rates** when the hybrid KV cache manager is enabled. This is the same EAGLE spiral block-dropping b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
