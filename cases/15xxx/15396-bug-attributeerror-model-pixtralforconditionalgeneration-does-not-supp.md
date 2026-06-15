# vllm-project/vllm#15396: [Bug]: AttributeError: Model PixtralForConditionalGeneration does not support BitsAndBytes quantization yet. No 'packed_modules_mapping' found.

| 字段 | 值 |
| --- | --- |
| Issue | [#15396](https://github.com/vllm-project/vllm/issues/15396) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: Model PixtralForConditionalGeneration does not support BitsAndBytes quantization yet. No 'packed_modules_mapping' found.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm==0.8.1 transformers==4.50.0 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ror: Model PixtralForConditionalGeneration does not support BitsAndBytes quantization yet. No 'packed_modules_mapping' found. bug;stale ### Your current environment ### 🐛 Describe the bug vllm==0.8.1 transformers==4.50....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0.0 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ation does not support BitsAndBytes quantization yet. No 'packed_modules_mapping' found. bug;stale ### Your current environment ### 🐛 Describe the bug vllm==0.8.1 transformers==4.50.0 ### Before submitting a new issue.....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: AttributeError: Model PixtralForConditionalGeneration does not support BitsAndBytes quantization yet. No 'packed_modules_mapping' found. bug;stale ### Your current environment ### 🐛 Describe the bug vllm==0.8.1 t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rt BitsAndBytes quantization yet. No 'packed_modules_mapping' found. bug;stale ### Your current environment ### 🐛 Describe the bug vllm==0.8.1 transformers==4.50.0 ### Before submitting a new issue... - [x] Make sure yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
