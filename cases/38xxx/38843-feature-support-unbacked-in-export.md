# vllm-project/vllm#38843: [Feature]: support unbacked in export

| 字段 | 值 |
| --- | --- |
| Issue | [#38843](https://github.com/vllm-project/vllm/issues/38843) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support unbacked in export

### Issue 正文摘录

### 🚀 The feature, motivation and pitch some context https://docs.google.com/document/d/17VMPSBflbQ0zCl-r2WkCRCH4t06PlrVoruFR0TkTy5M/edit?tab=t.0#heading=h.gq9bcerm8ep1 TLDR: We want to do the following: 1. Support unbacked in export Named Dims someone shall be able to say : ``` dynamic_shapes = { "x": {0: Dim("batch1", min=1, max=100, unbacked=True)}, "y": {0: Dim("batch1", min=1, max=100, unbacked=True)}, } ``` 1. This shall elevate the user experience! since Named dims in export imposes restriction that all shapes restrictions (guards) are encoded in spec. with the unbacked we "auto learn" restrictions that are encoded with torch._checks and not require users to be explicit about them. (see the example in the doc above). 2. Shall we enable by default for named dims? at least for export? probably yes as step2 i do not forsee any regression regressions due to that. Note: We want to extend the export dynamic shapes specs to be supported in compile in the near future. ### Alternatives NA ### Additional context NA ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentatio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ns that are encoded with torch._checks and not require users to be explicit about them. (see the example in the doc above). 2. Shall we enable by default for named dims? at least for export? probably yes as step2 i do n...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ed dims? at least for export? probably yes as step2 i do not forsee any regression regressions due to that. Note: We want to extend the export dynamic shapes specs to be supported in compile in the near future. ### Alte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: NA ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: support unbacked in export feature request ### 🚀 The feature, motivation and pitch some context https://docs.google.com/document/d/17VMPSBflbQ0zCl-r2WkCRCH4t06PlrVoruFR0TkTy5M/edit?tab=t.0#heading=h.gq9bcerm8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
