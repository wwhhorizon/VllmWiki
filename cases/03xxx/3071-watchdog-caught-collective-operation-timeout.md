# vllm-project/vllm#3071: Watchdog caught collective operation timeout

| 字段 | 值 |
| --- | --- |
| Issue | [#3071](https://github.com/vllm-project/vllm/issues/3071) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Watchdog caught collective operation timeout

### Issue 正文摘录

vllm v0.3.1 running for 7 days. error in allreduce: `(RayWorkerVllm pid=1394) [E ProcessGroupNCCL.cpp:475] [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=4967570, OpType=ALLREDUCE, NumelIn=73728, NumelOut=73728, Timeout(ms)=1800000) ran for 1800542 milliseconds before timing out.`

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
