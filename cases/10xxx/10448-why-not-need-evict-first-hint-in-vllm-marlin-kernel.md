# vllm-project/vllm#10448: Why not need evict_first Hint in vllm Marlin kernel？

| 字段 | 值 |
| --- | --- |
| Issue | [#10448](https://github.com/vllm-project/vllm/issues/10448) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why not need evict_first Hint in vllm Marlin kernel？

### Issue 正文摘录

Hi, I want to know why the marlin kernel in vllm do not need evict_first hint when copy B from global to shared memory. https://github.com/vllm-project/vllm/blob/7abba39ee64c1e2c84f48d7c38b2cd1c24bb0ebb/csrc/quantization/gptq_marlin/marlin.cuh#L71 As this optimization is specifically mentioned in the Marlin's paper. https://github.com/IST-DASLab/marlin/blob/1f25790bdd49fba53106164a24666dade68d7c90/marlin/marlin_cuda_kernel.cu#L75

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: csrc/quantization/gptq_marlin/marlin.cuh#L71 As this optimization is specifically mentioned in the Marlin's paper. https://github.com/IST-DASLab/marlin/blob/1f25790bdd49fba53106164a24666dade68d7c90/marlin/marlin_cuda_ke...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: com/vllm-project/vllm/blob/7abba39ee64c1e2c84f48d7c38b2cd1c24bb0ebb/csrc/quantization/gptq_marlin/marlin.cuh#L71 As this optimization is specifically mentioned in the Marlin's paper. https://github.com/IST-DASLab/marlin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ASLab/marlin/blob/1f25790bdd49fba53106164a24666dade68d7c90/marlin/marlin_cuda_kernel.cu#L75
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Why not need evict_first Hint in vllm Marlin kernel？ stale Hi, I want to know why the marlin kernel in vllm do not need evict_first hint when copy B from global to shared memory. https://github.com/vllm-project/vllm/blo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
