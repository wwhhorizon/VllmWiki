# vllm-project/vllm#17645: [Usage]: vLLM on multiple node GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#17645](https://github.com/vllm-project/vllm/issues/17645) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vLLM on multiple node GPUs

### Issue 正文摘录

### How would you like to use vllm I want to scale up vLLM by adding more GPU nodes in kubernetes. The model fits on a single GPU. I've tried scaling up vLLM using replicas/horizontal pod autoscaling. However the performance seems to be worse than a single node. The issue might be due to the routing. Any ideas as to what I'm doing wrong or what to do? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ance seems to be worse than a single node. The issue might be due to the routing. Any ideas as to what I'm doing wrong or what to do? ### Before submitting a new issue... - [x] Make sure you already searched for relevan...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: iple node GPUs usage;stale ### How would you like to use vllm I want to scale up vLLM by adding more GPU nodes in kubernetes. The model fits on a single GPU. I've tried scaling up vLLM using replicas/horizontal pod auto...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: do? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: llm I want to scale up vLLM by adding more GPU nodes in kubernetes. The model fits on a single GPU. I've tried scaling up vLLM using replicas/horizontal pod autoscaling. However the performance seems to be worse than a...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ance seems to be worse than a single node. The issue might be due to the routing. Any ideas as to what I'm doing wrong or what to do? ### Before submitting a new issue... - [x] Make sure you already searched for relevan...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
