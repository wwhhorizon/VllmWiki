# vllm-project/vllm#31204: [RFC]: Supporting Multi MTP layers in Speculative Decoding (EagleProposer)

| 字段 | 值 |
| --- | --- |
| Issue | [#31204](https://github.com/vllm-project/vllm/issues/31204) |
| 状态 | open |
| 标签 | RFC;unstale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Supporting Multi MTP layers in Speculative Decoding (EagleProposer)

### Issue 正文摘录

### Motivation. The EagleProposer for speculative decoding is only able to utilize the first MTP layer. However, the model [XiaomiMiMo/MiMo-V2-Flash](https://huggingface.co/XiaomiMiMo/MiMo-V2-Flash) has 3 MTP layers. Is there any plan or ongoing PR to extend support for multi MTP layers in speculative decoding? btw, [hugo-wind-ding/qwq-32b-mtp](https://huggingface.co/hugo-wind-ding/qwq-32b-mtp) has 7 mtp layers for QwQ-32B ### Proposed Change. EagleProposer needs a new member function to pass spec_step_idx to mtp models, when num_nextn_predict_layers > 1 and num_speculative_tokens > 1. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ative decoding is only able to utilize the first MTP layer. However, the model [XiaomiMiMo/MiMo-V2-Flash](https://huggingface.co/XiaomiMiMo/MiMo-V2-Flash) has 3 MTP layers. Is there any plan or ongoing PR to extend supp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Supporting Multi MTP layers in Speculative Decoding (EagleProposer) RFC;unstale ### Motivation. The EagleProposer for speculative decoding is only able to utilize the first MTP layer. However, the model [XiaomiMi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
