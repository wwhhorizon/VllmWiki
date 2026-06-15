# vllm-project/vllm#859: start vllm.entrypoints.api_server model vicuna-13b-v1.3  error: Fatal Python error: Bus error

| 字段 | 值 |
| --- | --- |
| Issue | [#859](https://github.com/vllm-project/vllm/issues/859) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> start vllm.entrypoints.api_server model vicuna-13b-v1.3  error: Fatal Python error: Bus error

### Issue 正文摘录

err detail `You are using the legacy behaviour of the . This means that tokens that come after special tokens will not be properly handled. We recommend you to read the related pull request available at https://github.com/huggingface/transformers/pull/24565 (RayWorker pid=3554640) *** SIGBUS received at time=1692931519 on cpu 133 *** (RayWorker pid=3554640) PC: @ 0x7f60c5616291 (unknown) __memset_avx2_erms (RayWorker pid=3554640) @ 0x7f60c60a8cf0 (unknown) (unknown) (RayWorker pid=3554640) [2023-08-25 10:45:19,168 E 3554640 3555230] logging.cc:361: *** SIGBUS received at time=1692931519 on cpu 133 *** (RayWorker pid=3554640) [2023-08-25 10:45:19,168 E 3554640 3555230] logging.cc:361: PC: @ 0x7f60c5616291 (unknown) __memset_avx2_erms (RayWorker pid=3554640) [2023-08-25 10:45:19,168 E 3554640 3555230] logging.cc:361: @ 0x7f60c60a8cf0 (unknown) (unknown) (RayWorker pid=3554640) Fatal Python error: Bus error (RayWorker pid=3554640) 2023-08-25 10:45:21,197 WARNING worker.py:2037 -- A worker died or was killed while executing a task by an unexpected system error. To troubleshoot the problem, check the logs for the dead worker. RayTask ID: ffffffffffffffff781cee214007f7ef2aa9c68501000000...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: start vllm.entrypoints.api_server model vicuna-13b-v1.3 error: Fatal Python error: Bus error err detail `You are using the legacy behaviour of the . This means that tokens that come after special tokens will not be prop...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the legacy behaviour of the . This means that tokens that come after special tokens will not be properly handled. We recommend you to read the related pull request available at https://github.com/huggingface/transformer...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected erro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: will not be properly handled. We recommend you to read the related pull request available at https://github.com/huggingface/transformers/pull/24565 (RayWorker pid=3554640) *** SIGBUS received at time=1692931519 on cpu 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
