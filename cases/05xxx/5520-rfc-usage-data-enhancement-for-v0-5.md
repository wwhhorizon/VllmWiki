# vllm-project/vllm#5520: [RFC]: Usage Data Enhancement for v0.5.*

| 字段 | 值 |
| --- | --- |
| Issue | [#5520](https://github.com/vllm-project/vllm/issues/5520) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Usage Data Enhancement for v0.5.*

### Issue 正文摘录

### Motivation. vLLM currently has a usage reporting feature https://docs.vllm.ai/en/stable/serving/usage_stats.html to inform us what features can be safely deprecated or what hardware to improve performance on. After v0.5.0, vLLM has various features that's being tested (chunked prefill, prefix caching, spec decode, fp8, and VLM), we would like to start gathering statistics on the usage of these features with different hardware and model types so we know what we are tested on. ### Proposed Change. Add the following data to `usage_lib` * `--enable-chunked-prefill` * `--enable-prefix-cache` * `speculative_model` (need model architecture/size or [ngram]) Another missing value from previous data is the size of the model, so we find it difficult to compare llama3 8b vs 70b. This might require some creative way to find the size of the model without capturing too much information. Any other suggestion welcomed. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [RFC]: Usage Data Enhancement for v0.5.* RFC;stale ### Motivation. vLLM currently has a usage reporting feature https://docs.vllm.ai/en/stable/serving/usage_stats.html to inform us what features can be safely deprecated...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: t's being tested (chunked prefill, prefix caching, spec decode, fp8, and VLM), we would like to start gathering statistics on the usage of these features with different hardware and model types so we know what we are te...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: tures that's being tested (chunked prefill, prefix caching, spec decode, fp8, and VLM), we would like to start gathering statistics on the usage of these features with different hardware and model types so we know what...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ked-prefill` * `--enable-prefix-cache` * `speculative_model` (need model architecture/size or [ngram]) Another missing value from previous data is the size of the model, so we find it difficult to compare llama3 8b vs 7...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ve performance on. After v0.5.0, vLLM has various features that's being tested (chunked prefill, prefix caching, spec decode, fp8, and VLM), we would like to start gathering statistics on the usage of these features wit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
