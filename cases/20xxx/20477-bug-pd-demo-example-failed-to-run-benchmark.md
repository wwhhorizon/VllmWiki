# vllm-project/vllm#20477: [Bug]: PD demo example failed to run benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#20477](https://github.com/vllm-project/vllm/issues/20477) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling |
| 症状 | crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PD demo example failed to run benchmark

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug run PD example application, then run benchmark, I suffer crashed. everything works fine without PD separation. steps 1. start P ``` CUDA_VISIBLE_DEVICES=0 VLLM_LOGGING_LEVEL=INFO VLLM_USE_V1=1 bin/vua-vllm serve mistralai/Mistral-7B-Instruct-v0.2 --gpu-memory-utilization 0.80 --kv-transfer-config '{"kv_connector":"VUAStorageConnector_V1","kv_role":"kv_producer","kv_connector_extra_config": {"shared_storage_path": "/mnt/nvme1n1/nfsrdma/test10"}}' --port 8001 ``` 2. start D ``` CUDA_VISIBLE_DEVICES=1 VLLM_LOGGING_LEVEL=INFO VLLM_USE_V1=1 bin/vua-vllm serve mistralai/Mistral-7B-Instruct-v0.2 --gpu-memory-utilization 0.80 --kv-transfer-config '{"kv_connector":"VUAStorageConnector_V1","kv_role":"kv_consumer","kv_connector_extra_config": {"shared_storage_path": "/mnt/nvme1n1/nfsrdma/test10"}}' --port 8002 ``` 3. start example proxy server ``` python3 examples/online_serving/disaggregated_serving/disagg_proxy_demo.py --model mistralai/Mistral-7B-Instruct-v0.2 --prefill localhost:8001 --decode localhost:8002 --port 8000 ``` 4. start bench on proxy server it hangs because P process dead ``` VLLM_LOGGING_LEVEL=INFO bin/vua-vllm bench serve...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: PD demo example failed to run benchmark bug;stale ### Your current environment ### 🐛 Describe the bug run PD example application, then run benchmark, I suffer crashed. everything works fine without PD separation....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: PD demo example failed to run benchmark bug;stale ### Your current environment ### 🐛 Describe the bug run PD example application, then run benchmark, I suffer crashed. everything works fine without PD separation....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: /Mistral-7B-Instruct-v0.2 --gpu-memory-utilization 0.80 --kv-transfer-config '{"kv_connector":"VUAStorageConnector_V1","kv_role":"kv_producer","kv_connector_extra_config": {"shared_storage_path": "/mnt/nvme1n1/nfsrdma/t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: shed. everything works fine without PD separation. steps 1. start P ``` CUDA_VISIBLE_DEVICES=0 VLLM_LOGGING_LEVEL=INFO VLLM_USE_V1=1 bin/vua-vllm serve mistralai/Mistral-7B-Instruct-v0.2 --gpu-memory-utilization 0.80 --...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ', dataset_path=None, custom_output_len=256, custom_skip_chat_template=False, sonnet_input_len=550, sonnet_output_len=150, sonnet_prefix_len=200, sharegpt_output_len=None, random_input_len=20000, random_output_len=4000,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
