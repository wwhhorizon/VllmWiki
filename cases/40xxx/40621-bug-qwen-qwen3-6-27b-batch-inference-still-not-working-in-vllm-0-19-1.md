# vllm-project/vllm#40621: [Bug]: Qwen/Qwen3.6-27B - Batch Inference still not working in vllm 0.19.1

| 字段 | 值 |
| --- | --- |
| Issue | [#40621](https://github.com/vllm-project/vllm/issues/40621) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen/Qwen3.6-27B - Batch Inference still not working in vllm 0.19.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There have been a lot of issues on the fact that batch inference is not working on Qwen3.5 Series of models. One is here: https://github.com/vllm-project/vllm/issues/36010, I wrote one for Qwen 3.5 27B, guess it's quite well documented. It's the case for all Qwen Models. Please don't answer with the same suggestions as already present in the existing issues (of course, we're setting enable_prefix_caching=True ;)). Could someone finally have a look on that issue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen/Qwen3.6-27B - Batch Inference still not working in vllm 0.19.1 bug ### Your current environment ### 🐛 Describe the bug There have been a lot of issues on the fact that batch inference is not working on Qwen3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
