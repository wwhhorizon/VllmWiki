# vllm-project/vllm#338: GPU Stuck

| 字段 | 值 |
| --- | --- |
| Issue | [#338](https://github.com/vllm-project/vllm/issues/338) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GPU Stuck

### Issue 正文摘录

I am using the vllm 0.1.1 version, Ubuntu 18.04. There is a server with 4 T4 GPU cards. I started 4 tasks simultaneously. But it seems that 2 out of 4 GPU was stuck. May I ask why? ### multi-GPU offline inference And When I try to run multi-GPU offline inference, it returns an error: the actor is dead because its worker process has died. Worker exit type: SYSTEM_ERROR Worker exit detail: Worker unexpectedly exits with a connection error code 2. End of file. There are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected errors. The actor never ran - it was cancelled before it started running. Unhandled exception: St13runtime_error. what(): NCCL Error 5: invalid usage

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: GPU Stuck bug I am using the vllm 0.1.1 version, Ubuntu 18.04. There is a server with 4 T4 GPU cards. I started 4 tasks simultaneously. But it seems that 2 out of 4 GPU was stuck. May I ask why? ### multi-GPU offline in...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected erro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
