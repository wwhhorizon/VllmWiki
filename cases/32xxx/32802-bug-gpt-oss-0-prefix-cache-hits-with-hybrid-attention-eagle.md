# vllm-project/vllm#32802: [Bug]: GPT-OSS 0% prefix cache hits with hybrid attention + EAGLE

| 字段 | 值 |
| --- | --- |
| Issue | [#32802](https://github.com/vllm-project/vllm/issues/32802) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPT-OSS 0% prefix cache hits with hybrid attention + EAGLE

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash # Eval script used python tests/evals/gsm8k/gsm8k_eval.py # With EAGLE: 0% prefix cache hit rate vllm serve openai/gpt-oss-120b \ --speculative-config '{"model": "nvidia/gpt-oss-120b-Eagle3-long-context", "num_speculative_tokens": 3, "method": "eagle3"}' # Prefix cache hit rate: 0.0% # Without EAGLE: ~80% hit rate as expected vllm serve openai/gpt-oss-120b # Prefix cache hit rate: 88.7% # Workaround: disable hybrid KV cache manager vllm serve openai/gpt-oss-120b \ --speculative-config '...' \ --disable-hybrid-kv-cache-manager # Prefix cache hit rate: ~80% ``` Qwen3 with EAGLE works fine (not a hybrid attention model). ### Root Cause In `HybridKVCacheCoordinator.find_longest_cache_hit()`: 1. Full attention finds N blocks, does EAGLE drop → returns N-1 blocks 2. This sets `max_length = (N-1) * block_size` for sliding window 3. Sliding window searches range 0 to N-2, but its cached blocks may be at positions N-k to N-1 (within the window) 4. The last cached block (N-1) is now outside the search range 5. Sliding window can't find enough contiguous blocks to meet its threshold → returns 0 6. Sliding window also does its own EA...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: GPT-OSS 0% prefix cache hits with hybrid attention + EAGLE bug ### Your current environment ### 🐛 Describe the bug ```bash # Eval script used python tests/evals/gsm8k/gsm8k_eval.py # With EAGLE: 0% prefix cache h...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: GPT-OSS 0% prefix cache hits with hybrid attention + EAGLE bug ### Your current environment ### 🐛 Describe the bug ```bash # Eval script used python tests/evals/gsm8k/gsm8k_eval.py # With EAGLE: 0% prefix cache h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### 🐛 Describe the bug ```bash # Eval script used python tests/evals/gsm8k/gsm8k_eval.py # With EAGLE: 0% prefix cache hit rate vllm serve openai/gpt-oss-120b \ --speculative-config '{"model": "nvidia/gpt-oss-120b-Eagle...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: KVCacheCoordinator.find_longest_cache_hit()`: 1. Full attention finds N blocks, does EAGLE drop → returns N-1 blocks 2. This sets `max_length = (N-1) * block_size` for sliding window 3. Sliding window searches range 0 t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: E bug ### Your current environment ### 🐛 Describe the bug ```bash # Eval script used python tests/evals/gsm8k/gsm8k_eval.py # With EAGLE: 0% prefix cache hit rate vllm serve openai/gpt-oss-120b \ --speculative-config '{...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
