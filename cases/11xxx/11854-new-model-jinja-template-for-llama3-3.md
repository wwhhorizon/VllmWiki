# vllm-project/vllm#11854: [New Model]: Jinja template for  Llama3.3

| 字段 | 值 |
| --- | --- |
| Issue | [#11854](https://github.com/vllm-project/vllm/issues/11854) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Jinja template for  Llama3.3

### Issue 正文摘录

### The model to consider. https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ### The closest model vllm already supports. vllm already supports Llama3.3 deployment but I am wondering on the chat template for it. ### What's your difficulty of supporting the model you want? Looking for chat template examples for Llama3.3 and wondering the closest or best recommended from https://github.com/vllm-project/vllm/tree/main/examples ? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Jinja template for Llama3.3 new-model;stale ### The model to consider. https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ### The closest model vllm already supports. vllm already supports Llama3.3 de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s ? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Jinja template for Llama3.3 new-model;stale ### The model to consider. https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ### The closest model vllm already supports. vllm already supports Llama3.3 de...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
