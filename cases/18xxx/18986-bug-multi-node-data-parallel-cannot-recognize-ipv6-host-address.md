# vllm-project/vllm#18986: [Bug]: Multi-node data parallel cannot recognize IPv6 host address

| 字段 | 值 |
| --- | --- |
| Issue | [#18986](https://github.com/vllm-project/vllm/issues/18986) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi-node data parallel cannot recognize IPv6 host address

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm try deploy Qwen2.5-32B-Instruct across 2 A100-80G nodes by using the following command: ``` export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 export VLLM_USE_V1="1" #export VLLM_HOST_IP=$(hostname -I | awk '{print $1}') #export HOST_IP=$(hostname -I | awk '{print $1}') IFS=',' read -ra HOSTS &2 exit 1 fi dp_address="tcp://[${ip}]:${port}" # vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver INFO 05-31 17:36:15 [__init__.py:36] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load. INFO 05-31 17:36:18 [api_server.py:1289] vLLM API server version 0.9.0.1 INFO 05-31 17:36:18 [cli_args.py:300] non-default args: {'host': '::', 'rope_scaling': {'rope_type': 'yarn', 'factor': 4.0, 'original_max_position_embeddings': 32768}, 'max_model_len': 131072, 'served_model_name': ['qwen2.5-32b'], 'tensor_parallel_size': 8, 'data_parallel_size': 2, 'data_parallel_size_local': 1, 'data_parallel_address': '2605:340:cd51:a00:2a6:1aa4:9970:acec', 'data_parallel_rpc_port': 9662, 'max_num_seqs': 256} INFO 05-31 17:36:18 [config.py:520] Overriding HF config with {'rope_scaling': {'rope_type': 'yar...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: lugins to load. INFO 05-31 17:36:18 [api_server.py:1289] vLLM API server version 0.9.0.1 INFO 05-31 17:36:18 [cli_args.py:300] non-default args: {'host': '::', 'rope_scaling': {'rope_type': 'yarn', 'factor': 4.0, 'origi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ### Your current environment ### 🐛 Describe the bug I'm try deploy Qwen2.5-32B-Instruct across 2 A100-80G nodes by using the following command: ``` export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 export VLLM_USE_V1="1" #export V...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: p for distributed inference INFO 05-31 17:36:39 [config.py:2118] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 05-31 17:36:39 [cuda.py:156] Data Parallel: Forcing enforce eager to be True since DP is...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, disable_custom_al...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ### 🐛 Describe the bug I'm try deploy Qwen2.5-32B-Instruct across 2 A100-80G nodes by using the following command: ``` export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 export VLLM_USE_V1="1" #export VLLM_HOST_IP=$(hostname -I | a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
