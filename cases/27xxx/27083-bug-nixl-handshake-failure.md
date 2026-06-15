# vllm-project/vllm#27083: [Bug]: NIXL handshake failure

| 字段 | 值 |
| --- | --- |
| Issue | [#27083](https://github.com/vllm-project/vllm/issues/27083) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: NIXL handshake failure

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I got this error when running DeepSeek with 2 nodes: 1P1D each with DP=8. Because of this, the decode node fails to get KV cache from the prefill node and re-computes the prompt. ``` (Worker_DP0_EP0 pid=2823482) ERROR 10-16 17:22:56 [nixl_connector.py:815] RuntimeError: Remote NIXL agent engine ID mismatch. Expected 46126a31-6b81 -435d-a116-e3e34a76ded3_dp0,received 96b1c4ff-9edf-4d21-b7cf-975a5f441d03_dp0. (Worker_DP0_EP0 pid=2823482) ERROR 10-16 17:22:56 [nixl_connector.py:827] Handshake failed for request chatcmpl ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: running DeepSeek with 2 nodes: 1P1D each with DP=8. Because of this, the decode node fails to get KV cache from the prefill node and re-computes the prompt. ``` (Worker_DP0_EP0 pid=2823482) ERROR 10-16 17:22:56 [nixl_co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 2:56 [nixl_connector.py:815] RuntimeError: Remote NIXL agent engine ID mismatch. Expected 46126a31-6b81 -435d-a116-e3e34a76ded3_dp0,received 96b1c4ff-9edf-4d21-b7cf-975a5f441d03_dp0. (Worker_DP0_EP0 pid=2823482) ERROR 1...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: :22:56 [nixl_connector.py:815] RuntimeError: Remote NIXL agent engine ID mismatch. Expected 46126a31-6b81 -435d-a116-e3e34a76ded3_dp0,received 96b1c4ff-9edf-4d21-b7cf-975a5f441d03_dp0. (Worker_DP0_EP0 pid=2823482) ERROR...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: odes: 1P1D each with DP=8. Because of this, the decode node fails to get KV cache from the prefill node and re-computes the prompt. ``` (Worker_DP0_EP0 pid=2823482) ERROR 10-16 17:22:56 [nixl_connector.py:815] RuntimeEr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
