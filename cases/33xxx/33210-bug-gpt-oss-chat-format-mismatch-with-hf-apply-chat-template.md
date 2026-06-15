# vllm-project/vllm#33210: [Bug]: gpt-oss chat format mismatch with HF apply_chat_template

| 字段 | 值 |
| --- | --- |
| Issue | [#33210](https://github.com/vllm-project/vllm/issues/33210) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: gpt-oss chat format mismatch with HF apply_chat_template

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The code path for how messages get processed for gpt-oss in vllm differs from huggingface’s apply_chat_template which might lead to subtle suboptimal performance. In hf - users system message gets prepended to developer message as “#Instruction\n\n{user-system-message}\n\n#Tools\n\n{tools_rendering}” - moreover, in the absence of tools and user system message the tags for developer message don't get added In vllm - there is always a default developer message that is empty or has tool descriptions - users system/developer message gets added as separate system message after developer message ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: gpt-oss chat format mismatch with HF apply_chat_template bug;stale ### Your current environment ### 🐛 Describe the bug The code path for how messages get processed for gpt-oss in vllm differs from huggingface’s a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: gpt-oss chat format mismatch with HF apply_chat_template bug;stale ### Your current environment ### 🐛 Describe the bug The code path for how messages get processed for gpt-oss in vllm differs from huggingface’s a...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: gpt-oss chat format mismatch with HF apply_chat_template bug;stale ### Your current environment ### 🐛 Describe the bug The code path for how messages get processed for gpt-oss in vllm differs from huggingface’s a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: gpt-oss chat format mismatch with HF apply_chat_template bug;stale ### Your current environment ### 🐛 Describe the bug The code path for how messages get processed for gpt-oss in vllm differs from huggingface’s a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
