# vllm-project/vllm#24461: [BugFix]: Avoid unnecessary coordination for non-MoE data parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#24461](https://github.com/vllm-project/vllm/issues/24461) |
| 状态 | closed |
| 标签 | bug;help wanted |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [BugFix]: Avoid unnecessary coordination for non-MoE data parallel

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, when DP is enabled, we assume the model uses EP or TP for expert layers and as such enable additional synchronization so that dummy forward passes are done in idle ranks when necessary, and certain metadata is shared before each forward pass. However, this is also done for non-MoE models unnecessarily, which results in unnecessary additional overhead. We should ensure that the extra DP-related sync isn't done in this case. We do probably still want the DPCoordinator to run, since we'll still want it to propagate the load-balancing stats. ### Alternatives We could consider hard-failing in this situation to avoid folks unintentionally using vLLM with sub-par performance.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [BugFix]: Avoid unnecessary coordination for non-MoE data parallel bug;help wanted ### 🚀 The feature, motivation and pitch Currently, when DP is enabled, we assume the model uses EP or TP for expert layers and as such e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Coordinator to run, since we'll still want it to propagate the load-balancing stats. ### Alternatives We could consider hard-failing in this situation to avoid folks unintentionally using vLLM with sub-par performance.
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: dummy forward passes are done in idle ranks when necessary, and certain metadata is shared before each forward pass. However, this is also done for non-MoE models unnecessarily, which results in unnecessary additional o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ture, motivation and pitch Currently, when DP is enabled, we assume the model uses EP or TP for expert layers and as such enable additional synchronization so that dummy forward passes are done in idle ranks when necess...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
