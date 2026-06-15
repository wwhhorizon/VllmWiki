# vllm-project/vllm#39677: [Bug]: The premature implementation of structured generation constraints in qwen3 led to a disastrous decline in model capabilities.

| 字段 | 值 |
| --- | --- |
| Issue | [#39677](https://github.com/vllm-project/vllm/issues/39677) |
| 状态 | open |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The premature implementation of structured generation constraints in qwen3 led to a disastrous decline in model capabilities.

### Issue 正文摘录

### Your current environment Query: Please answer with only Y or N: Is the sky blue? # Error reply request body ```json { "model": "qwen3-8B", "messages": [{"role": "user", "content": "Please answer with only Y or N: Is the sky blue?"}], "temperature": 0.0, "max_tokens": 500, "chat_template_kwargs": {"enable_thinking": true}, "guided_regex": "[YN]" } ``` output ```json { "model": "qwen3-8B", "choices": [ { "index": 0, "message": { "role": "assistant", "content": "N", "reasoning_content": "\nOkay, the user is asking if the sky is blue. I need to answer with just Y or N. Let me think. The sky appears blue because of Rayleigh scattering. When sunlight enters the Earth's atmosphere, the shorter wavelengths of light (like blue and violet) are scattered more than the longer wavelengths (like red and yellow). Even though violet has a shorter wavelength than blue, the sky appears blue because our eyes are more sensitive to blue light and some of the violet light is absorbed by the upper atmosphere. So, the answer should be yes. But wait, sometimes the sky can look different, like during sunrise or sunset when it's more red or orange. But the general answer is that the sky is blue. So the...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: g]: The premature implementation of structured generation constraints in qwen3 led to a disastrous decline in model capabilities. bug ### Your current environment Query: Please answer with only Y or N: Is the sky blue?...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ned conditions, it has two extra \n characters. ### 🐛 Describe the bug docker ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom rig...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ker ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Query: Please answer with only Y or N: Is the sky blue? # Error reply request body ```json { "model": "qwen3-8B", "messages": [{"role": "user", "content": "Please answer with only Y or N: Is the sky blue?"}], "temperatu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
