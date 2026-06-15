# vllm-project/vllm#38923: [Feature]: Built-in request multiplexer to let `vllm serve` use all available GPUs without external proxies

| 字段 | 值 |
| --- | --- |
| Issue | [#38923](https://github.com/vllm-project/vllm/issues/38923) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Built-in request multiplexer to let `vllm serve` use all available GPUs without external proxies

### Issue 正文摘录

### 🚀 The feature, motivation and pitch If I understand correctly, currently `--data-parallel-size` cannot be used for spinning several copies of a served non-MoE model? For the case where a model takes only 2 or 4 GPUs, one needs to launch several copies of vllm, and handle somehow request dispatching. It would be great for it to be built-in vllm for simple serving (or offline request processing) I think this request has been discussed quite a lot in `--data-parallel-size`-related issues ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: , one needs to launch several copies of vllm, and handle somehow request dispatching. It would be great for it to be built-in vllm for simple serving (or offline request processing) I think this request has been discuss...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lel-size` cannot be used for spinning several copies of a served non-MoE model? For the case where a model takes only 2 or 4 GPUs, one needs to launch several copies of vllm, and handle somehow request dispatching. It w...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: arallel-size` cannot be used for spinning several copies of a served non-MoE model? For the case where a model takes only 2 or 4 GPUs, one needs to launch several copies of vllm, and handle somehow request dispatching....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Built-in request multiplexer to let `vllm serve` use all available GPUs without external proxies feature request ### 🚀 The feature, motivation and pitch If I understand correctly, currently `--data-parallel-s...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
