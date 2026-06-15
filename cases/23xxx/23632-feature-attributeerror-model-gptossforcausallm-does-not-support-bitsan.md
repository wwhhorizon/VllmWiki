# vllm-project/vllm#23632: [Feature]: AttributeError: Model GptOssForCausalLM does not support BitsAndBytes quantization yet. No 'packed_modules_mapping' found.  Support GptOssForCausalLM of BitsAndBytes quantization?

| 字段 | 值 |
| --- | --- |
| Issue | [#23632](https://github.com/vllm-project/vllm/issues/23632) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: AttributeError: Model GptOssForCausalLM does not support BitsAndBytes quantization yet. No 'packed_modules_mapping' found.  Support GptOssForCausalLM of BitsAndBytes quantization?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using the gpt-oss-20b_bnb_4bit model, the vllm service failed to start with the error message: AttributeError: Model GptOssForCausalLM does not support BitsAndBytes quantization yet. No 'packed_modules_mapping' found. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: AttributeError: Model GptOssForCausalLM does not support BitsAndBytes quantization yet. No 'packed_modules_mapping' found. Support GptOssForCausalLM of BitsAndBytes quantization? bug;stale;gpt-oss ### Your cu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ]: AttributeError: Model GptOssForCausalLM does not support BitsAndBytes quantization yet. No 'packed_modules_mapping' found. Support GptOssForCausalLM of BitsAndBytes quantization? bug;stale;gpt-oss ### Your current en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nd. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: salLM does not support BitsAndBytes quantization yet. No 'packed_modules_mapping' found. Support GptOssForCausalLM of BitsAndBytes quantization? bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug Usin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ing' found. Support GptOssForCausalLM of BitsAndBytes quantization? bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug Using the gpt-oss-20b_bnb_4bit model, the vllm service failed to start with the e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
