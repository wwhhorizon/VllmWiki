# vllm-project/vllm#18899: [Bug]: Do we really need to implement additional functions for custom_allreduce to serve graph capture?

| 字段 | 值 |
| --- | --- |
| Issue | [#18899](https://github.com/vllm-project/vllm/issues/18899) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Do we really need to implement additional functions for custom_allreduce to serve graph capture?

### Issue 正文摘录

I changed the function when capture customer allreduce from ops.all_reduce(self._ptr, inp, out, 0, 0) to ops.all_reduce(self._ptr, inp, out, self.buffer_ptrs[self.rank], self.max_size). (custom_all_reduce.py line243) and close this condition ”if (status == cudaStreamCaptureStatusActive) “(custom_all_reduce.cuh line542). I ran the kernel test and offline_infer.py and they both get the correct data. I noticed this comment” However, the peer pointers are not known during graph capture time“ in custom_all_reduce.cuh line 384. If we still use the method of copying the inp to the buf that has finished communicating during graph capture, Wouldn't we have no more IPC problems? What is the reason to pass inp as buf directly to allreduce?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: . (custom_all_reduce.py line243) and close this condition ”if (status == cudaStreamCaptureStatusActive) “(custom_all_reduce.cuh line542). I ran the kernel test and offline_infer.py and they both get the correct data. I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nt additional functions for custom_allreduce to serve graph capture? bug;stale I changed the function when capture customer allreduce from ops.all_reduce(self._ptr, inp, out, 0, 0) to ops.all_reduce(self._ptr, inp, out,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: CaptureStatusActive) “(custom_all_reduce.cuh line542). I ran the kernel test and offline_infer.py and they both get the correct data. I noticed this comment” However, the peer pointers are not known during graph capture...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
