# vllm-project/vllm#9750: [Usage]: Can I get the loss of model directly?

| 字段 | 值 |
| --- | --- |
| Issue | [#9750](https://github.com/vllm-project/vllm/issues/9750) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can I get the loss of model directly?

### Issue 正文摘录

Hi, great work! I am currently optimizing LLM based on `vLLM` and need to test whether my optimizations affect the model's perplexity. Therefore, I want to obtain the model's cross-entropy loss. I have reviewed the issue: [Can I directly obtain the logits here?](https://github.com/vllm-project/vllm/issues/185) and understand that one way to get log probabilities is by setting the `logprobs` parameter in `SampleParams`. However, this method is not very convenient. We can only obtain the top-n most likely log probabilities for each token, and the probability of the correct token might not be among these top-n log probabilities. Setting `n` and searching for the probability of the correct token is quite cumbersome, and the cross-entropy has to be calculated manually as well. Therefore, I want to know if `vLLM` has a way to directly obtain cross-entropy, similar to `transformers`. Thank you sincerely for your help. :-)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: oken might not be among these top-n log probabilities. Setting `n` and searching for the probability of the correct token is quite cumbersome, and the cross-entropy has to be calculated manually as well. Therefore, I wa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Can I get the loss of model directly? usage;stale Hi, great work! I am currently optimizing LLM based on `vLLM` and need to test whether my optimizations affect the model's perplexity. Therefore, I want to obta...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Can I get the loss of model directly? usage;stale Hi, great work! I am currently optimizing LLM based on `vLLM` and need to test whether my optimizations affect the model's perplexity. Therefore, I want to obta...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: i, great work! I am currently optimizing LLM based on `vLLM` and need to test whether my optimizations affect the model's perplexity. Therefore, I want to obtain the model's cross-entropy loss. I have reviewed the issue...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
