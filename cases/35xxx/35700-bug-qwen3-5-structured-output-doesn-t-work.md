# vllm-project/vllm#35700: [Bug]: Qwen3.5 structured output doesn't work

| 字段 | 值 |
| --- | --- |
| Issue | [#35700](https://github.com/vllm-project/vllm/issues/35700) |
| 状态 | open |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 structured output doesn't work

### Issue 正文摘录

### Your current environment vllm nightly image ### 🐛 Describe the bug Serve Qwen3.5 27B FP8 as a openai compatible seveing. Use openai-python-sdk response format function, found model response doesn't follow the structure required. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5 structured output doesn't work bug ### Your current environment vllm nightly image ### 🐛 Describe the bug Serve Qwen3.5 27B FP8 as a openai compatible seveing. Use openai-python-sdk response format functi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: vironment vllm nightly image ### 🐛 Describe the bug Serve Qwen3.5 27B FP8 as a openai compatible seveing. Use openai-python-sdk response format function, found model response doesn't follow the structure required. ### B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
