# vllm-project/vllm#29139: [Feature]: Optimize collectives in TP MoE case using torch.compile pass

| 字段 | 值 |
| --- | --- |
| Issue | [#29139](https://github.com/vllm-project/vllm/issues/29139) |
| 状态 | open |
| 标签 | help wanted;good first issue;performance;feature request;torch.compile |
| 评论 | 33; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Optimize collectives in TP MoE case using torch.compile pass

### Issue 正文摘录

### 🚀 The feature, motivation and pitch To avoid redundant work in MoE models in the TP case, sequence parallelism was added to the Deepseek model definition in #24134 and expanded to other models in #24982. However, to avoid performing surgery on the linear layer, the current approach performs more communication than necessary. With a torch.compile custom pass, we can rewrite the graph to remove the redundant computation. ### More details Before the SP optimization, the ops in the model were: ``` - o_proj:[num_tokens, ...] -> [num_tokens, ...] (incomplete results) - all_reduce:[num_tokens, ...] -> [num_tokens, ...] - rms_norm:[num_tokens, ...] -> [num_tokens, ...] - router:[num_tokens, ...] -> [num_tokens, ...] - experts:[num_tokens, ...] -> [num_tokens, ...] - ... ``` With sequence parallel enabled, this becomes: ``` - o_proj: [num_tokens, ...] -> [num_tokens, ...] (incomplete results) - all_reduce: [num_tokens, ...] -> [num_tokens, ...] - rms_norm:[num_tokens, ...] -> [num_tokens, ...] - chunk: [num_tokens, ...] -> [num_tokens/tp, ...] - router: [num_tokens/tp, ...] -> [num_tokens/tp, ...] - experts: [num_tokens/tp, ...] -> [num_tokens/tp, ...] - all_gather: [num_tokens/tp, ......

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature]: Optimize collectives in TP MoE case using torch.compile pass help wanted;good first issue;performance;feature request;torch.compile ### 🚀 The feature, motivation and pitch To avoid redundant work in MoE model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: To avoid redundant work in MoE models in the TP case, sequence parallelism was added to the Deepseek model definition in #24134 and expanded to other models in #24982. However, to avoid performing surgery on the linear...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🚀 The feature, motivation and pitch To avoid redundant work in MoE models in the TP case, sequence parallelism was added to the Deepseek model definition in #24134 and expanded to other models in #24982. However, to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: num_tokens, ...] ``` Additionally, experts now properly do the dp+tp ep dispatch instead of just the original replicated dp ep dispatch. Notice that the `all_reduce` (and `rms_norm`) do redundant communication as each T...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Optimize collectives in TP MoE case using torch.compile pass help wanted;good first issue;performance;feature request;torch.compile ### 🚀 The feature, motivation and pitch To avoid redundant work in MoE model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
