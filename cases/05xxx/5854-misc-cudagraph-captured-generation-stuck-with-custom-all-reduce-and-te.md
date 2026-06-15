# vllm-project/vllm#5854: [Misc]: CUDAGraph captured generation stuck with custom_all_reduce and tensor_parallel=2

| 字段 | 值 |
| --- | --- |
| Issue | [#5854](https://github.com/vllm-project/vllm/issues/5854) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: CUDAGraph captured generation stuck with custom_all_reduce and tensor_parallel=2

### Issue 正文摘录

### Anything you want to discuss about vllm. # Issue I have been experimenting on CUDAGraph captured generation with my own transformer model implementation, using [custom all-reduce](https://github.com/vllm-project/vllm/blob/main/csrc/custom_all_reduce.cuh) in vLLM as replacement for pytorch all-reduce. CUDAGraph capturing worked well until I tried a certain parallel strategy (tensor parallel = pipeline parallel = data parallel = 2, 8 GPUs). In this configuration, the generation was randomly stuck when replaying the captured graph. This problem did not appear in any other parallel strategies with 8 GPUs. I wonder if anyone had encountered the same problem before? I observed that custom all-reduce use `cross_device_reduce_1stage` only when world_size=2 (and data of small sizes when world_size>2) instead of `cross_device_reduce_2stage`. Could this be the root cause of the problem? Thanks for your answers in advance!

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Misc]: CUDAGraph captured generation stuck with custom_all_reduce and tensor_parallel=2 stale ### Anything you want to discuss about vllm. # Issue I have been experimenting on CUDAGraph captured generation with my own...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n experimenting on CUDAGraph captured generation with my own transformer model implementation, using [custom all-reduce](https://github.com/vllm-project/vllm/blob/main/csrc/custom_all_reduce.cuh) in vLLM as replacement...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: h captured generation stuck with custom_all_reduce and tensor_parallel=2 stale ### Anything you want to discuss about vllm. # Issue I have been experimenting on CUDAGraph captured generation with my own transformer mode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
