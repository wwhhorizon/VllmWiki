# vllm-project/vllm#5328: [Bug]: vLLM does not support virtual GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#5328](https://github.com/vllm-project/vllm/issues/5328) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM does not support virtual GPU

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug error reported by https://github.com/vllm-project/vllm/issues/4587 . we need to avoid initializing nccl when the world size is 1.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vLLM does not support virtual GPU bug;unstale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug error reported by https://github.com/vllm-project/vllm/issues/45...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
