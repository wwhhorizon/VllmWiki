# vllm-project/vllm#16191: [Usage]: How can I quickly obtain the number of prompt tokens containing multimodal data?

| 字段 | 值 |
| --- | --- |
| Issue | [#16191](https://github.com/vllm-project/vllm/issues/16191) |
| 状态 | closed |
| 标签 | help wanted;usage;stale;multi-modality |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How can I quickly obtain the number of prompt tokens containing multimodal data?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm The /tokenize API can only return the number of prompt tokens that contain text and multimodal placeholders, but cannot return the actual number of prompt tokens. @DarkLight1337 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 37 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: How can I quickly obtain the number of prompt tokens containing multimodal data? help wanted;usage;stale;multi-modality ### Your current environment ```text The output of `python collect_env.py` ``` ### How wou...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: he number of prompt tokens containing multimodal data? help wanted;usage;stale;multi-modality ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm The /tokeni...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
