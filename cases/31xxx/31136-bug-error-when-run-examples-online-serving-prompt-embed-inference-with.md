# vllm-project/vllm#31136: [Bug]: error when run examples/online_serving/prompt_embed_inference_with_openai_client.py

| 字段 | 值 |
| --- | --- |
| Issue | [#31136](https://github.com/vllm-project/vllm/issues/31136) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: error when run examples/online_serving/prompt_embed_inference_with_openai_client.py

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, I am using vllm v0.12.0, and when I run [examples/online_serving/prompt_embed_inference_with_openai_client.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/prompt_embed_inference_with_openai_client.py) I met the below error: `(EngineCore_DP0 pid=305033) msgspec.ValidationError: Expected `object | null`, got `array` - at `$[10]`` Note: my model is `Qwen/Qwen3-0.6B` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nError: Expected `object | null`, got `array` - at `$[10]`` Note: my model is `Qwen/Qwen3-0.6B` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 6B` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
