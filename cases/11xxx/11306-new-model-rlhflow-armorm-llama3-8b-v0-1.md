# vllm-project/vllm#11306: [New Model]: RLHFlow/ArmoRM-Llama3-8B-v0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#11306](https://github.com/vllm-project/vllm/issues/11306) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: RLHFlow/ArmoRM-Llama3-8B-v0.1

### Issue 正文摘录

### The model to consider. https://huggingface.co/RLHFlow/ArmoRM-Llama3-8B-v0.1 ### The closest model vllm already supports. The generative Llama3 model is the closest: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/llama.py ### What's your difficulty of supporting the model you want? It will need to support adding the projection layer to map logits into reward dimensions. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: RLHFlow/ArmoRM-Llama3-8B-v0.1 new-model;stale ### The model to consider. https://huggingface.co/RLHFlow/ArmoRM-Llama3-8B-v0.1 ### The closest model vllm already supports. The generative Llama3 model is the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: RLHFlow/ArmoRM-Llama3-8B-v0.1 new-model;stale ### The model to consider. https://huggingface.co/RLHFlow/ArmoRM-Llama3-8B-v0.1 ### The closest model vllm already supports. The generative Llama3 model is the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
