# vllm-project/vllm#16544: [Bug]: vllm V1 Engine doesn't work with offline_profile

| 字段 | 值 |
| --- | --- |
| Issue | [#16544](https://github.com/vllm-project/vllm/issues/16544) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;fp8;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm V1 Engine doesn't work with offline_profile

### Issue 正文摘录

## with vllm 0.8.3 Run the follow command: `export VLLM_USE_V1=1; python examples/offline_inference/profiling.py --model /model/Llama-4-Maverick-17B-128E-Instruct-FP8-2layers/ --enforce-eager --prompt-len 1024 --batch-size 2 --max_model_len 8192 --max_num_batched_tokens 8192 --trust-remote-code --json /home/ubuntu/workspace/profile/Llama4/tensorboard/Maverick_2_1024_baseline/trace.json --tensor-parallel-size 8 run_num_steps --num-steps 6` Gives me emypt output: ``` Run profile with: engine_args = {'model': '/model/Llama-4-Maverick-17B-128E-Instruct-FP8-2layers/', 'served_model_name': None, 'tokenizer': '/model/Llama-4-Maverick-17B-128E-Instruct-FP8-2layers/', 'hf_config_path': None, 'task': 'auto', 'skip_tokenizer_init': False, 'tokenizer_mode': 'auto', 'trust_remote_code': True, 'allowed_local_media_path': None, 'download_dir': None, 'load_format': 'auto', 'config_format': , 'dtype': 'auto', 'kv_cache_dtype': 'auto', 'seed': None, 'max_model_len': 8192, 'distributed_executor_backend': None, 'pipeline_parallel_size': 1, 'tensor_parallel_size': 8, 'data_parallel_size': 1, 'enable_expert_parallel': False, 'max_parallel_loading_workers': None, 'block_size': None, 'enable_prefix_cachi...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: inference/profiling.py --model /model/Llama-4-Maverick-17B-128E-Instruct-FP8-2layers/ --enforce-eager --prompt-len 1024 --batch-size 2 --max_model_len 8192 --max_num_batched_tokens 8192 --trust-remote-code --json /home/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: vllm V1 Engine doesn't work with offline_profile bug;stale ## with vllm 0.8.3 Run the follow command: `export VLLM_USE_V1=1; python examples/offline_inference/profiling.py --model /model/Llama-4-Maverick-17B-128E...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: fig': None, 'qlora_adapter_name_or_path': None, 'show_hidden_metrics_for_version': None, 'otlp_traces_endpoint': None, 'collect_detailed_traces': None, 'disable_async_output_proc': False, 'scheduling_policy': 'fcfs', 's...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: `export VLLM_USE_V1=1; python examples/offline_inference/profiling.py --model /model/Llama-4-Maverick-17B-128E-Instruct-FP8-2layers/ --enforce-eager --prompt-len 1024 --batch-size 2 --max_model_len 8192 --max_num_batche...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ype': 'auto', 'seed': None, 'max_model_len': 8192, 'distributed_executor_backend': None, 'pipeline_parallel_size': 1, 'tensor_parallel_size': 8, 'data_parallel_size': 1, 'enable_expert_parallel': False, 'max_parallel_lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
