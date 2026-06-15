# vllm-project/vllm#4059: [Feature]: Automatic Prefix Caching on T4

| 字段 | 值 |
| --- | --- |
| Issue | [#4059](https://github.com/vllm-project/vllm/issues/4059) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Automatic Prefix Caching on T4

### Issue 正文摘录

### 🚀 The feature, motivation and pitch APC is not supported on T4 due to the attention kernels requiring > compute capability 8.0 (Ampere). T4 is widely used, and Automatic Prefix Caching is a key feature. APC is crucial for enhancing the inference performance, given the T4's extensive use in both cloud and on-premises environments, enabling APC is a key feature for vllm on this platform. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: is not supported on T4 due to the attention kernels requiring > compute capability 8.0 (Ampere). T4 is widely used, and Automatic Prefix Caching is a key feature. APC is crucial for enhancing the inference performance,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: is widely used, and Automatic Prefix Caching is a key feature. APC is crucial for enhancing the inference performance, given the T4's extensive use in both cloud and on-premises environments, enabling APC is a key featu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Automatic Prefix Caching on T4 feature request ### 🚀 The feature, motivation and pitch APC is not supported on T4 due to the attention kernels requiring > compute capability 8.0 (Ampere). T4 is widely used, a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
