# vllm-project/vllm#30880: [Feature]: more robust way to detect if compile_sizes/compile_ranges applies to the current compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#30880](https://github.com/vllm-project/vllm/issues/30880) |
| 状态 | closed |
| 标签 | feature request;torch.compile;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: more robust way to detect if compile_sizes/compile_ranges applies to the current compilation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In https://github.com/vllm-project/vllm/pull/30489 we add a global variable to control if something is marked as being an encoder. In the future I think we'll want to move past this: we'll likely compile things that are more than just {encoders, decoders}. The compile_ranges and compile_sizes work operates under one assumption: that the captured graph has one dynamic size, and that dynamic size is the number of tokens. We should be able to infer this from the graph being captured: there's a symint in the graph. ### Alternatives Rename is_encoder to is_decoder, maybe we're saying compile_ranges only applies for decoders. ### Additional context cc @ilmarkov @ProExpertProg ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: compile_sizes/compile_ranges applies to the current compilation feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch In https://github.com/vllm-project/vllm/pull/30489 we add a global variable to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: more robust way to detect if compile_sizes/compile_ranges applies to the current compilation feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch In https://github.com/vllm-project/vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: og ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ges only applies for decoders. ### Additional context cc @ilmarkov @ProExpertProg ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
