# vllm-project/vllm#14680: [Feature]: Memory interleaving: improve performance by increasing memory bandwidth between CPU and system memory

| 字段 | 值 |
| --- | --- |
| Issue | [#14680](https://github.com/vllm-project/vllm/issues/14680) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Memory interleaving: improve performance by increasing memory bandwidth between CPU and system memory

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Inference speed on CPU is often bound by available memory bandwidth (try with [pcm-memory](https://github.com/intel/pcm)). On Linux systems with multiple memory nodes and physical memory controllers, the OS typically allocates memory from the node that is closest to the CPU where the allocating process is running. This results in using very few nodes, and therefore very few physical memory channels to access the model during inference. Therefore memory bandwidth on these systems is typically limited by the bandwidth of the few channels, leaving most of the other channels underutilized. However, Linux provides a mechanism to interleave allocated memory across any given set of memory nodes ([set_mempolicy](https://man7.org/linux/man-pages/man2/set_mempolicy.2.html)). This feature request is about enabling vllm users to take advantage of this mechanism and use all memory channels that help speeding up inference. The speed up is significant on many platforms. Unfortunately, there is no generic logic to select interleaved memory nodes for best performance. On some hardware architectures selecting all nodes is the best, while on some other archite...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t of the other channels underutilized. However, Linux provides a mechanism to interleave allocated memory across any given set of memory nodes ([set_mempolicy](https://man7.org/linux/man-pages/man2/set_mempolicy.2.html)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ew nodes, and therefore very few physical memory channels to access the model during inference. Therefore memory bandwidth on these systems is typically limited by the bandwidth of the few channels, leaving most of the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nce by increasing memory bandwidth between CPU and system memory feature request;stale ### 🚀 The feature, motivation and pitch Inference speed on CPU is often bound by available memory bandwidth (try with [pcm-memory](h...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
