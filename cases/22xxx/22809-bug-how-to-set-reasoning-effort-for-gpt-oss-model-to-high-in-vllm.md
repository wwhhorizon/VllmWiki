# vllm-project/vllm#22809: [Bug]: How to set reasoning_effort for gpt-oss model to "high" in vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#22809](https://github.com/vllm-project/vllm/issues/22809) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: How to set reasoning_effort for gpt-oss model to "high" in vllm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi Team, I have deployed gpt oss model on vllm with this image. vllm/vllm-openai:gptoss I am unable to enable function calling and reasoning_effort. Can you please guide me how to enable tool calls and reasoning_effort ? This is my deployment spec: spec: containers: - args: - --host - 0.0.0.0 - --port - "8000" - --model - openai/gpt-oss-120b - --swap-space - "16" - --disable-log-requests - --tensor-parallel-size - "2" Do I need to enable anything here? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: How to set reasoning_effort for gpt-oss model to "high" in vllm bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug Hi Team, I have deployed gpt oss model on vllm with this image. vllm/vllm-open...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: How to set reasoning_effort for gpt-oss model to "high" in vllm bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug Hi Team, I have deployed gpt oss model on vllm with this image. vllm/vllm-openai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: re? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
