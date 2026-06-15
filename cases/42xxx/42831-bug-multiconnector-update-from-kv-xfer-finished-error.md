# vllm-project/vllm#42831: [Bug]: MultiConnector _update_from_kv_xfer_finished error

| 字段 | 值 |
| --- | --- |
| Issue | [#42831](https://github.com/vllm-project/vllm/issues/42831) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MultiConnector _update_from_kv_xfer_finished error

### Issue 正文摘录

### Your current environment vllm v0.20.2 ### 🐛 Describe the bug I encountered the following error during performance stress testing after setting up MultiConnector. ``` decode --kv-transfer-config '{"kv_connector":"MultiConnector","kv_role":"kv_consumer","kv_connector_extra_config":{"connectors":[{"kv_connector":"NixlConnector","kv_role":"kv_consumer"},{"kv_connector":"MooncakeStoreConnector","kv_role":"kv_consumer"}]}}' prefill --kv-transfer-config '{"kv_connector":"MultiConnector","kv_role":"kv_producer","kv_connector_extra_config":{"connectors":[{"kv_connector":"NixlConnector","kv_role":"kv_producer"},{"kv_connector":"MooncakeStoreConnector","kv_role":"kv_producer"}]}}' ``` ``` EngineCore encountered a fatal error. Traceback (most recent call last): File "/vllm-workspace/vllm/v1/engine/core.py", line 1129, in run_engine_core engine_core.run_busy_loop() File "/vllm-workspace/vllm/v1/engine/core.py", line 1170, in run_busy_loop self._process_engine_step() File "/vllm-workspace/vllm/v1/engine/core.py", line 1209, in _process_engine_step outputs, model_executed = self.step_fn() File "/vllm-workspace/vllm/v1/engine/core.py", line 427, in step engine_core_outputs = self.scheduler.up...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: during performance stress testing after setting up MultiConnector. ``` decode --kv-transfer-config '{"kv_connector":"MultiConnector","kv_role":"kv_consumer","kv_connector_extra_config":{"connectors":[{"kv_connector":"Ni...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tress testing after setting up MultiConnector. ``` decode --kv-transfer-config '{"kv_connector":"MultiConnector","kv_role":"kv_consumer","kv_connector_extra_config":{"connectors":[{"kv_connector":"NixlConnector","kv_rol...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ibe the bug I encountered the following error during performance stress testing after setting up MultiConnector. ``` decode --kv-transfer-config '{"kv_connector":"MultiConnector","kv_role":"kv_consumer","kv_connector_ex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
