# vllm-project/vllm#20394: [RFC][UX]: debug mode for vLLM-compile

| 字段 | 值 |
| --- | --- |
| Issue | [#20394](https://github.com/vllm-project/vllm/issues/20394) |
| 状态 | open |
| 标签 | RFC;torch.compile;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC][UX]: debug mode for vLLM-compile

### Issue 正文摘录

### Motivation. vLLM-compile (CompilationLevel.PIECEWISE) makes a lot of assumptions about the models that allow it to make them run really fast. There are two main assumptions that commonly lead to silent incorrectness if the models violate them. I've spent countless hours debugging user issues for it to turn out to be one of these assumptions. We should add a debug mode option for vLLM-compile that, when turned on, adds some safety checks for these assumptions at the tradeoff of some additional overhead. This will let users self-diagnose the issues without me in the loop. This is one of the items mentioned in https://github.com/vllm-project/vllm/issues/20283, I'm expanding it to include some more details. ### Proposed Change. The two assumptions that bite us are: 1) the [vLLM Dynamic Shapes Issue](https://docs.google.com/document/d/1R3XvVEpJeVi3whyxf4xpyZufGplbrfw628oXLZ6fqG0/edit?tab=t.0#heading=h.59xosv6nz9lg). vLLM performs one single graph capture with dynamic batch size and expects the graph to work for all batch sizes. However, the graph may not actually be valid for all batch sizes. 2) CUDAGraphs assume that the input addresses of Tensors do not change. Changing the input...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s. However, the graph may not actually be valid for all batch sizes. 2) CUDAGraphs assume that the input addresses of Tensors do not change. Changing the input addresses (e.g. doing model.weight1 = new_weight1) violates...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ompile (CompilationLevel.PIECEWISE) makes a lot of assumptions about the models that allow it to make them run really fast. There are two main assumptions that commonly lead to silent incorrectness if the models violate...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [RFC][UX]: debug mode for vLLM-compile RFC;torch.compile;unstale ### Motivation. vLLM-compile (CompilationLevel.PIECEWISE) makes a lot of assumptions about the models that allow it to make them run really fast. There ar...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ses did not change. ### Feedback Period. 7/2 - 7/11 ### CC List. @ProExpertProg @youkaichao @mgoin @robertgshaw2-redhat @WoosukKwon @drisspg @houseroad ### Any Other Things. thank you ### Before submitting a new issue.....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC][UX]: debug mode for vLLM-compile RFC;torch.compile;unstale ### Motivation. vLLM-compile (CompilationLevel.PIECEWISE) makes a lot of assumptions about the models that allow it to make them run really fast. There ar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
