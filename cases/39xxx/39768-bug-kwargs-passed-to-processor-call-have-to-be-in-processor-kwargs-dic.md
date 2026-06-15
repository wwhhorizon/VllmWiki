# vllm-project/vllm#39768: [Bug]: Kwargs passed to `processor.__call__` have to be in `processor_kwargs` dict, not in `**kwargs`

| 字段 | 值 |
| --- | --- |
| Issue | [#39768](https://github.com/vllm-project/vllm/issues/39768) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Kwargs passed to `processor.__call__` have to be in `processor_kwargs` dict, not in `**kwargs`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I get this problem: Kwargs passed to `processor.__call__` have to be in `processor_kwargs` dict, not in `**kwargs` I was running a LLM Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-FP8 on vllm, and I get this. How can I pass these params with SamplingParams? I checked Google and found this a transformers==5.3 problem. And pip said that vllm support not more than 5.0 transformers. What should I do? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: rgs` I was running a LLM Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-FP8 on vllm, and I get this. How can I pass these params with SamplingParams? I checked Google and found this a transformers==5.3 problem. And pip...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: do? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: to be in `processor_kwargs` dict, not in `**kwargs` I was running a LLM Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-FP8 on vllm, and I get this. How can I pass these params with SamplingParams? I checked Google and...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
