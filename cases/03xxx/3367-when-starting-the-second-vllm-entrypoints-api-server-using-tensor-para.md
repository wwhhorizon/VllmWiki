# vllm-project/vllm#3367: When  starting the second vllm.entrypoints.api_server using tensor parallel in a single node, the second vllm api_server Stuck in " Started a local Ray instance." OR  "Failed to register worker 01000000ffffffffffffffffffffffffffffffffffffffffffffffff to Raylet. IOError: [RayletClient] Unable to register worker with raylet. No such file or directory" 

| 字段 | 值 |
| --- | --- |
| Issue | [#3367](https://github.com/vllm-project/vllm/issues/3367) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> When  starting the second vllm.entrypoints.api_server using tensor parallel in a single node, the second vllm api_server Stuck in " Started a local Ray instance." OR  "Failed to register worker 01000000ffffffffffffffffffffffffffffffffffffffffffffffff to Raylet. IOError: [RayletClient] Unable to register worker with raylet. No such file or directory" 

### Issue 正文摘录

![image](https://github.com/vllm-project/vllm/assets/145545818/2c37e30e-83c9-45f1-b73b-5a04f3583318) ![image](https://github.com/vllm-project/vllm/assets/145545818/ab96caeb-d3da-465f-a63a-5a70d082f409) As I mentioned above, when I try to start two vllm api_servers, both using tensor-parallel(and size =2), I find the SECOND api_server can't run successfully (while the first one is ok). Also, I find that using top command, it shows there are many ray:IDLE. ![image](https://github.com/vllm-project/vllm/assets/145545818/cc0dae47-baaf-4416-be7a-18da7ce89f21)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ient] Unable to register worker with raylet. No such file or directory" stale ![image](https://github.com/vllm-project/vllm/assets/145545818/2c37e30e-83c9-45f1-b73b-5a04f3583318) ![image](https://github.com/vllm-project...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
