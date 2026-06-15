# vllm-project/vllm#27722: [Bug]: `yarn_find_correction_range` incorrect for GPT-OSS

| 字段 | 值 |
| --- | --- |
| Issue | [#27722](https://github.com/vllm-project/vllm/issues/27722) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `yarn_find_correction_range` incorrect for GPT-OSS

### Issue 正文摘录

### Your current environment VLLM v0.11.0 ### 🐛 Describe the bug In the HuggingFace implementation of GPT-OSS, [truncate is set to False](https://huggingface.co/openai/gpt-oss-20b/blob/main/config.json#L66) within the rope config, which means that the bounds of the yarn correction range are [_not_ rounded to integers](https://github.com/huggingface/transformers/blob/main/src/transformers/modeling_rope_utils.py#L407-L414). In constrast, vllm's bounds are [always rounded to integers](https://github.com/vllm-project/vllm/blob/d2c33c397ad30f0b0fad7296a3c80d47df0243fe/vllm/model_executor/layers/rotary_embedding/common.py#L118-L123). Would it be possible to add support for `truncate=False` for parity with HuggingFace? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: `yarn_find_correction_range` incorrect for GPT-OSS bug ### Your current environment VLLM v0.11.0 ### 🐛 Describe the bug In the HuggingFace implementation of GPT-OSS, [truncate is set to False](https://huggingface...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: bug In the HuggingFace implementation of GPT-OSS, [truncate is set to False](https://huggingface.co/openai/gpt-oss-20b/blob/main/config.json#L66) within the rope config, which means that the bounds of the yarn correctio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
