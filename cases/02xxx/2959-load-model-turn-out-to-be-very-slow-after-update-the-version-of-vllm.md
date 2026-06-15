# vllm-project/vllm#2959: Load model turn out to be very slow after update the version of vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#2959](https://github.com/vllm-project/vllm/issues/2959) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Load model turn out to be very slow after update the version of vllm

### Issue 正文摘录

I am using vllm and mixtral 8x7b, the version of vllm is 0.2.6, it works well. I tried to update the version to latest 0.3.1. however, while it proceeds to load model weight, it becomes very slow. it takes almost 40 minutes vs. 5 minutes for the old version. I don't know how it happens since I do not change any other environment and parameters. I have checked the difference of loading model in mixtral.py and doesn't find any clues. I downloaded the model, and my parameters are: > Namespace(host='0.0.0.0', port=28711, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name='mixtral', chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, root_path=None, middleware=[], model='/data0/Mixtral-8x7B-Instruct-v0.1', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_b...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_load...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Load model turn out to be very slow after update the version of vllm I am using vllm and mixtral 8x7b, the version of vllm is 0.2.6, it works well. I tried to update the version to latest 0.3.1. however, while it procee...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Load model turn out to be very slow after update the version of vllm I am using vllm and mixtral 8x7b, the version of vllm is 0.2.6, it works well. I tried to update the version to latest 0.3.1. however, while it procee...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: meters are: > Namespace(host='0.0.0.0', port=28711, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name='mixtral', chat_template=None, response_r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ora_extra_vocab_size=256, lora_dtype='auto', max_cpu_loras=None, device='cuda', engine_use_ray=False, disable_log_requests=False, max_log_len=None) the log hanging for about 40 minutes at: > Initializing an LLM engine w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
