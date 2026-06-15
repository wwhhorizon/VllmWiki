# vllm-project/vllm#2405: Feature request: Expert parallel for MoE architectures

| 字段 | 值 |
| --- | --- |
| Issue | [#2405](https://github.com/vllm-project/vllm/issues/2405) |
| 状态 | closed |
| 标签 | feature request;keep-open |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Feature request: Expert parallel for MoE architectures

### Issue 正文摘录

Can we implement the expert parallel strategy for MoE to fully exploit the sparse activation property? Ideally, MoE should only use compute at the order of active parameters, but the current implementation uses the same compute as a dense model. Expert parallelism is very similar to data parallelism across multiple GPUs, the only difference is that the experts are on separate GPUs and the tokens are permuted during MoE layer forward pass, as shown in the figure below. I can help implement the MoE layer, but I'm curious how to implement data parallel with vLLM? ![Diagram](https://github.com/vllm-project/vllm/assets/26354659/c04c1e05-30c6-458e-b791-67562fabc76f) (Diagram from [FastMoE](https://github.com/laekov/fastmoe))

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: Feature request: Expert parallel for MoE architectures feature request;keep-open Can we implement the expert parallel strategy for MoE to fully exploit the sparse activation property? Ideally, MoE should only use comput...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Feature request: Expert parallel for MoE architectures feature request;keep-open Can we implement the expert parallel strategy for MoE to fully exploit the sparse activation property? Ideally, MoE should only use comput...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ameters, but the current implementation uses the same compute as a dense model. Expert parallelism is very similar to data parallelism across multiple GPUs, the only difference is that the experts are on separate GPUs a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Feature request: Expert parallel for MoE architectures feature request;keep-open Can we implement the expert parallel strategy for MoE to fully exploit the sparse activation property? Ideally, MoE should only use comput...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
