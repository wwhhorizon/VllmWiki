# vllm-project/vllm#16932: [Bug]: Pooling model adapter removes the attributes expected by model init

| 字段 | 值 |
| --- | --- |
| Issue | [#16932](https://github.com/vllm-project/vllm/issues/16932) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Pooling model adapter removes the attributes expected by model init

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Cannot load model as embedding model because of attributes getting removed inside the adapter. I am currently encountering the error described in the screenshot because the model failed to load. The attributes `lm_head.logits_processor` was removed here https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/adapters.py#L58-L61 while it's expected by the model in its `__init__` method here: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/gemma3_mm.py#L497 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Pooling model adapter removes the attributes expected by model init bug;stale ### Your current environment ### 🐛 Describe the bug Cannot load model as embedding model because of attributes getting removed inside...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 97 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ttps://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/gemma3_mm.py#L497 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Pooling model adapter removes the attributes expected by model init bug;stale ### Your current environment ### 🐛 Describe the bug Cannot load model as embedding model because of attributes getting removed inside the ada...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
