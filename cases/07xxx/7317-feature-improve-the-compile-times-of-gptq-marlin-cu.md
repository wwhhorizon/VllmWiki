# vllm-project/vllm#7317: [Feature]: Improve the compile times of gptq_marlin.cu

| 字段 | 值 |
| --- | --- |
| Issue | [#7317](https://github.com/vllm-project/vllm/issues/7317) |
| 状态 | closed |
| 标签 | good first issue;feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Improve the compile times of gptq_marlin.cu

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The compile times for the GPTQ Marlin kernels are quite long, and have become painful for developers. `gptq_marlin.cu` is monolithic and heavily templated, and many cases of the marlin kernel are instantiated. Compile times got particularly bad in #6612, where the number of cases being compiled approximately doubled. Namely, 320 kernels are defined in this block of code in `gptq_marlin.cu`: ``` GPTQ_CALL_IF(4, 16, 4, 256) GPTQ_CALL_IF(4, 8, 8, 256) GPTQ_CALL_IF(4, 8, 4, 128) GPTQ_CALL_IF(4, 4, 8, 128) GPTQ_CALL_IF(8, 16, 4, 256) GPTQ_CALL_IF(8, 8, 8, 256) GPTQ_CALL_IF(8, 8, 4, 128) GPTQ_CALL_IF(8, 4, 8, 128) AWQ_CALL_IF(4, 16, 4, 256) AWQ_CALL_IF(4, 8, 8, 256) AWQ_CALL_IF(4, 8, 4, 128) AWQ_CALL_IF(4, 4, 8, 128) AWQ_CALL_IF(8, 16, 4, 256) AWQ_CALL_IF(8, 8, 8, 256) AWQ_CALL_IF(8, 8, 4, 128) AWQ_CALL_IF(8, 4, 8, 128) ``` I think the best option for improving this right now it to split up `gptq_marlin.cu` into multiple files so that compilation can be parallelized. ### Details: First, this function and its dependencies should be moved into a file called something like `gptq_marlin_kernel.cuh` ``` template shared // fetch pipeline const bool has_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Improve the compile times of gptq_marlin.cu good first issue;feature request;stale ### 🚀 The feature, motivation and pitch The compile times for the GPTQ Marlin kernels are quite long, and have become painful...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 16x16 blocks // with a separate quantization scale > __global__ void Marlin { ... } ``` Next, we need to spread the instantiations of the template function across a _sensible_ number of .cu files. Too many will likely b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e]: Improve the compile times of gptq_marlin.cu good first issue;feature request;stale ### 🚀 The feature, motivation and pitch The compile times for the GPTQ Marlin kernels are quite long, and have become painful for de...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: q_marlin.cu` -- drastically smaller than it is currently. Should contain dispatch logic and include `gpq_marlin.cuh` * `gptq_marlin.cuh` -- Should only declare the Marlin configs that have been defined in the new files...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: igs. Name them better than I did here. * `gptq_marlin.cu` -- drastically smaller than it is currently. Should contain dispatch logic and include `gpq_marlin.cuh` * `gptq_marlin.cuh` -- Should only declare the Marlin con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
