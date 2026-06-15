# vllm-project/vllm#11550: [Performance]: How to measure the actual GPU memory usage?

| 字段 | 值 |
| --- | --- |
| Issue | [#11550](https://github.com/vllm-project/vllm/issues/11550) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: How to measure the actual GPU memory usage?

### Issue 正文摘录

### Proposal to improve performance Hi there, we would like to measure the actual GPU memory usage of vLLM. Since it would occupy almost all memory after initialization, we cannot measure the size of GPU memory that is actually on used, that is, that part of GPU memory used for loading model weights and PagedAttention blocks that has already been allocated for existing requests. Is there such APIs to measure this? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: requests. Is there such APIs to measure this? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Performance]: How to measure the actual GPU memory usage? performance ### Proposal to improve performance Hi there, we would like to measure the actual GPU memory usage of vLLM. Since it would occupy almost all memory...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: hat part of GPU memory used for loading model weights and PagedAttention blocks that has already been allocated for existing requests. Is there such APIs to measure this? ### Report of performance regression _No respons...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t is actually on used, that is, that part of GPU memory used for loading model weights and PagedAttention blocks that has already been allocated for existing requests. Is there such APIs to measure this? ### Report of p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
