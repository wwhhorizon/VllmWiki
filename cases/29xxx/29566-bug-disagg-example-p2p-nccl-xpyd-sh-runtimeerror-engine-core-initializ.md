# vllm-project/vllm#29566: [Bug]: disagg_example_p2p_nccl_xpyd.sh RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}

| 字段 | 值 |
| --- | --- |
| Issue | [#29566](https://github.com/vllm-project/vllm/issues/29566) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: disagg_example_p2p_nccl_xpyd.sh RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using the image vllm/vllm-openai:nightly (sha256:400e8c154231bb4f0f3c36cb53538ff061c64ba641982a6f72bccbc9e93e020a) inside the container. The model I’m using is deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B. I am running the script: ``` bash examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/disagg_example_p2p_nccl_xpyd.sh ```` Here is the log from prefill1: ```text (APIServer pid=952263) INFO 11-26 18:17:59 [api_server.py:2056] vLLM API server version 0.11.2.dev296+gd9d342d21 (APIServer pid=952263) INFO 11-26 18:17:59 [utils.py:253] non-default args: {'model_tag': '/data/models', 'host': '0.0.0.0', 'port': 20003, 'model': '/data/models', 'trust_remote_code': True, 'dtype': 'float16', 'seed': 1024, 'max_model_len': 10000, 'enforce_eager': True, 'max_num_batched_tokens': 10000, 'max_num_seqs': 256, 'kv_transfer_config': KVTransferConfig(kv_connector='P2pNcclConnector', engine_id='fa8a3994-2563-4e17-8528-da635d149f92', kv_buffer_device='cuda', kv_buffer_size=10.0, kv_role='kv_producer', kv_rank=None, kv_parallel_size=1, kv_ip='127.0.0.1', kv_port=21001, kv_connector_extra_config={'proxy_ip': '0.0.0.0', 'proxy_port': '30001...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ver pid=952263) INFO 11-26 18:17:59 [api_server.py:2056] vLLM API server version 0.11.2.dev296+gd9d342d21 (APIServer pid=952263) INFO 11-26 18:17:59 [utils.py:253] non-default args: {'model_tag': '/data/models', 'host':...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: .0', 'port': 20003, 'model': '/data/models', 'trust_remote_code': True, 'dtype': 'float16', 'seed': 1024, 'max_model_len': 10000, 'enforce_eager': True, 'max_num_batched_tokens': 10000, 'max_num_seqs': 256, 'kv_transfer...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: c36cb53538ff061c64ba641982a6f72bccbc9e93e020a) inside the container. The model I’m using is deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B. I am running the script: ``` bash examples/online_serving/disaggregated_serving_p2p_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: initialization failed. See root cause above. Failed core proc(s): {} bug;stale ### Your current environment ### 🐛 Describe the bug I am using the image vllm/vllm-openai:nightly (sha256:400e8c154231bb4f0f3c36cb53538ff061...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
