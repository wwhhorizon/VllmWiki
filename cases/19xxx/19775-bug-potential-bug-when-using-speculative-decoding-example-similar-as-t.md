# vllm-project/vllm#19775: [Bug]: Potential bug when using speculative decoding example similar as the one from docs

| 字段 | 值 |
| --- | --- |
| Issue | [#19775](https://github.com/vllm-project/vllm/issues/19775) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Potential bug when using speculative decoding example similar as the one from docs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm currently trying to following [this documentation](https://docs.vllm.ai/en/stable/features/spec_decode.html#speculating-with-a-draft-model) but don't know why it is taking so long to set up the speculative decoding model. I've already had the chance to set up a vllm server using Llama 3.3 70B and it doesn't take this long. So far it's been 2 hours, so I'm wondering if this could be related to a potential bug or maybe something else. Please any suggestion is welcome, thanks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Potential bug when using speculative decoding example similar as the one from docs bug;stale ### Your current environment ### 🐛 Describe the bug I'm currently trying to following [this documentation](https://docs...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ocs.vllm.ai/en/stable/features/spec_decode.html#speculating-with-a-draft-model) but don't know why it is taking so long to set up the speculative decoding model. I've already had the chance to set up a vllm server using...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ondering if this could be related to a potential bug or maybe something else. Please any suggestion is welcome, thanks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
