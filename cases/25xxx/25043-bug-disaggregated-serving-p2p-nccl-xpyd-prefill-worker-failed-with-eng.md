# vllm-project/vllm#25043: [Bug]: disaggregated_serving_p2p_nccl_xpyd prefill worker failed with "EngineCore failed to start".

| 字段 | 值 |
| --- | --- |
| Issue | [#25043](https://github.com/vllm-project/vllm/issues/25043) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: disaggregated_serving_p2p_nccl_xpyd prefill worker failed with "EngineCore failed to start".

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The example disaggregated_serving_p2p_nccl_xpyd.sh script runs with 1P3D configuration as default on a single HGX B200 node, with P2P NCCL Connector. The prefill worker fails to start engine core with the stack below. It appears bind_connector_metadata is not called for the prefill worker. OTOH, the symptom is not observed on 3 decoder worker. > (EngineCore_DP0 pid=35109)ESC[0;0m ERROR 09-17 05:40:55 [v1/engine/core.py:712] EngineCore failed to start. > (EngineCore_DP0 pid=35109)ESC[0;0m ERROR 09-17 05:40:55 [v1/engine/core.py:712] Traceback (most recent call last): > (EngineCore_DP0 pid=35109)ESC[0;0m ERROR 09-17 05:40:55 [v1/engine/core.py:712] File "/home/ubuntu/vllm/vllm/v1/engine/core.py", line 703, in run_engine_core > (EngineCore_DP0 pid=35109)ESC[0;0m ERROR 09-17 05:40:55 [v1/engine/core.py:712] engine_core = EngineCoreProc(*args, **kwargs) > (EngineCore_DP0 pid=35109)ESC[0;0m ERROR 09-17 05:40:55 [v1/engine/core.py:712] File "/home/ubuntu/vllm/vllm/v1/engine/core.py", line 502, in __init__ > (EngineCore_DP0 pid=35109)ESC[0;0m ERROR 09-17 05:40:55 [v1/engine/core.py:712] super().__init__(vllm_config, executor_class, log_s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: The example disaggregated_serving_p2p_nccl_xpyd.sh script runs with 1P3D configuration as default on a single HGX B200 node, with P2P NCCL Connector. The prefill worker fails to start engine core with the stack below. I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: disaggregated_serving_p2p_nccl_xpyd prefill worker failed with "EngineCore failed to start". bug;stale ### Your current environment ### 🐛 Describe the bug The example disaggregated_serving_p2p_nccl_xpyd.sh script...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l_xpyd.sh script runs with 1P3D configuration as default on a single HGX B200 node, with P2P NCCL Connector. The prefill worker fails to start engine core with the stack below. It appears bind_connector_metadata is not...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 0m ERROR 09-17 05:40:55 [v1/engine/core.py:712] self.collective_rpc("compile_or_warm_up_model") > (EngineCore_DP0 pid=35109)ESC[0;0m ERROR 09-17 05:40:55 [v1/engine/core.py:712] File "/home/ubuntu/vllm/vllm/executor/uni...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ils to start engine core with the stack below. It appears bind_connector_metadata is not called for the prefill worker. OTOH, the symptom is not observed on 3 decoder worker. > (EngineCore_DP0 pid=35109)ESC[0;0m ERROR 0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
