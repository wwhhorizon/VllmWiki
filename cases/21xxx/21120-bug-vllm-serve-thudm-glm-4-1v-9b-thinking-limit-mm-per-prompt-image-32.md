# vllm-project/vllm#21120: [Bug]: vllm serve THUDM/GLM-4.1V-9B-Thinking --limit-mm-per-prompt image =32  ： ValueError: `limit_mm_per_prompt` is only supported for multimodal models.

| 字段 | 值 |
| --- | --- |
| Issue | [#21120](https://github.com/vllm-project/vllm/issues/21120) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve THUDM/GLM-4.1V-9B-Thinking --limit-mm-per-prompt image =32  ： ValueError: `limit_mm_per_prompt` is only supported for multimodal models.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve THUDM/GLM-4.1V-9B-Thinking --served-model-name GLM-4.1V-9B-Thinking --tensor-parallel-size 4 --gpu-memory-utilization 0.99 --max-model-len 65536 --max-num-seqs 1 --max-num-batched-tokens 65536 --limit-mm-per-prompt image=64,video=1 --dtype bfloat16 --enforce-eager --swap-space 32 --port 11400 --seed 42 --trust-remote-code /home/anaconda3/envs/xinference/lib/python3.11/site-packages/transformers/utils/hub.py:111: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and will be removed in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( INFO 07-17 20:29:33 [__init__.py:239] Automatically detected platform cuda. INFO 07-17 20:29:34 [api_server.py:1034] vLLM API server version 0.8.3 INFO 07-17 20:29:34 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='THUDM/GLM-4.1V-9B-Thinking', config='', host=None, port=11400, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_forma...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: mpt image =32 ： ValueError: `limit_mm_per_prompt` is only supported for multimodal models. bug ### Your current environment ### 🐛 Describe the bug `CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve THUDM/GLM-4.1V-9B-Thinking --se...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ax-num-batched-tokens 65536 --limit-mm-per-prompt image=64,video=1 --dtype bfloat16 --enforce-eager --swap-space 32 --port 11400 --seed 42 --trust-remote-code /home/anaconda3/envs/xinference/lib/python3.11/site-packages...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: platform cuda. INFO 07-17 20:29:34 [api_server.py:1034] vLLM API server version 0.8.3 INFO 07-17 20:29:34 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='THUDM/GLM-4.1V-9B-Thinking', config='', host=N...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='THUDM/GLM-4.1V-9B-Thinking', task='a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ='bfloat16', kv_cache_dtype='auto', max_model_len=65536, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
