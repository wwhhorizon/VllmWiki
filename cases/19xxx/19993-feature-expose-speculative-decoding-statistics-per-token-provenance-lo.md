# vllm-project/vllm#19993: [Feature]: Expose speculative-decoding statistics & per-token provenance/log-probs in `GenerationOutput`

| 字段 | 值 |
| --- | --- |
| Issue | [#19993](https://github.com/vllm-project/vllm/issues/19993) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Expose speculative-decoding statistics & per-token provenance/log-probs in `GenerationOutput`

### Issue 正文摘录

### Description `vllm.LLM.generate()` returns a list of `CompletionOutput` objects that contain the generated text, `token_ids`, and (optionally) **target-model** log-probs. When speculative decoding (SD) is enabled, all SD-related information is currently accessible only via the global Prometheus metrics endpoint. That means a client that runs offline evaluation must poll those counters and manually correlate them with each call to `generate`, which is inconvenient and loses per-request granularity. --- ### What we propose 1. **Add SD statistics to `CompletionOutput`** | field | meaning | |-------|---------| | `sd_stats.num_draft_tokens` | tokens proposed by the draft model | | `sd_stats.num_accepted_tokens` | tokens accepted by the target model | | `sd_stats.efficiency` | vLLM-reported SD efficiency | 2. **Return draft-model log-probs** next to the existing target log-probs. 3. **Return a per-token “source mask”** indicating whether each emitted token was accepted from the draft model (`1`) or produced by the target model (`0`). This enables fine-grained analysis such as latency attribution or adaptive-K research. --- ### Possible API sketch ```python @dataclass class SpecDecode...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: bal Prometheus metrics endpoint. That means a client that runs offline evaluation must poll those counters and manually correlate them with each call to `generate`, which is inconvenient and loses per-request granularit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Feature]: Expose speculative-decoding statistics & per-token provenance/log-probs in `GenerationOutput` feature request;stale ### Description `vllm.LLM.generate()` returns a list of `CompletionOutput` objects that cont...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: that contain the generated text, `token_ids`, and (optionally) **target-model** log-probs. When speculative decoding (SD) is enabled, all SD-related information is currently accessible only via the global Prometheus met...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: -cases * **Benchmarking & evaluation** – relate acceptance-rate to task accuracy. * **Dynamic tuning** – adjust `num_speculative_tokens` on the fly without scraping global metrics. * **Debugging & research** – quickly s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pted_tokens` | tokens accepted by the target model | | `sd_stats.efficiency` | vLLM-reported SD efficiency | 2. **Return draft-model log-probs** next to the existing target log-probs. 3. **Return a per-token “source mas...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
