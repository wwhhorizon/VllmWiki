# vllm-project/vllm#1099: improve detokenize_incrementally performance

| 字段 | 值 |
| --- | --- |
| Issue | [#1099](https://github.com/vllm-project/vllm/issues/1099) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> improve detokenize_incrementally performance

### Issue 正文摘录

I tried to benchmark the latency of sequence calculation, and I found that the `detokenize_incrementally` function took a significant time. more specific, it's the calling to `tokenizer.convert_tokens_to_string` takes the most of time. however the input argument of `convert_tokens_to_string` is previous output tokens plus the new one, ``` output_tokens = prev_output_tokens + [new_token] ``` since the outer function called after each token calculated, the previous output tokens will do `convert_tokens_to_string` multiple times. I've measured in my environment, `convert_tokens_to_string` took around 2ms when convert the last token in my sequence (around 300 tokens, model is baichuan 13b), and it got called 300 times, so it cost around 0.3s for the total one sequence, that would be more time if the token number is bigger or batching number increasing. I was thinking if `convert_tokens_to_string` could only convert the newly calculated token instead of all the output tokens, so every token only convert once. I tried to change the code a little bit, like ``` output_tokens = [prev_output_text, new_token] ``` and it's 10 times faster for baichuan 13b so, do we have any special considerat...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: improve detokenize_incrementally performance I tried to benchmark the latency of sequence calculation, and I found that the `detokenize_incrementally` function took a significant time. more specific, it's the calling to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he `detokenize_incrementally` function took a significant time. more specific, it's the calling to `tokenizer.convert_tokens_to_string` takes the most of time. however the input argument of `convert_tokens_to_string` is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: round 2ms when convert the last token in my sequence (around 300 tokens, model is baichuan 13b), and it got called 300 times, so it cost around 0.3s for the total one sequence, that would be more time if the token numbe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
