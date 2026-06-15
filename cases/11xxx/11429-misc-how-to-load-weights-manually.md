# vllm-project/vllm#11429: [Misc]: how to load weights manually ?

| 字段 | 值 |
| --- | --- |
| Issue | [#11429](https://github.com/vllm-project/vllm/issues/11429) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: how to load weights manually ?

### Issue 正文摘录

### Anything you want to discuss about vllm. I'm trying to add a new model using vllm with instructions from [adding_model](https://docs.vllm.ai/en/latest/models/adding_model.html),There's load_weights function, and by default it load_weights from huggingface_hub, how can I load weights from a normal checkpoint rather than using huggingface-hub checkpoint? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ? ### Anything you want to discuss about vllm. I'm trying to add a new model using vllm with instructions from [adding_model](https://docs.vllm.ai/en/latest/models/adding_model.html),There's load_weights function, and b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ing vllm with instructions from [adding_model](https://docs.vllm.ai/en/latest/models/adding_model.html),There's load_weights function, and by default it load_weights from huggingface_hub, how can I load weights from a n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
