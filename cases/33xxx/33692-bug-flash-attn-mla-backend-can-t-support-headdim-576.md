# vllm-project/vllm#33692: [Bug]: FLash Attn MLA Backend can't support headdim!=576

| 字段 | 值 |
| --- | --- |
| Issue | [#33692](https://github.com/vllm-project/vllm/issues/33692) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: FLash Attn MLA Backend can't support headdim!=576

### Issue 正文摘录

### Your current environment . ### 🐛 Describe the bug I am running a custom model, which uses MLA while headdim=64， it run with error "raise ValueError(f"Head dimension 64 is not supported by MLA) My Attention Backend is Flashattention-2, and i found this restriction is added by MLACommonBackend, which only supports 576 for headdim. I think, this restriction should be removed or support more dimension for different models ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: FLash Attn MLA Backend can't support headdim!=576 bug;stale ### Your current environment . ### 🐛 Describe the bug I am running a custom model, which uses MLA while headdim=64， it run with error "raise ValueError(...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: els ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ur current environment . ### 🐛 Describe the bug I am running a custom model, which uses MLA while headdim=64， it run with error "raise ValueError(f"Head dimension 64 is not supported by MLA) My Attention Backend is Flas...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: FLash Attn MLA Backend can't support headdim!=576 bug;stale ### Your current environment . ### 🐛 Describe the bug I am running a custom model, which uses MLA while headdim=64， it run with error "raise ValueError(...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
