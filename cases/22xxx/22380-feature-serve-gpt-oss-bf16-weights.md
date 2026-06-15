# vllm-project/vllm#22380: [Feature]: serve gpt-oss BF16 weights

| 字段 | 值 |
| --- | --- |
| Issue | [#22380](https://github.com/vllm-project/vllm/issues/22380) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: serve gpt-oss BF16 weights

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It would be great if vLLM can also support serving GPT-OSS BF16 weights (either upcasted, or finetuned), like this one: https://huggingface.co/unsloth/gpt-oss-20b-BF16/discussions/1 Many people have the needs to finetune or tweak GPT-OSS, but they won't be able to quantize it back to MXFP4 due to the lack of QAT capability ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature]: serve gpt-oss BF16 weights feature request;stale ### 🚀 The feature, motivation and pitch It would be great if vLLM can also support serving GPT-OSS BF16 weights (either upcasted, or finetuned), like this one:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t they won't be able to quantize it back to MXFP4 due to the lack of QAT capability ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already se...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: serve gpt-oss BF16 weights feature request;stale ### 🚀 The feature, motivation and pitch It would be great if vLLM can also support serving GPT-OSS BF16 weights (either upcasted, or finetuned), like this one:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: serve gpt-oss BF16 weights feature request;stale ### 🚀 The feature, motivation and pitch It would be great if vLLM can also support serving GPT-OSS BF16 weights (either upcasted, or finetuned), like this one:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: (either upcasted, or finetuned), like this one: https://huggingface.co/unsloth/gpt-oss-20b-BF16/discussions/1 Many people have the needs to finetune or tweak GPT-OSS, but they won't be able to quantize it back to MXFP4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
