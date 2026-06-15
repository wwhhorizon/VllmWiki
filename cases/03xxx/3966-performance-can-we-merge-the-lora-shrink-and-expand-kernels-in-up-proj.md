# vllm-project/vllm#3966: [Performance]: Can we merge the lora shrink and expand kernels in up_proj?

| 字段 | 值 |
| --- | --- |
| Issue | [#3966](https://github.com/vllm-project/vllm/issues/3966) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Can we merge the lora shrink and expand kernels in up_proj?

### Issue 正文摘录

### Proposal to improve performance ![image](https://github.com/vllm-project/vllm/assets/26128514/e269575f-712e-4024-ab96-09aeff4a6218) ### Report of performance regression I notice the up_proj part uses two shrink and expand kernels to calculate the adapter. Can we merge them just like how we merge the two gemms in the base model up_proj? ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: pter. Can we merge them just like how we merge the two gemms in the base model up_proj? ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) _No response_
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: calculate the adapter. Can we merge them just like how we merge the two gemms in the base model up_proj? ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) _No r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Can we merge the lora shrink and expand kernels in up_proj? performance;stale ### Proposal to improve performance ![image](https://github.com/vllm-project/vllm/assets/26128514/e269575f-712e-4024-ab96-09aeff4a6218) ### R...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 6128514/e269575f-712e-4024-ab96-09aeff4a6218) ### Report of performance regression I notice the up_proj part uses two shrink and expand kernels to calculate the adapter. Can we merge them just like how we merge the two...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
