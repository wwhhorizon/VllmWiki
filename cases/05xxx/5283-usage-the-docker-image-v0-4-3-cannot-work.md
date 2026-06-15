# vllm-project/vllm#5283: [Usage]: the docker image v0.4.3 cannot work

| 字段 | 值 |
| --- | --- |
| Issue | [#5283](https://github.com/vllm-project/vllm/issues/5283) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: the docker image v0.4.3 cannot work

### Issue 正文摘录

### Your current environment vllm-openai_1 | (RayWorkerWrapper pid=3487) ERROR 06-05 16:30:08 worker_base.py:148] RuntimeError: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 804: forward compatibility was attempted on non supported HW ### How would you like to use vllm everything is good in docker v0.3.3, what should I do to use v0.4.3?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Usage]: the docker image v0.4.3 cannot work usage ### Your current environment vllm-openai_1 | (RayWorkerWrapper pid=3487) ERROR 06-05 16:30:08 worker_base.py:148] RuntimeError: Unexpected error from cudaGetDeviceCount...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: R 06-05 16:30:08 worker_base.py:148] RuntimeError: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 804: forward com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
