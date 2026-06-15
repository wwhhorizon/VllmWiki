# vllm-project/vllm#23891: [Feature] Improve embedding merge implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#23891](https://github.com/vllm-project/vllm/issues/23891) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] Improve embedding merge implementation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently merging text embeddings and multimodal embedding is done by checking `input_ids` in the current batch and scatter multimodal embeddings into where the placeholder ids are. See more details [here](https://github.com/ywang96/vllm/blob/main/vllm/model_executor/models/utils.py#L478C2-L478C32). An alternative solution here that should be investigated is to gather this information from `mm_positions` of scheduled requests to form a batch-level mask (similar to `grammar_bitmask`) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: The feature, motivation and pitch Currently merging text embeddings and multimodal embedding is done by checking `input_ids` in the current batch and scatter multimodal embeddings into where the placeholder ids are. See...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature] Improve embedding merge implementation feature request ### 🚀 The feature, motivation and pitch Currently merging text embeddings and multimodal embedding is done by checking `input_ids` in the current batch an...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
