# vllm-project/vllm#8170: [New Model]: Support for allenai/OLMoE-1B-7B-0924

| 字段 | 值 |
| --- | --- |
| Issue | [#8170](https://github.com/vllm-project/vllm/issues/8170) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Support for allenai/OLMoE-1B-7B-0924

### Issue 正文摘录

### The model to consider. allenai/OLMoE-1B-7B-0924 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: Support for allenai/OLMoE-1B-7B-0924 new-model;stale ### The model to consider. allenai/OLMoE-1B-7B-0924 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting t...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [New Model]: Support for allenai/OLMoE-1B-7B-0924 new-model;stale ### The model to consider. allenai/OLMoE-1B-7B-0924 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Support for allenai/OLMoE-1B-7B-0924 new-model;stale ### The model to consider. allenai/OLMoE-1B-7B-0924 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
