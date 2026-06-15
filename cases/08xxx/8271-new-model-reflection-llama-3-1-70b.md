# vllm-project/vllm#8271: [New Model]: Reflection-Llama-3.1-70B

| 字段 | 值 |
| --- | --- |
| Issue | [#8271](https://github.com/vllm-project/vllm/issues/8271) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Reflection-Llama-3.1-70B

### Issue 正文摘录

### The model to consider. https://huggingface.co/mattshumer/Reflection-Llama-3.1-70B ### The closest model vllm already supports. https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Reflection-Llama-3.1-70B new-model;stale ### The model to consider. https://huggingface.co/mattshumer/Reflection-Llama-3.1-70B ### The closest model vllm already supports. https://huggingface.co/meta-llama/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Reflection-Llama-3.1-70B new-model;stale ### The model to consider. https://huggingface.co/mattshumer/Reflection-Llama-3.1-70B ### The closest model vllm already supports. https://huggingface.co/meta-llama/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
