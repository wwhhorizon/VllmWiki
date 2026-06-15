# vllm-project/vllm#30023: [Feature]: Support qwen3next with GGUF?

| 字段 | 值 |
| --- | --- |
| Issue | [#30023](https://github.com/vllm-project/vllm/issues/30023) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support qwen3next with GGUF?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch With v0.11.0, `vllm` report: ``` vllm | (APIServer pid=1) ValueError: GGUF model with architecture qwen3next is not supported yet. ``` https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking-GGUF I did a simple dig for this, seems the vllm has support of `Qwen3-Next` as architecture is `qwen3_next`. But the `Qwen` set it as `qwen3next`. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Support qwen3next with GGUF? feature request ### 🚀 The feature, motivation and pitch With v0.11.0, `vllm` report: ``` vllm | (APIServer pid=1) ValueError: GGUF model with architecture qwen3next is not support...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: vllm` report: ``` vllm | (APIServer pid=1) ValueError: GGUF model with architecture qwen3next is not supported yet. ``` https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking-GGUF I did a simple dig for this, seems the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support qwen3next with GGUF? feature request ### 🚀 The feature, motivation and pitch With v0.11.0, `vllm` report: ``` vllm | (APIServer pid=1) ValueError: GGUF model with architecture qwen3next is not support...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
