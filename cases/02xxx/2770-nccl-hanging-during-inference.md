# vllm-project/vllm#2770: NCCL hanging during inference

| 字段 | 值 |
| --- | --- |
| Issue | [#2770](https://github.com/vllm-project/vllm/issues/2770) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> NCCL hanging during inference

### Issue 正文摘录

with vllm v0.2.7, I saw the nccl hanging for allreduce: ``` [36m(RayWorkerVllm pid=5085)[0m [E ProcessGroupNCCL.cpp:475] [Rank 4] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=20518, OpType=ALLREDUCE, NumelIn=106496, NumelOut=106496, Timeout(ms)=1800000) ran for 1800270 milliseconds before timing out. ``` after switching to v0.3.0(with custom all reduce), it's `gather` ``` (RayWorkerVllm pid=4775) [E ProcessGroupNCCL.cpp:475] [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=369526, OpType=GATHER, NumelIn=4000, NumelOut=0, Timeout(ms)=1800000) ran for 1800252 milliseconds before timing out. ```

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
