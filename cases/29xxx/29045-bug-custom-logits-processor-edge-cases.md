# vllm-project/vllm#29045: [Bug]: Custom logits processor edge-cases

| 字段 | 值 |
| --- | --- |
| Issue | [#29045](https://github.com/vllm-project/vllm/issues/29045) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Custom logits processor edge-cases

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug The following Logits Processor API bug was reported in vLLM Slack; reproducing this bug is TODO: There are two edge cases where I see incorrect generations for my requests: 1. partial prefills: scheduler puts only a chunk of the prompt in the persistent batch. Model runner processes this, and then the sampler + LP runs, and the "wrong" token then gets discarded in the `_bookkeeping_sync` part of `gpu_model_runner.py`. The issue with this is that the partial prompt has modified state in the LP (`update_state()` was called on it), so even though the generated token was discarded the LP state is still corrupted. 2. preemptions: similarly, when a preempted request gets removed from the persistent batch, its LP state also gets deleted. When we re-add the preempted request later, it has a fresh state but the generated output tokens got added to the prompt (ie. we're not starting from scratch), so we essentially need to "replay" the generation inside the LP to restore state to before preemption. For (2), I can think of some ways to add more bookkeeping inside my LP (for example, don't delete the request's state until I truly know th...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Custom logits processor edge-cases bug;stale ### Your current environment N/A ### 🐛 Describe the bug The following Logits Processor API bug was reported in vLLM Slack; reproducing this bug is TODO: There are two...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he following Logits Processor API bug was reported in vLLM Slack; reproducing this bug is TODO: There are two edge cases where I see incorrect generations for my requests: 1. partial prefills: scheduler puts only a chun...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ode ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ills: scheduler puts only a chunk of the prompt in the persistent batch. Model runner processes this, and then the sampler + LP runs, and the "wrong" token then gets discarded in the `_bookkeeping_sync` part of `gpu_mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
