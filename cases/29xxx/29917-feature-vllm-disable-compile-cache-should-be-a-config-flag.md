# vllm-project/vllm#29917: [Feature]: VLLM_DISABLE_COMPILE_CACHE should be a config flag

| 字段 | 值 |
| --- | --- |
| Issue | [#29917](https://github.com/vllm-project/vllm/issues/29917) |
| 状态 | closed |
| 标签 | help wanted;feature request;torch.compile;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: VLLM_DISABLE_COMPILE_CACHE should be a config flag

### Issue 正文摘录

### 🚀 The feature, motivation and pitch `vllm serve` does a nice printout of non-default config flags. VLLM_DISABLE_COMPILE_CACHE gets used enough that it should have an equivalent config flag for it Offline @ProExpertProg mentioned we can treat it like VLLM_DEBUG_DUMP_PATH where we have both and the env var overrides the config option by overwriting it directly ### Alternatives none ### Additional context n/a ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : VLLM_DISABLE_COMPILE_CACHE should be a config flag help wanted;feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch `vllm serve` does a nice printout of non-default config flags. VLLM_DISABLE_CO...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: VLLM_DISABLE_COMPILE_CACHE should be a config flag help wanted;feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch `vllm serve` does a nice printout of non-default config flags. VLLM_D...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n/a ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: VLLM_DISABLE_COMPILE_CACHE should be a config flag help wanted;feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch `vllm serve` does a nice printout of non-default config flags. VLLM_D...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: enough that it should have an equivalent config flag for it Offline @ProExpertProg mentioned we can treat it like VLLM_DEBUG_DUMP_PATH where we have both and the env var overrides the config option by overwriting it dir...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
