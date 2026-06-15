# vllm-project/vllm#2719: RuntimeError: unable to open shared memory object </torch_1_2004494542_0> in read-write mode: Permission denied (13)

| 字段 | 值 |
| --- | --- |
| Issue | [#2719](https://github.com/vllm-project/vllm/issues/2719) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError: unable to open shared memory object </torch_1_2004494542_0> in read-write mode: Permission denied (13)

### Issue 正文摘录

With 0.3.0 release, not on 0.2.7. cuda 12.1 using V100. ``` ➜ ~ k logs -f h2ogpt-vllm-inference-764dfd798c-rlmjd -n h2ogpt INFO 02-02 01:01:59 api_server.py:209] args: Namespace(host='0.0.0.0', port=5000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, root_path=None, middleware=[], model='h2oai/h2ogpt-4096-llama2-7b-chat', tokenizer='hf-internal-testing/llama-tokenizer', revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, download_dir='/workspace/.cache/huggingface/hub', load_format='auto', dtype='auto', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block_size=16, seed=1234, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=8192, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quantization=None, enforce_eager=False, max_context_len_to_capture=8192, disable_custom_all_reduce=False, enable_lora=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: '*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, root_path=None, middleware=[], model='h2oai/h...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e, download_dir='/workspace/.cache/huggingface/hub', load_format='auto', dtype='auto', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_load...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r.py:209] args: Namespace(host='0.0.0.0', port=5000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, chat_template=None, response_role=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rontend_api;model_support;quantization cuda;quantization crash dtype;env_dependency With 0.3.0 release, not on 0.2.7. cuda 12.1 using V100.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ad-write mode: Permission denied (13) With 0.3.0 release, not on 0.2.7. cuda 12.1 using V100. ``` ➜ ~ k logs -f h2ogpt-vllm-inference-764dfd798c-rlmjd -n h2ogpt INFO 02-02 01:01:59 api_server.py:209] args: Namespace(hos...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
