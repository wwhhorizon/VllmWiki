# vllm-project/vllm#15996: [Bug]: System gets stuck during pressure test

| 字段 | 值 |
| --- | --- |
| Issue | [#15996](https://github.com/vllm-project/vllm/issues/15996) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: System gets stuck during pressure test

### Issue 正文摘录

### Your current environment vllm 0.7.2 with a single A100 80G ### 🐛 Describe the bug We're trying to pressure-test vllm on our own machine (single node with one A100 80G) with LlaMA-30B model, the request arrival rate is set to a high value (nearly 2 req / s) so that the GPU KV Cache utilization quickly increases (with logs show that GPU KV Cache > 90%) within a few minutes. The problem is, as we keep sending requests when the Cache is near-fully occupied, the system would somehow get stuck. The logs show that new requests are added and all in Pending state, there are still some requests in Running state but nothing more is generated and returned. With futher debugging, we find that the system would keep doing "scheduling → empty shcedule output → empty call to step_async (we are using _AsyncLLMEngine_)". Why doesn't the scheduler schedule any requests for execution? And no preemption was done, although we set _preemtion_mode_ as _swap_ and use priority policy, we just cannot judge whether it's a common case. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: System gets stuck during pressure test bug;stale ### Your current environment vllm 0.7.2 with a single A100 80G ### 🐛 Describe the bug We're trying to pressure-test vllm on our own machine (single node with one A...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: re test bug;stale ### Your current environment vllm 0.7.2 with a single A100 80G ### 🐛 Describe the bug We're trying to pressure-test vllm on our own machine (single node with one A100 80G) with LlaMA-30B model, the req...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: essure-test vllm on our own machine (single node with one A100 80G) with LlaMA-30B model, the request arrival rate is set to a high value (nearly 2 req / s) so that the GPU KV Cache utilization quickly increases (with l...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t arrival rate is set to a high value (nearly 2 req / s) so that the GPU KV Cache utilization quickly increases (with logs show that GPU KV Cache > 90%) within a few minutes. The problem is, as we keep sending requests...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: System gets stuck during pressure test bug;stale ### Your current environment vllm 0.7.2 with a single A100 80G ### 🐛 Describe the bug We're trying to pressure-test vllm on our own machine (single node with one A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
