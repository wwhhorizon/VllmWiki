# vllm-project/vllm#26398: [Docs] flashinfer missing from `/en/latest/configuration/env_vars.html`

| 字段 | 值 |
| --- | --- |
| Issue | [#26398](https://github.com/vllm-project/vllm/issues/26398) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Docs] flashinfer missing from `/en/latest/configuration/env_vars.html`

### Issue 正文摘录

### 📚 The doc issue I am using vLLM release 0.10.2 and got a nasty surprise about some undocumented environment variables used by flashinfer. I eventually found https://github.com/flashinfer-ai/flashinfer/blob/v0.3.0/flashinfer/jit/env.py, which I hope provides the answers I need. ### Suggest a potential alternative/fix Document FLASHINFER_WORKSPACE_BASE, FLASHINFER_CUBIN_DIR. FYI, https://github.com/vllm-project/vllm/pull/21972 will affect this. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Docs] flashinfer missing from `/en/latest/configuration/env_vars.html` documentation;stale ### 📚 The doc issue I am using vLLM release 0.10.2 and got a nasty surprise about some undocumented environment variables used...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Docs] flashinfer missing from `/en/latest/configuration/env_vars.html` documentation;stale ### 📚 The doc issue I am using vLLM release 0.10.2 and got a nasty surprise about some undocumented environment variables used...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nfer missing from `/en/latest/configuration/env_vars.html` documentation;stale ### 📚 The doc issue I am using vLLM release 0.10.2 and got a nasty surprise about some undocumented environment variables used by flashinfer...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Docs] flashinfer missing from `/en/latest/configuration/env_vars.html` documentation;stale ### 📚 The doc issue I am using vLLM release 0.10.2 and got a nasty surprise about some undocumented environment variables used...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
