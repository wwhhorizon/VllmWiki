# vllm-project/vllm#6295: pthread_create failed: Resource temporarily unavailable 

| 字段 | 值 |
| --- | --- |
| Issue | [#6295](https://github.com/vllm-project/vllm/issues/6295) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> pthread_create failed: Resource temporarily unavailable 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug It is text of error: Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. 2024-07-10 15:24:06,387 INFO worker.py:1771 -- Started a local Ray instance. E0710 15:24:06.605366961 2474524 thd.cc:157] pthread_create failed: Resource temporarily unavailable [2024-07-10 15:24:06,819 E 2474429 2474429] core_worker.cc:251: Failed to register worker 01000000ffffffffffffffffffffffffffffffffffffffffffffffff to Raylet. IOError: [RayletClient] Unable to register worker with raylet. No such file or directory The GPU server administrators have refused to increase the thread limit, which is currently capped at 4096. I would like to know if there is any method to run models across multiple GPUs under the 4096 thread limit.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: on collect_env.py` ``` ### 🐛 Describe the bug It is text of error: Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. 2024-07-10 15:24:06,387 INFO worke...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ently capped at 4096. I would like to know if there is any method to run models across multiple GPUs under the 4096 thread limit.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: pthread_create failed: Resource temporarily unavailable bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug It is text of error: Special tokens have been added...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
