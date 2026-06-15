# vllm-project/vllm#39732: fix: handle load failures gracefully in offloading_connector instead of crashing

| 字段 | 值 |
| --- | --- |
| Issue | [#39732](https://github.com/vllm-project/vllm/issues/39732) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> fix: handle load failures gracefully in offloading_connector instead of crashing

### Issue 正文摘录

## Summary The `OffloadingConnectorWorkerSide` in `offloading_connector.py` uses `assert success` / `assert transfer_result.success` on the load (GET) path. If a load fails (e.g., file not found, I/O error, corrupted data), the assert crashes the entire vllm worker process. KV cache loads can fail for legitimate reasons (missing files, storage errors, etc.). The process should not crash on load failure — instead, the failure should be properly reported so the scheduler can fall back to recomputation for that request. ## Problem Locations **`offloading_connector.py:644-645`** — load submission: ```python success = self.worker.transfer_async(job_id, transfer_spec) assert success # crashes the process if load submission fails ``` **`offloading_connector.py:670-672`** — load completion: ```python job_id = transfer_result.job_id assert transfer_result.success # crashes the process if load reports failure ``` For load jobs, the failure should be reported back to the scheduler so it can trigger recomputation for the affected request, rather than crashing the worker process.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: fix: handle load failures gracefully in offloading_connector instead of crashing ## Summary The `OffloadingConnectorWorkerSide` in `offloading_connector.py` uses `assert success` / `assert transfer_result.success` on th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n load failure — instead, the failure should be properly reported so the scheduler can fall back to recomputation for that request. ## Problem Locations **`offloading_connector.py:644-645`** — load submission: ```python...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
