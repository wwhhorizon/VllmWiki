# vllm-project/vllm#31004: [New Model]: T5Gemma 2

| 字段 | 值 |
| --- | --- |
| Issue | [#31004](https://github.com/vllm-project/vllm/issues/31004) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: T5Gemma 2

### Issue 正文摘录

### The model to consider. https://huggingface.co/collections/google/t5gemma-2 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? I know vLLM dropped encoder-decoder support, but can we bring it back? https://huggingface.co/docs/transformers/model_doc/t5gemma2 https://blog.google/technology/developers/t5gemma-2/ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: T5Gemma 2 new-model;stale ### The model to consider. https://huggingface.co/collections/google/t5gemma-2 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [New Model]: T5Gemma 2 new-model;stale ### The model to consider. https://huggingface.co/collections/google/t5gemma-2 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: -2/ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [New Model]: T5Gemma 2 new-model;stale ### The model to consider. https://huggingface.co/collections/google/t5gemma-2 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
