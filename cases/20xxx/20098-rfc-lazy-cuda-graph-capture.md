# vllm-project/vllm#20098: [RFC]: Lazy CUDA Graph capture

| 字段 | 值 |
| --- | --- |
| Issue | [#20098](https://github.com/vllm-project/vllm/issues/20098) |
| 状态 | closed |
| 标签 | RFC;stale;startup-ux |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Lazy CUDA Graph capture

### Issue 正文摘录

### Motivation. Currently vLLM captures cudagraphs as part of the engine initialization significantly slowing down vLLM startup time. By default, vLLM captures 67 graphs, which depending on model size and GPU type, can take more than 10s. This is not great UX (see #19824 for details). In addition, It's most unlikely that all 67 graphs are actually needed, wasting both time and space. ### Proposed Change. We propose to capture cudagraphs lazily. Instead of performing dummy runs during the engine initialization phase, the idea is to do those runs somewhere in the CUDA piecewise backend, and only for the current runtime shape if not cached already. Exact implementation needs to be worked out. ### Feedback Period. one week ### CC List. @ProExpertProg @aarnphm @charlesfrye ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Lazy CUDA Graph capture RFC;stale;startup-ux ### Motivation. Currently vLLM captures cudagraphs as part of the engine initialization significantly slowing down vLLM startup time. By default, vLLM captures 67 grap...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tion phase, the idea is to do those runs somewhere in the CUDA piecewise backend, and only for the current runtime shape if not cached already. Exact implementation needs to be worked out. ### Feedback Period. one week...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: LM startup time. By default, vLLM captures 67 graphs, which depending on model size and GPU type, can take more than 10s. This is not great UX (see #19824 for details). In addition, It's most unlikely that all 67 graphs...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: eds to be worked out. ### Feedback Period. one week ### CC List. @ProExpertProg @aarnphm @charlesfrye ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for rel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Lazy CUDA Graph capture RFC;stale;startup-ux ### Motivation. Currently vLLM captures cudagraphs as part of the engine initialization significantly slowing down vLLM startup time. By default, vLLM captures 67 grap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
