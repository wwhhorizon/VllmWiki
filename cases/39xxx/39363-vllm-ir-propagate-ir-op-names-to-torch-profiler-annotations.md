# vllm-project/vllm#39363: [vLLM IR] Propagate IR op names to torch profiler annotations

| 字段 | 值 |
| --- | --- |
| Issue | [#39363](https://github.com/vllm-project/vllm/issues/39363) |
| 状态 | open |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [vLLM IR] Propagate IR op names to torch profiler annotations

### Issue 正文摘录

Looking at a torch profile (or nsys), it can often be difficult to know which kernel appearing in the profile correspond to which semantic operation. It would be good if we could somehow propagate this information down, specifically annotating both custom and codegen-ed Triton kernels with the corresponding IR op (and implementation name). This is slightly related to #39215. (thanks @tlrmchlsmth for the idea!)

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: his information down, specifically annotating both custom and codegen-ed Triton kernels with the corresponding IR op (and implementation name). This is slightly related to #39215. (thanks @tlrmchlsmth for the idea!)
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: It would be good if we could somehow propagate this information down, specifically annotating both custom and codegen-ed Triton kernels with the corresponding IR op (and implementation name). This is slightly related to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: plementation name). This is slightly related to #39215. (thanks @tlrmchlsmth for the idea!)
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: emantic operation. It would be good if we could somehow propagate this information down, specifically annotating both custom and codegen-ed Triton kernels with the corresponding IR op (and implementation name). This is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [vLLM IR] Propagate IR op names to torch profiler annotations Looking at a torch profile (or nsys), it can often be difficult to know which kernel appearing in the profile correspond to which semantic operation. It woul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
