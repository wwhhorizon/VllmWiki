# vllm-project/vllm#20485: [Bug]: with LMCache,  list index out of range

| 字段 | 值 |
| --- | --- |
| Issue | [#20485](https://github.com/vllm-project/vllm/issues/20485) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: with LMCache,  list index out of range

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug running with vllm ``` vllm serve /mnt/models/Qwen-2.5-0.5b --port 8200 --disable-log-requests --enforce-eager --gpu-memory-utilization 0.25 --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_consumer","kv_connector_extra_config": {"discard_partial_chunks": false, "lmcache_rpc_port": "consumer1"}}' ``` when there's a request to 8200 port, error shows up ``` DEBUG 07-04 11:38:22 [core.py:620] EngineCore loop active. [2025-07-04 11:38:22,145] LMCache INFO: Reqid: cmpl-6b617ce8cf9f4e639322af1d0f78c369-0, Total tokens 6, LMCache hit tokens: 0, need to load: 0 ERROR 07-04 11:38:22 [core.py:588] EngineCore encountered a fatal error. ERROR 07-04 11:38:22 [core.py:588] Traceback (most recent call last): ERROR 07-04 11:38:22 [core.py:588] File "/peter/dev-pod/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 579, in run_engine_core ERROR 07-04 11:38:22 [core.py:588] engine_core.run_busy_loop() ERROR 07-04 11:38:22 [core.py:588] File "/peter/dev-pod/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 606, in run_busy_loop ERROR 07-04 11:38:22 [core.py:588] self._process_engine_step() ERROR 0...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: onment ### 🐛 Describe the bug running with vllm ``` vllm serve /mnt/models/Qwen-2.5-0.5b --port 8200 --disable-log-requests --enforce-eager --gpu-memory-utilization 0.25 --kv-transfer-config '{"kv_connector":"LMCacheCon...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: vllm ``` vllm serve /mnt/models/Qwen-2.5-0.5b --port 8200 --disable-log-requests --enforce-eager --gpu-memory-utilization 0.25 --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_consumer","kv_conne...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: INFO: Reqid: cmpl-6b617ce8cf9f4e639322af1d0f78c369-0, Total tokens 6, LMCache hit tokens: 0, need to load: 0 ERROR 07-04 11:38:22 [core.py:588] EngineCore encountered a fatal error. ERROR 07-04 11:38:22 [core.py:588] Tr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n schedule ERROR 07-04 11:38:22 [core.py:588] meta = self.connector.build_connector_meta(scheduler_output) ERROR 07-04 11:38:22 [core.py:588] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 07-04 11:38:22 [c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
