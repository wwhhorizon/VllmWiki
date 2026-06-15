# vllm-project/vllm#4653: [Bug]: NCCL timed out during inference

| 字段 | 值 |
| --- | --- |
| Issue | [#4653](https://github.com/vllm-project/vllm/issues/4653) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: NCCL timed out during inference

### Issue 正文摘录

### Your current environment Using: * vllm 0.4.1 * nccl 2.18.1 * pytorch 2.2.1 ### 🐛 Describe the bug During inference I sometimes get this error: ```bash (RayWorkerWrapper pid=2376582) [rank1]:[E ProcessGroupNCCL.cpp:523] [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=50404, OpType=GATHER, NumelIn=8000, NumelOut=0, Timeout(ms)=600000) ran for 600327 milliseconds before timing out. ``` Havn't seen it in earlier versions of vllm, any thoughts?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: or 600327 milliseconds before timing out. ``` Havn't seen it in earlier versions of vllm, any thoughts?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: NCCL timed out during inference bug;stale ### Your current environment Using: * vllm 0.4.1 * nccl 2.18.1 * pytorch 2.2.1 ### 🐛 Describe the bug During inference I sometimes get this error: ```bash (RayWorkerWrapp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
