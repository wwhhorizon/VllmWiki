# vllm-project/vllm#2107: Any optimization options for H100?

| 字段 | 值 |
| --- | --- |
| Issue | [#2107](https://github.com/vllm-project/vllm/issues/2107) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Any optimization options for H100?

### Issue 正文摘录

Thank you for your hard work. The performance difference between A100 and H100 is not significant. I used the official VLLM image 0.2.4 on Docker Hub. I set the prompt and completion to 500, and both A100 and H100 take 19 seconds. Are there any settings to optimize performance on H100?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ance difference between A100 and H100 is not significant. I used the official VLLM image 0.2.4 on Docker Hub. I set the prompt and completion to 500, and both A100 and H100 take 19 seconds. Are there any settings to opt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Any optimization options for H100? performance;stale Thank you for your hard work. The performance difference between A100 and H100 is not significant. I used the official VLLM image 0.2.4 on Docker Hub. I set the promp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Any optimization options for H100? performance;stale Thank you for your hard work. The performance difference between A100 and H100 is not significant. I used the official VLLM image 0.2.4 on Docker Hub. I set the promp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
