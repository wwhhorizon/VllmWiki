# vllm-project/vllm#21712: [Bug]: P2PNcclConnector Assertion Error for Chat Completeion Endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#21712](https://github.com/vllm-project/vllm/issues/21712) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: P2PNcclConnector Assertion Error for Chat Completeion Endpoint

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The [example proxy server](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/disagg_proxy_p2p_nccl_xpyd.py) for NCCL xPyD only supports the `/v1/completions` endpoint. When I added the proxy endpoint for the `/v1/chat/completions` endpoint, after sending a few requests, I got the following error: ``` INFO 07-27 21:10:50 [async_llm.py:269] Added request chatcmpl-___prefill_addr_141.211.141.42:10000___decode_addr_141.211.141.42:12000_a43152a1e2ec4997a1fbada755d9b0ec. INFO 07-27 21:10:50 [p2p_nccl_engine.py:45] set_p2p_nccl_context, original_values: {'NCCL_MAX_NCHANNELS': None, 'NCCL_MIN_NCHANNELS': None, 'NCCL_CUMEM_ENABLE': '0', 'NCCL_BUFFSIZE': None, 'NCCL_PROTO': None, 'NCCL_ALGO': None} INFO 07-27 21:10:50 [p2p_nccl_engine.py:195] 🤝ncclCommInitRank Success, 141.211.141.42:10000👉141.211.141.42:12000, MyRank:0 ERROR 07-27 21:10:50 [core.py:634] EngineCore encountered a fatal error. ERROR 07-27 21:10:50 [core.py:634] Traceback (most recent call last): ERROR 07-27 21:10:50 [core.py:634] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 625, in run_en...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: xy endpoint for the `/v1/chat/completions` endpoint, after sending a few requests, I got the following error: ``` INFO 07-27 21:10:50 [async_llm.py:269] Added request chatcmpl-___prefill_addr_141.211.141.42:10000___deco...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: in schedule ERROR 07-27 21:10:50 [core.py:634] meta = self.connector.build_connector_meta(scheduler_output) ERROR 07-27 21:10:50 [core.py:634] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 07-27 21:10:50 [...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: in _process_engine_step ERROR 07-27 21:10:50 [core.py:634] outputs, model_executed = self.step_fn() ERROR 07-27 21:10:50 [core.py:634] ^^^^^^^^^^^^^^ ERROR 07-27 21:10:50 [core.py:634] File "/usr/local/lib/python3.12/di...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
