# vllm-project/vllm#11056: [Performance]: Arguments `EM` and `num_valid_tokens` of `fused_moe_kernel` should be set to `do_not_specialize`

| 字段 | 值 |
| --- | --- |
| Issue | [#11056](https://github.com/vllm-project/vllm/issues/11056) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Arguments `EM` and `num_valid_tokens` of `fused_moe_kernel` should be set to `do_not_specialize`

### Issue 正文摘录

### Proposal to improve performance The `fused_moe_kernel` is implemented with Triton. During runtime, Triton checks all kernel arguments of `torch.Tensor` and `int` and then specialize different kernels based on the remainder of the `tensor.data_ptr()` and `int` divided by 16. This mechanism is used to handle memory alignment things. `int`s are also checked because they are sometimes used to represent pointers. see: https://github.com/triton-lang/triton/blob/release/3.1.x/python/triton/runtime/jit.py#L295-L305 However, this specialization is unnecessary for the `fused_moe_kernel`'s `EM` and `num_valid_tokens`, as they do not represent pointers. Additionally, since these two parameters change when the number of input tokens change, Triton spends lots of time specializing and compiling a large number of unnecessary kernels, severely impacting the performance when the vllm service first starts. In Triton 3.1.0, we can use `do_not_specialize` to specify arguments that do not need specialization. The `EM` and `num_valid_tokens` should be labeled as `do_not_specialize`. example: https://github.com/triton-lang/triton/blob/release/3.1.x/python/test/unit/runtime/test_cache.py#L42-L46

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: posal to improve performance The `fused_moe_kernel` is implemented with Triton. During runtime, Triton checks all kernel arguments of `torch.Tensor` and `int` and then specialize different kernels based on the remainder...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and `num_valid_tokens` of `fused_moe_kernel` should be set to `do_not_specialize` performance;stale ### Proposal to improve performance The `fused_moe_kernel` is implemented with Triton. During runtime, Triton checks al...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: emainder of the `tensor.data_ptr()` and `int` divided by 16. This mechanism is used to handle memory alignment things. `int`s are also checked because they are sometimes used to represent pointers. see: https://github.c...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Performance]: Arguments `EM` and `num_valid_tokens` of `fused_moe_kernel` should be set to `do_not_specialize` performance;stale ### Proposal to improve performance The `fused_moe_kernel` is implemented with Triton. Du...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ` of `fused_moe_kernel` should be set to `do_not_specialize` performance;stale ### Proposal to improve performance The `fused_moe_kernel` is implemented with Triton. During runtime, Triton checks all kernel arguments of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
