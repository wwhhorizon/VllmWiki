# vllm-project/vllm#5866: [Bug]: The end_sync operation inside the cross_device_reduce_2stage kernel sometimes deadlocks because it can't wait for the end signal.

| 字段 | 值 |
| --- | --- |
| Issue | [#5866](https://github.com/vllm-project/vllm/issues/5866) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The end_sync operation inside the cross_device_reduce_2stage kernel sometimes deadlocks because it can't wait for the end signal.

### Issue 正文摘录

### Your current environment When we stress test the VLLM model inference on NVIDIA A100 or H800, this problem will be reproduced. ### 🐛 Describe the bug In the start_sync function, although the write operations to the start and end signals are volatile, this does not guarantee that the order of these two operations will not be reordered by NVCC. According to the CUDA Memory Consistency Model manual, the order of two ld.volatile operations is only guaranteed not to change when they read and write to the same memory location ([link](https://docs.nvidia.com/cuda/parallel-thread-execution/#data-movement-and-conversion-instructions-ld)). The start and end signals are not even on the same cache line. Please see [CUDA Memory Consistency Model ](https://docs.nvidia.com/cuda/parallel-thread-execution/#memory-consistency-model). Once the order of line 135 and line 140 is reversed, it's possible that other devices' write operations to set end to 1 could happen before this device's operation to set end to 0, resulting in a deadlock in the while loop on line 165. To solve this problem, enhance the dependency between the operations on line 135 and line 140, for example: ``` self_sg->end[blockI...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: d not to change when they read and write to the same memory location ([link](https://docs.nvidia.com/cuda/parallel-thread-execution/#data-movement-and-conversion-instructions-ld)). The start and end signals are not even...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rent environment When we stress test the VLLM model inference on NVIDIA A100 or H800, this problem will be reproduced. ### 🐛 Describe the bug In the start_sync function, although the write operations to the start and en...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nd_sync operation inside the cross_device_reduce_2stage kernel sometimes deadlocks because it can't wait for the end signal. bug;stale ### Your current environment When we stress test the VLLM model inference on NVIDIA...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: st the VLLM model inference on NVIDIA A100 or H800, this problem will be reproduced. ### 🐛 Describe the bug In the start_sync function, although the write operations to the start and end signals are volatile, this does...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: n the operations on line 135 and line 140, for example: ``` self_sg->end[blockIdx.x][threadIdx.x] = 0; __threadfence_block(); sg.signals[threadIdx.x]->start[blockIdx.x][rank] = 1; ``` Another way to solve likes this: ``...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
