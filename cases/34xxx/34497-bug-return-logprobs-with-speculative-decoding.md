# vllm-project/vllm#34497: [Bug]: return logprobs with speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#34497](https://github.com/vllm-project/vllm/issues/34497) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: return logprobs with speculative decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM claims to support `logprobs` together with speculative decoding as of v0.11.1 (see https://github.com/vllm-project/vllm/pull/26060). Since then, there have been multiple issues/PRs referring to improving support for `logprobs` + speculative decoding. However, the `is_spec_decode_unsupported` function continues to disable speculative decoding whenever `logprobs` is requested, and this logic is only removed around v0.14.0. In v0.12.0, the function still looks like this: ```python def is_spec_decode_unsupported(sampling_params: SamplingParams) -> bool: """True if request is incompatible with speculative decoding""" return ( sampling_params.frequency_penalty != 0.0 or sampling_params.presence_penalty != 0.0 or sampling_params.repetition_penalty != 1.0 or sampling_params.min_p > _SAMPLING_EPS or sampling_params.logprobs is not None ) ``` As an experiment, I commented out the line ```python or sampling_params.logprobs is not None ``` to allow speculative decoding when `logprobs` are requested, but the returned logprobs are incorrect/broken (tested on v0.12.0). My question is: how can I obtain **correct** `logprobs` when using spec...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: return logprobs with speculative decoding bug ### Your current environment ### 🐛 Describe the bug vLLM claims to support `logprobs` together with speculative decoding as of v0.11.1 (see https://github.com/vllm-pr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: grade vLLM up to v0.12.0, so any workaround or backportable fix for this version would be very helpful. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ul. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: logprobs` are requested, but the returned logprobs are incorrect/broken (tested on v0.12.0). My question is: how can I obtain **correct** `logprobs` when using speculative decoding (e.g., suffix/ngram speculative decodi...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
