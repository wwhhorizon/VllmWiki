# vllm-project/vllm#2393: Improve Cuda compatibility of vllm-openai image

| 字段 | 值 |
| --- | --- |
| Issue | [#2393](https://github.com/vllm-project/vllm/issues/2393) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Improve Cuda compatibility of vllm-openai image

### Issue 正文摘录

Currently the 'https://hub.docker.com/r/vllm/vllm-openai/' image uses Cuda 12.1 - this runs into a lot of cuda versioning issues depending on the drivers used on the underlying GPU. This makes the image an inconsistent starting point for running on services like vast ai or runpod. Could the docker image be updated to more dynamically support cuda versions from 11.8 and up?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ty of vllm-openai image feature request;stale Currently the 'https://hub.docker.com/r/vllm/vllm-openai/' image uses Cuda 12.1 - this runs into a lot of cuda versioning issues depending on the drivers used on the underly...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Improve Cuda compatibility of vllm-openai image feature request;stale Currently the 'https://hub.docker.com/r/vllm/vllm-openai/' image uses Cuda 12.1 - this runs into a lot of cuda versioning issues depending on the dri...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Improve Cuda compatibility of vllm-openai image feature request;stale Currently the 'https://hub.docker.com/r/vllm/vllm-openai/' image uses Cuda 12.1 - this runs into a lot of cuda versioning issues depending on the dri...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
