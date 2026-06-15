# vllm-project/vllm#23456: [CI]: Replace use of models with smaller models where possible

| 字段 | 值 |
| --- | --- |
| Issue | [#23456](https://github.com/vllm-project/vllm/issues/23456) |
| 状态 | closed |
| 标签 | ci/build;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;moe |
| 子分类 |  |
| Operator 关键词 | cuda;moe |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI]: Replace use of models with smaller models where possible

### Issue 正文摘录

- Many tests use an arbitrary model, use a small one such as opt-125m (or smaller) in these cases. - If an arbitrary MoE model is required, ibm-research/PowerMoE-3b can be used (or maybe we can identify an even smaller one) - Ensure `--enforce-eager` is included in server startup args for short-running tests that aren't testing cuda graphs specifically This can reduce the overall running time significantly

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [CI]: Replace use of models with smaller models where possible ci/build;stale - Many tests use an arbitrary model, use a small one such as opt-125m (or smaller) in these cases. - If an arbitrary MoE model is required, i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI]: Replace use of models with smaller models where possible ci/build;stale - Many tests use an arbitrary model, use a small one such as opt-125m (or smaller) in these cases. - If an arbitrary MoE model is required, i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [CI]: Replace use of models with smaller models where possible ci/build;stale - Many tests use an arbitrary model, use a small one such as opt-125m (or smaller) in these cases. - If an arbitrary MoE model is required, i...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: mall one such as opt-125m (or smaller) in these cases. - If an arbitrary MoE model is required, ibm-research/PowerMoE-3b can be used (or maybe we can identify an even smaller one) - Ensure `--enforce-eager` is included...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI]: Replace use of models with smaller models where possible ci/build;stale - Many tests use an arbitrary model, use a small one such as opt-125m (or smaller) in these cases. - If an arbitrary MoE model is required, i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
