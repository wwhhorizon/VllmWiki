# vllm-project/vllm#32138: [CI Failure]: DeepSeek-R1-W8A8-longseq A3 multi-node run failed

| 字段 | 值 |
| --- | --- |
| Issue | [#32138](https://github.com/vllm-project/vllm/issues/32138) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: DeepSeek-R1-W8A8-longseq A3 multi-node run failed

### Issue 正文摘录

### Name of failing test DeepSeek-R1-W8A8-longseq ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` (Worker_PCP1_TP4_DCP4_EP12 pid=1195585) INFO 01-12 01:31:33 [mooncake_connector.py:160] Force freed request: chatcmpl-ef4d6818-d419-4850-9b95-a3219a353310 (EngineCore_DP0 pid=1194930) INFO 01-12 01:31:33 [mooncake_connector.py:1050] Delaying free of 1 blocks for request chatcmpl-d3a162d1-e802-40fa-a4ad-a6c037446f4d (APIServer pid=1194908) INFO: 172.22.0.188:41572 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 172.22.0.188:57484 - "POST /v1/chat/completions HTTP/1.1" 200 OK (EngineCore_DP0 pid=1194930) INFO 01-12 01:31:33 [mooncake_connector.py:1050] Delaying free of 1 blocks for request chatcmpl-615c1b16-028d-46dd-acd5-bd85769b0fd7 (APIServer pid=1194908) INFO: 172.22.0.188:41582 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 172.22.0.188:57512 - "POST /v1/chat/completions HTTP/1.1" 200 OK (APIServer pid=1194908) INFO: 172.22.0.212:38814 - "GET /health HTTP/1.1" 200 OK (EngineCore_DP0 pid=1194930) INFO 01-12 01:31:36 [mooncake_connector.py:1050] Delaying fre...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: pid=1195585) INFO 01-12 01:31:33 [mooncake_connector.py:160] Force freed request: chatcmpl-ef4d6818-d419-4850-9b95-a3219a353310 (EngineCore_DP0 pid=1194930) INFO 01-12 01:31:33 [mooncake_connector.py:1050] Delaying free...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: pSeek-R1-W8A8-longseq ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` (Worker_PCP1_TP4_DCP4_EP12 pid...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 0.3 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 22.1%, Prefix cache hit rate: 0.0%, External prefix cache hit rate: 0.0% (Worker_PCP1_TP6_DCP6_EP14 pid=1195701) INFO 01-12 01:31:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -failure ### Name of failing test DeepSeek-R1-W8A8-longseq ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: -R1-W8A8-longseq A3 multi-node run failed ci-failure ### Name of failing test DeepSeek-R1-W8A8-longseq ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
