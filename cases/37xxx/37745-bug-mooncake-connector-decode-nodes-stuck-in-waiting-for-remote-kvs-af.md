# vllm-project/vllm#37745: [Bug]: Mooncake Connector: Decode nodes stuck in WAITING_FOR_REMOTE_KVS after Prefill node restart

| 字段 | 值 |
| --- | --- |
| Issue | [#37745](https://github.com/vllm-project/vllm/issues/37745) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mooncake Connector: Decode nodes stuck in WAITING_FOR_REMOTE_KVS after Prefill node restart

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Bug Description In Prefill-Decode disaggregated Mooncake Connector scenarios, when a Prefill node restarts, new requests from Decode nodes get permanently stuck in `WAITING_FOR_REMOTE_KVS` state and cannot recover automatically. ## Error Logs **First Request (Normal Operation)**: *Prefill Node Log:* ``` (EngineCore pid=58582) INFO 03-21 04:57:39 Creating v1 connector with name: MooncakeConnector and engine_id: 67469cae-1e91-483e-82b6-d2d0a313c3da ... (EngineCore pid=58582) DEBUG 03-21 04:58:18 MooncakeConnector request_finished, req_id=cmpl-9793265a-b5fe-4a21-8490-9a43b682520c-0-b9d7e16a, request_status=FINISHED_LENGTH_CAPPED (EngineCore pid=58582) DEBUG 03-21 04:58:18 Sending kv_caches for request cmpl-9793265a-b5fe-4a21-8490-9a43b682520c-0-a0fb0868 (1 blocks) to 10.233.74.186:15857 ``` *Decode Node Log:* ``` (EngineCore pid=58784) DEBUG 03-21 04:58:18 MooncakeConnector get_num_new_matched_tokens: kv_transfer_params={'remote_engine_id': '67469cae-1e91-483e-82b6-d2d0a313c3da', 'transfer_id': 'xfer-9793265a-b5fe-4a21-8490-9a43b682520c'} ... (EngineCore pid=58784) DEBUG 03-21 04:58:18 Finished recving KV transfer for request cmp...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Mooncake Connector: Decode nodes stuck in WAITING_FOR_REMOTE_KVS after Prefill node restart bug ### Your current environment ### 🐛 Describe the bug ## Bug Description In Prefill-Decode disaggregated Mooncake Conn...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 3. **Restart Prefill node**: ```bash # Restart Prefill service docker restart prefill-service # or kill and restart Prefill process ``` 4. **Send new requests** - Observe request hang ## Actual Behavior - After sending...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ed services**: ```bash # Start Prefill service vllm serve /data/models/Qwen2.5-0.5B-Instruct \ -port 8010 \ --no-enable-prefix-caching \ --model \ --kv-transfer-config \ "{"kv_connector":"MooncakeConnector","kv_role":"k...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: se old engine_id = `67469cae-1e91-483e-82b6-d2d0a313c3da` **Engine ID Mismatch Summary**: - **Before Restart**: Prefill engine_id = `67469cae-1e91-483e-82b6-d2d0a313c3da` Match - **After Restart**: Prefill engine_id = `...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: use old engine_id = `67469cae-1e91-483e-82b6-d2d0a313c3da` **Engine ID Mismatch Summary**: - **Before Restart**: Prefill engine_id = `67469cae-1e91-483e-82b6-d2d0a313c3da` Match - **After Restart**: Prefill engine_id =...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
