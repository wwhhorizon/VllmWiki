# vllm-project/vllm#21170: [Bug]: How to Resolve KVC Transmission Timeout

| 字段 | 值 |
| --- | --- |
| Issue | [#21170](https://github.com/vllm-project/vllm/issues/21170) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: How to Resolve KVC Transmission Timeout

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Proposed Changes 1. The `get_finished` function returns requests that have timed out during reception. 2. The _update_waiting_for_remote_kv function handles requests that have timed out during reception. def get_finished( self, finished_req_ids: set[str] ) -> tuple[Optional[set[str]], Optional[set[str]]]: """ """ return save_finished, load_finished, load_timeout def _update_waiting_for_remote_kv(self, request: Request) -> bool: """ """ if request.request_id in self.timeout_recving_kv_req_ids: self.handle_timeout_request(request) return True ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: How to Resolve KVC Transmission Timeout bug;stale ### Your current environment ### 🐛 Describe the bug Proposed Changes 1. The `get_finished` function returns requests that have timed out during reception. 2. The...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: How to Resolve KVC Transmission Timeout bug;stale ### Your current environment ### 🐛 Describe the bug Proposed Changes 1. The `get_finished` function returns requests that have timed out during reception. 2. The...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
