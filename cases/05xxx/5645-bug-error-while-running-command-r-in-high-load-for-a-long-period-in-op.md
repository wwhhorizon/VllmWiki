# vllm-project/vllm#5645: [Bug]: Error while running command-r in high load for a long period in OpenBLAS on 2 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#5645](https://github.com/vllm-project/vllm/issues/5645) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error while running command-r in high load for a long period in OpenBLAS on 2 GPUs

### Issue 正文摘录

### Your current environment Running within on-prem k8s environment with official docker image. ### 🐛 Describe the bug ``` OpenBLAS blas_thread_init: pthread_create: Resource temporarily unavailable OpenBLAS blas_thread_init: RLIMIT_NPROC X current, X max ``` after little search found that adding `export OPENBLAS_NUM_THREADS=your cpu cores` it should work but than get ``` terminate called after throwing an instance of 'std::system_error' what(): Resource temporarily unavailable Aborted ``` [error in stack overflow](https://stackoverflow.com/questions/52026652/openblas-blas-thread-init-pthread-create-resource-temporarily-unavailable) it says that if you add ``` import os os.environ['OPENBLAS_NUM_THREADS'] = '1' ``` it works for some reason so I wish to add that to the code

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: our current environment Running within on-prem k8s environment with official docker image. ### 🐛 Describe the bug ``` OpenBLAS blas_thread_init: pthread_create: Resource temporarily unavailable OpenBLAS blas_thread_init...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nBLAS blas_thread_init: RLIMIT_NPROC X current, X max ``` after little search found that adding `export OPENBLAS_NUM_THREADS=your cpu cores` it should work but than get ``` terminate called after throwing an instance of...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nning command-r in high load for a long period in OpenBLAS on 2 GPUs bug;stale ### Your current environment Running within on-prem k8s environment with official docker image. ### 🐛 Describe the bug ``` OpenBLAS blas_thr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
