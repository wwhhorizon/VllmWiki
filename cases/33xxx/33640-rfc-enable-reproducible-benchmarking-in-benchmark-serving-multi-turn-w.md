# vllm-project/vllm#33640: [RFC]: Enable reproducible benchmarking in benchmark_serving_multi_turn with API-usage token counts

| 字段 | 值 |
| --- | --- |
| Issue | [#33640](https://github.com/vllm-project/vllm/issues/33640) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Enable reproducible benchmarking in benchmark_serving_multi_turn with API-usage token counts

### Issue 正文摘录

### Motivation. The token counting in `benchmark_serving_multi_turn.py` doesn't match actual API behavior, making benchmark results hard to reproduce. (`benchmarks/multi_turn/benchmark_serving_multi_turn.py`) #### Token count mismatch due to missing chat template Even when using `--limit-min-tokens 0 --limit-max-tokens 0` to follow dataset token counts, the benchmark calculates tokens differently from the API: ```python # Current implementation - tokenizes each message independently def get_messages_token_count(tokenizer, messages): token_count = 0 for m in messages: token_count += get_token_count(tokenizer, m["content"]) return token_count ``` This misses special tokens like ` `, ` user\n[500] \n (+5 tokens) assistant\n[700] \n (+5 tokens) user\n[400] \n (+5 tokens) assistant\n (+3 tokens) = ~1618 tokens ``` with DeepSeek R1 format, ``` Benchmark calculation: User1(500) + Asst1(700) + User2(400) = 1600 tokens Actual API processing: [system] (+1 token, BOS) [500] (+1 token) [700] (+2 tokens) [400] (+1 token) (+1 token) = ~1606 tokens ``` The discrepancy varies by model and chat template, but it's always there. #### Missing output_tokens field breaks reproducibility The dataset for...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: [RFC]: Enable reproducible benchmarking in benchmark_serving_multi_turn with API-usage token counts RFC;stale ### Motivation. The token counting in `benchmark_serving_multi_turn.py` doesn't match actual API behavior, ma...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [RFC]: Enable reproducible benchmarking in benchmark_serving_multi_turn with API-usage token counts RFC;stale ### Motivation. The token counting in `benchmark_serving_multi_turn.py` doesn't match actual API behavior, ma...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nt\n (+3 tokens) = ~1618 tokens ``` with DeepSeek R1 format, ``` Benchmark calculation: User1(500) + Asst1(700) + User2(400) = 1600 tokens Actual API processing: [system] (+1 token, BOS) [500] (+1 token) [700] (+2 token...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC]: Enable reproducible benchmarking in benchmark_serving_multi_turn with API-usage token counts RFC;stale ### Motivation. The token counting in `benchmark_serving_multi_turn.py` doesn't match actual API behavior, ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: chmarks/multi_turn/benchmark_serving_multi_turn.py`) #### Token count mismatch due to missing chat template Even when using `--limit-min-tokens 0 --limit-max-tokens 0` to follow dataset token counts, the benchmark calcu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
