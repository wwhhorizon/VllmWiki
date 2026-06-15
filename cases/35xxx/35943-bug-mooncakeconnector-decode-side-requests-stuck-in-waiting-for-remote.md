# vllm-project/vllm#35943: [Bug]: [MooncakeConnector] Decode side requests stuck in WAITING_FOR_REMOTE_KVS indefinitely on transfer failure, causing HBM leak

| 字段 | 值 |
| --- | --- |
| Issue | [#35943](https://github.com/vllm-project/vllm/issues/35943) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [MooncakeConnector] Decode side requests stuck in WAITING_FOR_REMOTE_KVS indefinitely on transfer failure, causing HBM leak

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary In the Mooncake P/D disaggregation connector, when a KV transfer from P to D fails (due to P timeout, P crash, or network interruption), the D-side request remains stuck in `WAITING_FOR_REMOTE_KVS` state permanently. The allocated KV cache blocks are never freed and cannot be preempted, leading to a progressive HBM leak that eventually stalls the entire decode engine. ## Root Cause ### 1. No timeout on D-side `WAITING_FOR_REMOTE_KVS` On the P side, `SendBlockMeta.expire_time` is correctly set and checked in `fetch_finished_sending_reqs()`, which forces block release after `VLLM_MOONCAKE_ABORT_REQUEST_TIMEOUT` (default 480 s). On the D side, the equivalent field exists but is **never assigned**: ```python # mooncake_connector.py @dataclass class PullReqMeta: # Set expire time to avoid infinitely sending requests. expire_time: float = float("inf") # never set anywhere in code ``` ### 2. Transfer errors are silently dropped In `receive_kv_from_single_worker`, when `response.status == MooncakeXferResponseStatus.ERROR`, only logs an error: ```python ret_msg = await sock.recv() response = self._xfer_resp_decoder.decode(ret_m...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: [MooncakeConnector] Decode side requests stuck in WAITING_FOR_REMOTE_KVS indefinitely on transfer failure, causing HBM leak bug;stale ### Your current environment ### 🐛 Describe the bug ## Summary In the Mooncake...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ns stuck in `WAITING_FOR_REMOTE_KVS` state permanently. The allocated KV cache blocks are never freed and cannot be preempted, leading to a progressive HBM leak that eventually stalls the entire decode engine. ## Root C...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ck in `WAITING_FOR_REMOTE_KVS` state permanently. The allocated KV cache blocks are never freed and cannot be preempted, leading to a progressive HBM leak that eventually stalls the entire decode engine. ## Root Cause #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
