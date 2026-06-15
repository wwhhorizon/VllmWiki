# vllm-project/vllm#20056: [Bug]: engine die during the inference benchmark workload with kvcache

| 字段 | 值 |
| --- | --- |
| Issue | [#20056](https://github.com/vllm-project/vllm/issues/20056) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: engine die during the inference benchmark workload with kvcache

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ====steps to run serve and benchmark=== ``` VLLM_LOGGING_LEVEL=INFO VLLM_USE_V1=1 bin/vua-vllm serve mistralai/Mistral-7B-Instruct-v0.2 --gpu-memory-utilization 0.80 --kv-transfer-config '{"kv_connector":"VUAStorageConnector_V1","kv_role":"kv_both","kv_connector_extra_config": {"shared_storage_path": "/mnt/nvme1n1/nfsrdma/test5"}}' --enforce_eager VLLM_LOGGING_LEVEL=INFO bin/vua-vllm bench serve --model mistralai/Mistral-7B-Instruct-v0.2 --random-input-len 20000 --random-output-len 4000 --num-prompt 200 ``` ====below is error log shows engine died ``` 11063, 11071, 1493, 1485, 1477, 1469, 1460, 1452, 1444, 1436, 1428, 1420, 1412, 1404, 1396, 1388, 1380, 1372, 1364, 1356, 1348, 1340, 1255, 1263, 1271, 1279, 1287, 1295, 1303, 1311, 1319, 1327, 1335, 9826, 7777, 7763, 7762, 7761, 7760, 7759, 7758, 7757, 7756, 7755, 7754, 7753, 7752, 7751, 7750, 7749, 7748, 7747, 7746, 7745, 7744, 7743, 7742, 7741, 7740, 7739, 7738, 7737, 7736, 7735, 7734, 7733, 7732, 7731, 7730, 7729, 7728, 7727, 7726, 7725, 7724, 7723, 7722, 7721, 7720, 7719, 7718, 7717, 7716, 7715, 7714, 7713, 7712, 7711, 7710, 7709, 7708, 7707, 7706, 7705, 7704, 7703, 7702, 7701,...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: _id='cmpl-1ddaf4e9a4a14260a13ad221eafa4e64-0', resumed_from_preemption=false, new_token_ids=[1119], new_block_ids=[[]], num_computed_tokens=20866), CachedRequestData(req_id='cmpl-95057702575a49cfa76f148afccf139f-0', res...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ug]: engine die during the inference benchmark workload with kvcache bug;stale ### Your current environment ### 🐛 Describe the bug ====steps to run serve and benchmark=== ``` VLLM_LOGGING_LEVEL=INFO VLLM_USE_V1=1 bin/vu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: /Mistral-7B-Instruct-v0.2 --gpu-memory-utilization 0.80 --kv-transfer-config '{"kv_connector":"VUAStorageConnector_V1","kv_role":"kv_both","kv_connector_extra_config": {"shared_storage_path": "/mnt/nvme1n1/nfsrdma/test5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: engine die during the inference benchmark workload with kvcache bug;stale ### Your current environment ### 🐛 Describe the bug ====steps to run serve and benchmark=== ``` VLLM_LOGGING_LEVEL=INFO VLLM_USE_V1=1 bin/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
