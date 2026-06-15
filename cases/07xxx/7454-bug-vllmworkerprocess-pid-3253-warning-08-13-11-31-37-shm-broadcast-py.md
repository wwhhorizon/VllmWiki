# vllm-project/vllm#7454: [Bug]: (VllmWorkerProcess pid=3253) WARNING 08-13 11:31:37 shm_broadcast.py:386] No available block found in 60 second

| 字段 | 值 |
| --- | --- |
| Issue | [#7454](https://github.com/vllm-project/vllm/issues/7454) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: (VllmWorkerProcess pid=3253) WARNING 08-13 11:31:37 shm_broadcast.py:386] No available block found in 60 second

### Issue 正文摘录

### Your current environment vllm update to latest version , it happened that (VllmWorkerProcess pid=3253) WARNING 08-13 11:31:37 shm_broadcast.py:386] No available block found in 60 second, and the task is hold ,wait for something, it seems not working ### 🐛 Describe the bug (VllmWorkerProcess pid=3253) WARNING 08-13 11:31:37 shm_broadcast.py:386] No available block found in 60 second

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 60 second bug;stale ### Your current environment vllm update to latest version , it happened that (VllmWorkerProcess pid=3253) WARNING 08-13 11:31:37 shm_broadcast.py:386] No available block found in 60 second, and the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cess pid=3253) WARNING 08-13 11:31:37 shm_broadcast.py:386] No available block found in 60 second bug;stale ### Your current environment vllm update to latest version , it happened that (VllmWorkerProcess pid=3253) WARN...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 11:31:37 shm_broadcast.py:386] No available block found in 60 second bug;stale ### Your current environment vllm update to latest version , it happened that (VllmWorkerProcess pid=3253) WARNING 08-13 11:31:37 shm_broadc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nd in 60 second bug;stale ### Your current environment vllm update to latest version , it happened that (VllmWorkerProcess pid=3253) WARNING 08-13 11:31:37 shm_broadcast.py:386] No available block found in 60 second, an...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
