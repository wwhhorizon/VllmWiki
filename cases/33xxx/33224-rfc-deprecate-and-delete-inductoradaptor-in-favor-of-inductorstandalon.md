# vllm-project/vllm#33224: [RFC]: Deprecate and delete InductorAdaptor in favor of InductorStandaloneAdaptor

| 字段 | 值 |
| --- | --- |
| Issue | [#33224](https://github.com/vllm-project/vllm/issues/33224) |
| 状态 | open |
| 标签 | RFC;torch.compile;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Deprecate and delete InductorAdaptor in favor of InductorStandaloneAdaptor

### Issue 正文摘录

### Motivation. InductorStandaloneAdaptor (standalone_compile) has been on by default since PyTorch 2.9. We initially turned it on in PyTorch 2.8, had some problems with it (and turned it off), but it has been on by default since PyTorch 2.9. Many models (e.g. Deepseek 3.2) actually require InductorStandaloneAdaptor to run (for reasons I don't understand). vLLM aims to support at most the current PyTorch version and the previous PyTorch version. When vLLM upgrades to using PyTorch 2.10, then the two versions will be 2.10 and 2.9. The motivation to deprecate InductorAdaptor is to simplify the code via [deletion](https://github.com/vllm-project/vllm/blob/a97b5e206d78b96a75615f402357dbf7e73d4efe/vllm/compilation/compiler_interface.py#L313-L641). Sometimes folks get confused and think we want to support both when they read the code, we only really want to support one. ### Proposed Change. Deprecate InductorAdaptor once vLLM upgrades to PyTorch 2.10. That is, emit a deprecation warning when it is used. Delete InductorAdaptor sometime later (PyTorch 2.11? Or after X vLLM releases?). NB: I might want to speed up the timeline here too, it is not clear to me anything is preventing the Indu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d delete InductorAdaptor in favor of InductorStandaloneAdaptor RFC;torch.compile;stale ### Motivation. InductorStandaloneAdaptor (standalone_compile) has been on by default since PyTorch 2.9. We initially turned it on i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: upgrades to PyTorch 2.10". In particular, figure out which vLLM hardware backends can use InductorAdaptor/InductorStandaloneAdaptor and then see when those adopt PyTorch 2.10. ### Feedback Period. one week ### CC List....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nd turned it off), but it has been on by default since PyTorch 2.9. Many models (e.g. Deepseek 3.2) actually require InductorStandaloneAdaptor to run (for reasons I don't understand). vLLM aims to support at most the cu...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: e adopt PyTorch 2.10. ### Feedback Period. one week ### CC List. @ProExpertProg @youkaichao @BoyuanFeng @angelayi @gmagogsfm @Lucaskabela ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Ma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
