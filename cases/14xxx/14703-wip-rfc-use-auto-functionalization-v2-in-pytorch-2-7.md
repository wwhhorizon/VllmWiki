# vllm-project/vllm#14703: [WIP][RFC]: Use auto-functionalization V2 in PyTorch 2.7+

| 字段 | 值 |
| --- | --- |
| Issue | [#14703](https://github.com/vllm-project/vllm/issues/14703) |
| 状态 | open |
| 标签 | RFC;torch.compile;keep-open;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [WIP][RFC]: Use auto-functionalization V2 in PyTorch 2.7+

### Issue 正文摘录

### Motivation In PyTorch 2.6, `auto_functionalized_v2` was introduced as a replacement for the `auto_functionalized` higher-order, partially to address the issues with redundant tensor copies in vLLM. However, certain custom fusion passes rely on pattern matching and don't currently work with `auto_functionalized_v2`. Due to this as well as a separate issue with V2 ([PyTorch#147924](https://github.com/pytorch/pytorch/issues/147924)), we are currently disabling V2 in PyTorch 2.6+. We have also circumvented the copy issues using a `FixFunctionalizationPass`, reducing the urgency for enabling V2. I am creating this RFC to centralize the discussion about when to upgrade to V2 and how to mitigate it in custom fusion passes. #### Motivation for custom passes Our graph-level optimization system performs graph transformations that would break abstractions or be intrusive to model code in some other way. For example, `RMSNormFusionPass` performs manual fusion of RMSNorm and quantization custom ops. A simplified model definition looks like this, whether quantization is enabled or not: ``` x2 = RMSNorm(x1) x3 = Linear(x2) ``` If quantization is on, `Linear` consists of a `quant` followed by...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [WIP][RFC]: Use auto-functionalization V2 in PyTorch 2.7+ RFC;torch.compile;keep-open;stale ### Motivation In PyTorch 2.6, `auto_functionalized_v2` was introduced as a replacement for the `auto_functionalized` higher-or...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: r custom passes Our graph-level optimization system performs graph transformations that would break abstractions or be intrusive to model code in some other way. For example, `RMSNormFusionPass` performs manual fusion o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: . For example, `RMSNormFusionPass` performs manual fusion of RMSNorm and quantization custom ops. A simplified model definition looks like this, whether quantization is enabled or not: ``` x2 = RMSNorm(x1) x3 = Linear(x...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: at ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: se auto-functionalization V2 in PyTorch 2.7+ RFC;torch.compile;keep-open;stale ### Motivation In PyTorch 2.6, `auto_functionalized_v2` was introduced as a replacement for the `auto_functionalized` higher-order, partiall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
