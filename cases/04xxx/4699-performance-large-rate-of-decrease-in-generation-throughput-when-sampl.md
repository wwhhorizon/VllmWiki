# vllm-project/vllm#4699: [Performance]: large rate of decrease in generation throughput when SamplingParams.logprobs increases

| 字段 | 值 |
| --- | --- |
| Issue | [#4699](https://github.com/vllm-project/vllm/issues/4699) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: large rate of decrease in generation throughput when SamplingParams.logprobs increases

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Model: meta-llama/Meta-Llama-3-8B-Instruct GPU: 1x A6000 | SamplingParams.logprobs | Generation Throughput (vLLM==0.4.2) (tokens/s) | Generation Throughput (vLLM==0.3.0) (tokens/s) | | -------- | ------- | ------- | | 100 | 37.76435 | 39.47888 | | 1000 | 27.62177 | 38.71567 | | 10000 | 9.62248 | 36.21264 | | 20000 | 5.36203 | 35.83716 | | len(tokenizer.vocab.keys()) | 1.00312 | 22.60807 | | len(tokenizer.vocab.keys()) + fix post-processing | 6.03333 | N.A. | ### Misc discussion on performance In my project, I have a vLLM server and during inference, I require to get all the log probs for every generated token as I need to do further post-processing/sampling. Getting all the log probs didn't result in visible drop in generation throughput previously but it became especially obvious since I migrated to vLLM==0.4.1. In vllm==0.4.1 and 0.4.2, there is a large rate of decrease in the generation throughput when `SamplingParams.logprobs` increases. It can get as low as 1 token/s using meta-llama/Meta-Llama-3-8B-Instruct on an A6000 with `engine_args.max_logprobs == sampling_params.logprobs == len(token...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: lt in visible drop in generation throughput previously but it became especially obvious since I migrated to vLLM==0.4.1. In vllm==0.4.1 and 0.4.2, there is a large rate of decrease in the generation throughput when `Sam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mprove performance _No response_ ### Report of performance regression Model: meta-llama/Meta-Llama-3-8B-Instruct GPU: 1x A6000 | SamplingParams.logprobs | Generation Throughput (vLLM==0.4.2) (tokens/s) | Generation Thro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: generation throughput when SamplingParams.logprobs increases performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Model: meta-llama/Meta-Llama-3-8B-Instruct GPU: 1x A6...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Performance]: large rate of decrease in generation throughput when SamplingParams.logprobs increases performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Model: meta-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
