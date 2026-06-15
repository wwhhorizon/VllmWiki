# vllm-project/vllm#34407: [RFC]: Disaggregated Frontend — Separating Online Serving from Engine

| 字段 | 值 |
| --- | --- |
| Issue | [#34407](https://github.com/vllm-project/vllm/issues/34407) |
| 状态 | open |
| 标签 | RFC;keep-open |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Disaggregated Frontend — Separating Online Serving from Engine

### Issue 正文摘录

### Motivation. This RFC is a follow-up to [RFC #22817 (Disaggregated Everything - Token In <> Token Out API Server)](https://github.com/vllm-project/vllm/issues/22817), which proposed disaggregating tokenization and enabling a token-in / token-out API server. It builds upon https://github.com/vllm-project/vllm/issues/22880. Based on discussions in `#sig-frontend`, I propose a two-phase approach to achieve disaggregation. The key goals are: - **GPU-less deployment of frontend**: Allow preprocessing (tokenization, MM input processing) and postprocessing (detokenization, tool call parsing, reasoning parsing) to run without GPU. - **Disaggregated tokenization**: Support use cases such as llm-d, Dynamo, and custom frontends that need to leverage vLLM's preprocessing logic without running the full inference engine. - **Tokens-in / tokens-out engine**: Make the engine a pure token-in / token-out service, decoupled from request preprocessing. ### Proposed Change. We propose a two-phase disaggregation approach, introducing new CLI subcommands instead of [adding flags ](https://github.com/vllm-project/vllm/pull/33000)to the existing `vllm serve`. ### Phase 1: `vllm online` | `vllm engine`...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: regating tokenization and enabling a token-in / token-out API server. It builds upon https://github.com/vllm-project/vllm/issues/22880. Based on discussions in `#sig-frontend`, I propose a two-phase approach to achieve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e**: Make the engine a pure token-in / token-out service, decoupled from request preprocessing. ### Proposed Change. We propose a two-phase disaggregation approach, introducing new CLI subcommands instead of [adding fla...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d the heavier parts are the "renderer core" (inside vllm renderer). ### Architecture Overview ### Default Behavior By default, all components run co-located in the same process (equivalent to current `vllm serve`). Disa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
