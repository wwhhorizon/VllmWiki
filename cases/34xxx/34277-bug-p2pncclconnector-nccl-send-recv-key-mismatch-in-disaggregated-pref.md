# vllm-project/vllm#34277: [Bug]: P2pNcclConnector NCCL send/recv key mismatch in disaggregated prefill XpYd architecture due to assign_request_id() random suffix

| 字段 | 值 |
| --- | --- |
| Issue | [#34277](https://github.com/vllm-project/vllm/issues/34277) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: P2pNcclConnector NCCL send/recv key mismatch in disaggregated prefill XpYd architecture due to assign_request_id() random suffix

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running disaggregated serving using `P2pNcclConnector` with the XpYd proxy architecture (`examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/`), the NCCL P2P KV cache transfer between the Prefill instance and Decode instance **hangs indefinitely** (or times out). The Prefill side sends KV data under one key, but the Decode side attempts to receive under a different key, so they never match. ### Root Cause The proxy server (`disagg_proxy_p2p_nccl_xpyd.py`) generates a single `request_id` containing both the prefill and decode ZMQ addresses and passes it to both vLLM instances via the `X-Request-Id` HTTP header: ```python # In the proxy: request_id = ( f"___prefill_addr_{prefill_zmq_addr}___decode_addr_" f"{decode_zmq_addr}_{random_uuid()}" ) ``` Both the Prefill and Decode vLLM instances receive **the same** `request_id`. However, inside each vLLM instance, `InputProcessor.assign_request_id()` replaces the `request_id` with an internal one by appending a random 8-character hex suffix: ```python # In vllm/v1/engine/input_processor.py: @staticmethod def assign_request_id(request: EngineCoreRequest): request.external_re...

## 现有链接修复摘要

#34747 fix: use external_req_id for P2P NCCL keys in disaggregated prefill | #44179 fix offline disaggregated prefill request ids for P2P NCCL

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: P2pNcclConnector NCCL send/recv key mismatch in disaggregated prefill XpYd architecture due to assign_request_id() random suffix bug;stale ### Your current environment ### 🐛 Describe the bug When running disaggre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cache;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: P2pNcclConnector NCCL send/recv key mismatch in disaggregated prefill XpYd architecture due to assign_request_id() random suffix bug;stale ### Your current environment ### 🐛 Describe the bug When running disaggre...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: P2pNcclConnector NCCL send/recv key mismatch in disaggregated prefill XpYd architecture due to assign_request_id() random suffix bug;stale ### Your current environment ### 🐛 Describe the bug When running disaggre...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: on Decode **never match**: ``` Prefill sends with key: "..._ -a1b2c3d4#model.layers.0.self_attn" Decode recvs with key: "..._ -e5f6g7h8#model.layers.0.self_attn" ^^^^^^^^^ MISMATCH! ``` Additionally, `parse_request_id()...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34747](https://github.com/vllm-project/vllm/pull/34747) | closes_keyword | 0.95 | fix: use external_req_id for P2P NCCL keys in disaggregated prefill | Fixes #34277 ### Root Cause In the XpYd disaggregated serving architecture, the proxy generates a single `request_id` containing both prefill and decode ZMQ addresses. However, ` |
| [#44179](https://github.com/vllm-project/vllm/pull/44179) | mentioned | 0.6 | fix offline disaggregated prefill request ids for P2P NCCL | r`, including work referenced in #33947, #42931, #42839, and possibly #34277, but it does not try to generalize that broader effort. - Instead, it keeps the scope narrow by fixing… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
