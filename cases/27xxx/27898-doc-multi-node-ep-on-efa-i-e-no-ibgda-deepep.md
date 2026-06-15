# vllm-project/vllm#27898: [Doc]: Multi-node EP on EFA (i.e. no IBGDA/DeepEP)

| 字段 | 值 |
| --- | --- |
| Issue | [#27898](https://github.com/vllm-project/vllm/issues/27898) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Multi-node EP on EFA (i.e. no IBGDA/DeepEP)

### Issue 正文摘录

### 📚 The doc issue Usecase: On AWS we have EFA for high bandwidth interconnect, not Infiniband, so no IBGDA. The [documentation](https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment.html#backend-selection-guide) indicates that the DeepEP kernels should be used for multi/inter-node EP, and pplx for single node. However, [DeepEP indicates that they only support IBGDA for inter-node comms](https://github.com/deepseek-ai/DeepEP/issues/369). pplx has good support for EFA. Is pplx for single node, DeepEP for multi-node a suggestion based on testing, or a hard requirement? In addition, it appears that the EP size cannot be configured and is always TP x DP. Is there any way to set EP size to equal TP size (for example), so we can have each node be a DP group and limit EP alltoall's to intra-node (NVLink) only? Thank you! EDIT: per https://github.com/vllm-project/vllm/issues/27633 it appears this may be problematic, although since pplx supports EFA as a transportation layer, this seems bizarre. Specific docs around usage on EFA would be helpful.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: an have each node be a DP group and limit EP alltoall's to intra-node (NVLink) only? Thank you! EDIT: per https://github.com/vllm-project/vllm/issues/27633 it appears this may be problematic, although since pplx support...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ](https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment.html#backend-selection-guide) indicates that the DeepEP kernels should be used for multi/inter-node EP, and pplx for single node. However, [DeepEP indi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: a hard requirement? In addition, it appears that the EP size cannot be configured and is always TP x DP. Is there any way to set EP size to equal TP size (for example), so we can have each node be a DP group and limit E...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: so no IBGDA. The [documentation](https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment.html#backend-selection-guide) indicates that the DeepEP kernels should be used for multi/inter-node EP, and pplx for sin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: Multi-node EP on EFA (i.e. no IBGDA/DeepEP) documentation;stale ### 📚 The doc issue Usecase: On AWS we have EFA for high bandwidth interconnect, not Infiniband, so no IBGDA. The [documentation](https://docs.vllm....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
