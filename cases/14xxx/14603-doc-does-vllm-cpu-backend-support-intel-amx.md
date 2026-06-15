# vllm-project/vllm#14603: [Doc]: Does vllm CPU backend support Intel AMX?

| 字段 | 值 |
| --- | --- |
| Issue | [#14603](https://github.com/vllm-project/vllm/issues/14603) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Does vllm CPU backend support Intel AMX?

### Issue 正文摘录

### 📚 The doc issue I see pr #4971 has integrated some optimizations into vllm CPU backend, and I want to know whether vllm CPU supports intel AMX, and how to use it. Thank you. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Doc]: Does vllm CPU backend support Intel AMX? documentation;stale ### 📚 The doc issue I see pr #4971 has integrated some optimizations into vllm CPU backend, and I want to know whether vllm CPU supports intel AMX, and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: Does vllm CPU backend support Intel AMX? documentation;stale ### 📚 The doc issue I see pr #4971 has integrated some optimizations into vllm CPU backend, and I want to know whether vllm CPU supports intel AMX, and...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
