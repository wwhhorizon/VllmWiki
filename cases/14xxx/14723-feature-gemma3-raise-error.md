# vllm-project/vllm#14723: [Feature]: gemma3 raise error

| 字段 | 值 |
| --- | --- |
| Issue | [#14723](https://github.com/vllm-project/vllm/issues/14723) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: gemma3 raise error

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Gemma3ForConditionalGeneration has no vLLM implementation, falling back to Transformers implementation. Some features may not be supported and performance may not be optimal. INFO 03-13 03:20:24 transformers.py:129] Using Transformers backend. ERROR 03-13 03:20:24 engine.py:400] Unrecognized configuration class for this kind of AutoModel: AutoModel. how to solve it ? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: gemma3 raise error feature request;stale ### 🚀 The feature, motivation and pitch Gemma3ForConditionalGeneration has no vLLM implementation, falling back to Transformers implementation. Some features may not b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: gemma3 raise error feature request;stale ### 🚀 The feature, motivation and pitch Gemma3ForConditionalGeneration has no vLLM implementation, falling back to Transformers implementation. Some features may not b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: be optimal. INFO 03-13 03:20:24 transformers.py:129] Using Transformers backend. ERROR 03-13 03:20:24 engine.py:400] Unrecognized configuration class for this kind of AutoModel: AutoModel. how to solve it ? ### Alternat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: gemma3 raise error feature request;stale ### 🚀 The feature, motivation and pitch Gemma3ForConditionalGeneration has no vLLM implementation, falling back to Transformers implementation. Some features may not b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
