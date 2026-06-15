# vllm-project/vllm#38808: [Bug]: Disaggregate prefill script cannot work due to inconsistent request id between P node and D node.

| 字段 | 值 |
| --- | --- |
| Issue | [#38808](https://github.com/vllm-project/vllm/issues/38808) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;scheduler_memory |
| 子分类 | wrong_output |
| Operator 关键词 | attention;cache;cuda;operator;triton |
| 症状 | build_error;mismatch;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Disaggregate prefill script cannot work due to inconsistent request id between P node and D node.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I try to run prefill disaggregate with **Qwen3-14B** by running command ```shell cd examples/online_serving && bash disaggregated_prefill.sh ``` this procedure hang, and I cannot get the request output from LLM. The logging message like: ```shell INFO:__main__:[prefill] start request_id=___prefill_addr_localhost:14579___decode_addr_localhost:14580_aa38055cf06b4fbcadf37f77befaf21d url=http://localhost:8100/v1/completions (EngineCore pid=71849) INFO 04-02 19:44:09 [p2p_nccl_engine.py:52] set_p2p_nccl_context, original_values: {'NCCL_MAX_NCHANNELS': None, 'NCCL_MIN_NCHANNELS': None, 'NCCL_CUMEM_ENABLE': '0', 'NCCL_BUFFSIZE': None, 'NCCL_PROTO': None, 'NCCL_ALGO': None} (EngineCore pid=71856) INFO 04-02 19:44:09 [p2p_nccl_engine.py:52] set_p2p_nccl_context, original_values: {'NCCL_MAX_NCHANNELS': None, 'NCCL_MIN_NCHANNELS': None, 'NCCL_CUMEM_ENABLE': '0', 'NCCL_BUFFSIZE': None, 'NCCL_PROTO': None, 'NCCL_ALGO': None} (EngineCore pid=71856) INFO 04-02 19:44:09 [p2p_nccl_engine.py:387] 🤝ncclCommInitRank Success, 127.0.0.1:14580👈127.0.0.1:14579, MyRank:1 (EngineCore pid=71849) INFO 04-02 19:44:09 [p2p_nccl_engine.py:226] 🤝ncclCommInitRan...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: uest_id with 'cmpl-' prefix and '-0-\ ', which make decode node cannot recieve correct KV tensor from prefill node. Here is my temporary solution for this mismatch: In class P2pNcclConnector , define a static method to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Disaggregate prefill script cannot work due to inconsistent request id between P node and D node. bug ### Your current environment ### 🐛 Describe the bug I try to run prefill disaggregate with **Qwen3-14B** by ru...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: er these message. Through some debugging，I figure out that there is a mismatch request id between prefill node and decode node. OpenAPI may wrap the original request_id with 'cmpl-' prefix and '-0-\ ', which make decode...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: he hit rate: 0.0%, External prefix cache hit rate: 0.0% ``` and nothing else is printed after these message. Through some debugging，I figure out that there is a mismatch request id between prefill node and decode node....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ns/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%, External prefix cache hit rate: 0.0% (APIServer pid=71627) INFO 04-02 19:44:27 [loggers.py:259] Engine 000: Avg prompt throu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
