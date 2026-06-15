# vllm-project/vllm#22945: [Feature][CUDAGraph]: Audit CUDAGraph support in attention backends

| 字段 | 值 |
| --- | --- |
| Issue | [#22945](https://github.com/vllm-project/vllm/issues/22945) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][CUDAGraph]: Audit CUDAGraph support in attention backends

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In #20059, we added more fine-grained control over what kinds of batches are supported in cudagraphs for each attention backend. For some, we did not know exactly what's supported so we played this safe. This should be audited by people with more knowledge of the backends to make sure we allow the broadest support that's still safe. Backends (and current support): - [ ] AITER: `UNIFORM_SINGLE_TOKEN_DECODE` - [ ] FlashMLA: `UNIFORM_BATCH` - [ ] FlashInfer: `UNIFORM_SINGLE_TOKEN_DECODE` - [ ] FA2: `UNIFORM_BATCH` - should indicate ALWAYS but with separate full cudagraphs for uniform single-token decode and mixed batch. FA3 and Triton (both `ALWAYS`) not listed. We should likely also remove methods `can_run_in_cudagraph` and `build_for_cudagraph_capture` as support is now handled statically and `build` can be used instead of the latter. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequen...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Feature][CUDAGraph]: Audit CUDAGraph support in attention backends feature request;unstale ### 🚀 The feature, motivation and pitch In #20059, we added more fine-grained control over what kinds of batches are supported...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ature][CUDAGraph]: Audit CUDAGraph support in attention backends feature request;unstale ### 🚀 The feature, motivation and pitch In #20059, we added more fine-grained control over what kinds of batches are supported in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature][CUDAGraph]: Audit CUDAGraph support in attention backends feature request;unstale ### 🚀 The feature, motivation and pitch In #20059, we added more fine-grained control over what kinds of batches are supported...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: isted. We should likely also remove methods `can_run_in_cudagraph` and `build_for_cudagraph_capture` as support is now handled statically and `build` can be used instead of the latter. ### Alternatives _No response_ ###...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
