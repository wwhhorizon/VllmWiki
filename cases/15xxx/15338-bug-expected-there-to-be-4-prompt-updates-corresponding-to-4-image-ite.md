# vllm-project/vllm#15338: [Bug]:  Expected there to be 4 prompt updates corresponding to 4 image items, but instead found 3 prompt updates! Either the prompt text has missing/incorrect tokens for multi-modal inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#15338](https://github.com/vllm-project/vllm/issues/15338) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;kernel;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Expected there to be 4 prompt updates corresponding to 4 image items, but instead found 3 prompt updates! Either the prompt text has missing/incorrect tokens for multi-modal inputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1 vllm serve abhishekchohan/gemma-3-27b-it-quantized-W4A16 --limit-mm-per-prompt 'image=4' --max-model-len 16384 --port 11455 --tensor-parallel-size 2 --disable-frontend-multiprocessing when t 'image=3' it`s OK，but when image>3，ERROR occurs: ` /home/anaconda3/envs/xinference14/lib/python3.10/site-packages/transformers/utils/hub.py:106: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and will be removed in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( INFO 03-23 00:51:57 [__init__.py:256] Automatically detected platform cuda. INFO 03-23 00:51:58 [api_server.py:977] vLLM API server version 0.8.1 INFO 03-23 00:51:58 [api_server.py:978] args: Namespace(subparser='serve', model_tag='abhishekchohan/gemma-3-27b-it-quantized-W4A16', config='', host=None, port=11455, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=F...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1 vllm serve abhishekchohan/gemma-3-27b-it-quantized-W4A16 --limit-mm-per-prompt 'image=4' --max-model-len 16384 --port 11455 --tensor-parallel-size 2 --disable-frontend-multipr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: the prompt text has missing/incorrect tokens for multi-modal inputs bug;stale ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1 vllm serve abhishekchohan/gemma-3-27b-it-quantized-W4A16 --limit...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: type='auto', kv_cache_dtype='auto', max_model_len=16384, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: d platform cuda. INFO 03-23 00:51:58 [api_server.py:977] vLLM API server version 0.8.1 INFO 03-23 00:51:58 [api_server.py:978] args: Namespace(subparser='serve', model_tag='abhishekchohan/gemma-3-27b-it-quantized-W4A16'...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: bug CUDA_VISIBLE_DEVICES=0,1 vllm serve abhishekchohan/gemma-3-27b-it-quantized-W4A16 --limit-mm-per-prompt 'image=4' --max-model-len 16384 --port 11455 --tensor-parallel-size 2 --disable-frontend-multiprocessing when t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
