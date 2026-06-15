# vllm-project/vllm#14032: [Bug]: EP enablement and chunked-prefill-enablement

| 字段 | 值 |
| --- | --- |
| Issue | [#14032](https://github.com/vllm-project/vllm/issues/14032) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: EP enablement and chunked-prefill-enablement

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug export VLLM_TEST_ENABLE_EP=1 vllm server xxxxx --enable-chunked-prefill This is how I enble the EP feature and enable the chunked prefill two quesiones: 1.How I confirm the EP is enabled correctly, it seems no such information from the log 2.From the log, I see the chunked-prefilled-enable is falsed. Is this a bug or not> THanks, ![Image](https://github.com/user-attachments/assets/591f5101-66b4-4661-8c06-62698273b088) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: EP enablement and chunked-prefill-enablement bug;stale ### Your current environment ### 🐛 Describe the bug export VLLM_TEST_ENABLE_EP=1 vllm server xxxxx --enable-chunked-prefill This is how I enble the EP featur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 88) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ion from the log 2.From the log, I see the chunked-prefilled-enable is falsed. Is this a bug or not> THanks, ![Image](https://github.com/user-attachments/assets/591f5101-66b4-4661-8c06-62698273b088) ### Before submittin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: esiones: 1.How I confirm the EP is enabled correctly, it seems no such information from the log 2.From the log, I see the chunked-prefilled-enable is falsed. Is this a bug or not> THanks, ![Image](https://github.com/use...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ale ### Your current environment ### 🐛 Describe the bug export VLLM_TEST_ENABLE_EP=1 vllm server xxxxx --enable-chunked-prefill This is how I enble the EP feature and enable the chunked prefill two quesiones: 1.How I co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
