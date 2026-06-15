# vllm-project/vllm#40602: [Bug]: Qwen/Qwen3.5-122B-A10B-FP8 stuck in thinking loop with 0.19.2rc1.dev107+g4eafc7292

| 字段 | 值 |
| --- | --- |
| Issue | [#40602](https://github.com/vllm-project/vllm/issues/40602) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen/Qwen3.5-122B-A10B-FP8 stuck in thinking loop with 0.19.2rc1.dev107+g4eafc7292

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using the docker image `vllm/vllm-openai:cu130-nightly` with model `Qwen/Qwen3.5-122B-A10B-FP8`. I am using `'override_generation_config': {'temperature': 0.6, 'top_p': 0.95, 'top_k': 20, 'min_p': 0.0, 'presence_penalty': 0.0, 'repetition_penalty': 1.0}` vllm version `0.19.1rc1.dev312+g55e1a8e10` works fine. vllm version `0.19.2rc1.dev107+g4eafc7292` hangs in thinking loops after prompting simple questions. It kinda feels like `override_generation_config` is ignored, but I could not find any indication of this in the container logs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen/Qwen3.5-122B-A10B-FP8 stuck in thinking loop with 0.19.2rc1.dev107+g4eafc7292 bug ### Your current environment ### 🐛 Describe the bug I am using the docker image `vllm/vllm-openai:cu130-nightly` with model `...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ### Your current environment ### 🐛 Describe the bug I am using the docker image `vllm/vllm-openai:cu130-nightly` with model `Qwen/Qwen3.5-122B-A10B-FP8`. I am using `'override_generation_config': {'temperature': 0.6, 't...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Qwen/Qwen3.5-122B-A10B-FP8 stuck in thinking loop with 0.19.2rc1.dev107+g4eafc7292 bug ### Your current environment ### 🐛 Describe the bug I am using the docker image `vllm/vllm-openai:cu130-nightly` with model `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: gs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
