# vllm-project/vllm#37037: [Bug]: FlatLogprobs empty slice crashes with IndexError and delta-mode logprobs[-0:] returns stale data

| 字段 | 值 |
| --- | --- |
| Issue | [#37037](https://github.com/vllm-project/vllm/issues/37037) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: FlatLogprobs empty slice crashes with IndexError and delta-mode logprobs[-0:] returns stale data

### Issue 正文摘录

### Your current environment Latest main branch of vllm. ### Describe the bug I found two related bugs in the logprobs handling code: **1. FlatLogprobs.__getitem__ crashes on empty slices** In `vllm/logprobs.py`, the `FlatLogprobs.__getitem__` method unconditionally accesses `self.start_indices[index][0]` and `self.end_indices[index][-1]` when called with a slice. If the slice result is empty (e.g., `logprobs[0:0]`, `logprobs[5:5]`), these accesses raise `IndexError` because you're indexing into an empty list. This violates the Python sequence protocol -- standard `list` returns `[]` for empty slices. Since `FlatLogprobs` implements `MutableSequence`, it should do the same. **2. Delta-mode logprobs returns all accumulated logprobs instead of none** In `vllm/v1/engine/output_processor.py` line 396: ```python if delta and logprobs: logprobs = logprobs[-len(token_ids) :] ``` When `token_ids` is an empty list (length 0), Python evaluates `-0` as `0`, so `logprobs[-0:]` becomes `logprobs[0:]`, which returns ALL accumulated logprobs instead of an empty slice. In delta streaming mode, this would send stale/duplicate logprobs data to the client. ### Steps to reproduce ```python from vllm....

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: empty slice crashes with IndexError and delta-mode logprobs[-0:] returns stale data ### Your current environment Latest main branch of vllm. ### Describe the bug I found two related bugs in the logprobs handling code: *...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ta-mode logprobs[-0:] returns stale data ### Your current environment Latest main branch of vllm. ### Describe the bug I found two related bugs in the logprobs handling code: **1. FlatLogprobs.__getitem__ crashes on emp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: is would send stale/duplicate logprobs data to the client. ### Steps to reproduce ```python from vllm.logprobs import FlatLogprobs, Logprob lp = FlatLogprobs() lp.append({1: Logprob(logprob=-0.5, rank=1, decoded_token="...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ata to the client. ### Steps to reproduce ```python from vllm.logprobs import FlatLogprobs, Logprob lp = FlatLogprobs() lp.append({1: Logprob(logprob=-0.5, rank=1, decoded_token="a")}) lp.append({2: Logprob(logprob=-1.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
