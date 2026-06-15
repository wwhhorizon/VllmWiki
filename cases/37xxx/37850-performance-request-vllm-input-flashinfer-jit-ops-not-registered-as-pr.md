# vllm-project/vllm#37850: [Performance]: Request vLLM input: FlashInfer JIT ops not registered as proper torch.ops custom ops, breaking torch.compile(fullgraph=True) — upstream fix in progress at flashinfer#2734

| 字段 | 值 |
| --- | --- |
| Issue | [#37850](https://github.com/vllm-project/vllm/issues/37850) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Request vLLM input: FlashInfer JIT ops not registered as proper torch.ops custom ops, breaking torch.compile(fullgraph=True) — upstream fix in progress at flashinfer#2734

### Issue 正文摘录

### Proposal to improve performance ## Context FlashInfer PR #2734 is fixing torch.compile(fullgraph=True) compatibility for FlashInfer JIT-backed ops. The root cause: register_custom_op / register_fake_op in FlashInfer were stub no-ops, so Dynamo traces into the Python body and hits Path.exists() / os.stat() in the JIT loading path — which Dynamo cannot capture, breaking fullgraph compilation. ## Current state in SGLang SGLang uses an is_dynamo_compiling() guard as an explicit temporary workaround: - Eager → calls FlashInfer JIT directly - Under torch.compile → falls back to torch.ops.sgl_kernel.* AOT kernels (proper PyTorch custom ops, opaque to Dynamo) ## Why we need vLLM input The original performance concern about enabling torch.library.custom_op in FlashInfer was raised by the vLLM team (referenced in the PR). Before the FlashInfer maintainers merge the fix, they want vLLM to weigh in on: 1. Does vLLM currently hit this same issue with FlashInfer JIT kernels under torch.compile? 2. Is there any regression risk from enabling proper custom op registration in FlashInfer (the original perf concern)? 3. Can a vLLM contributor review/approve the direction in flashinfer#2734? cc @n...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: er JIT ops not registered as proper torch.ops custom ops, breaking torch.compile(fullgraph=True) — upstream fix in progress at flashinfer#2734 performance ### Proposal to improve performance ## Context FlashInfer PR #27...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: issue with FlashInfer JIT kernels under torch.compile? 2. Is there any regression risk from enabling proper custom op registration in FlashInfer (the original perf concern)? 3. Can a vLLM contributor review/approve the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Performance]: Request vLLM input: FlashInfer JIT ops not registered as proper torch.ops custom ops, breaking torch.compile(fullgraph=True) — upstream fix in progress at flashinfer#2734 performance ### Proposal to impro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: Request vLLM input: FlashInfer JIT ops not registered as proper torch.ops custom ops, breaking torch.compile(fullgraph=True) — upstream fix in progress at flashinfer#2734 performance ### Proposal to impro...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
