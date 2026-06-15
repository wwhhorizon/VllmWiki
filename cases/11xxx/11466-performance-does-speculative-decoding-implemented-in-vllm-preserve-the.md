# vllm-project/vllm#11466: [Performance]: Does Speculative Decoding implemented in vLLM preserve the target model output?

| 字段 | 值 |
| --- | --- |
| Issue | [#11466](https://github.com/vllm-project/vllm/issues/11466) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Does Speculative Decoding implemented in vLLM preserve the target model output?

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance The Speculative Decoding in vLLM is implemented followed [Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/pdf/2302.01318) instead of [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/pdf/2211.17192). Will the speculative decoding output be the same as the target model output? ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance The Speculative Decoding in vLLM is implemented followed [Accelerating Large Language Mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ance]: Does Speculative Decoding implemented in vLLM preserve the target model output? performance ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: Does Speculative Decoding implemented in vLLM preserve the target model output? performance ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc di...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
