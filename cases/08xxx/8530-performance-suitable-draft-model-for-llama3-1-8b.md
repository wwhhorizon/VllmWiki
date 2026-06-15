# vllm-project/vllm#8530: [Performance]: Suitable draft model for llama3.1 8b 

| 字段 | 值 |
| --- | --- |
| Issue | [#8530](https://github.com/vllm-project/vllm/issues/8530) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Suitable draft model for llama3.1 8b 

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Hi, a question on speculative decoding: for draft model method, it is natural to use llama3.1-8b as a draft model for llama3.1-70b, but for llama3.1-8b, what could be used as a suitable drafter? I noticed that some works used JackFram/llama-68m for llama2. However, the vocabulary size of llama3.1-8b is 128K, the vocabulary size of JackFram/llama-68m is 32000, and it seems that vLLM requires the vocabulary sizes of the draft model and the target model are the same. Are there any suggestions or experiences to share on this? Thanks a lot! ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: Suitable draft model for llama3.1 8b performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Hi, a question on speculative decoding: for draft model method...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Suitable draft model for llama3.1 8b performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Hi, a question on speculative decoding: for draft model method...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression Hi, a question on speculative decoding: for draft model method, it is natural to use llama3.1-8b as a draft model for llama3.1-70b, but f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
