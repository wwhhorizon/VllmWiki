# vllm-project/vllm#16177: [Bug]: AttributeError: 'Llama4ForConditionalGeneration' object has no attribute 'sampler' with prompt_logprobs

| 字段 | 值 |
| --- | --- |
| Issue | [#16177](https://github.com/vllm-project/vllm/issues/16177) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;moe;quantization;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Llama4ForConditionalGeneration' object has no attribute 'sampler' with prompt_logprobs

### Issue 正文摘录

### Your current environment 2xH200 Runpod `vllm/vllm-openai:v0.8.3` docker image `--model meta-llama/Llama-4-Scout-17B-16E-Instruct --tensor-parallel-size 2 --max-model-len 10000` /chat/completions leads to error logs below ### 🐛 Describe the bug ```json { "messages": [ { "role": "user", "content": [ { "type": "text", "text": "What's in this image?" }, { "type": "image_url", "image_url": { "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg" } } ] }, { "role": "assistant", "content": "The image features a wooden boardwalk meandering through a lush, vibrant green field, flanked by tall grasses and a brilliant blue sky with wispy clouds." } ], "temperature": 0.5, "max_tokens": 1, "add_generation_prompt": false, "continue_final_message": true, "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct", "top_p": 1, "stream": false, "logprobs": true, "prompt_logprobs": 10, "seed": 10 } ``` leads to log: ``` 2025-04-07T08:53:13.833428818Z INFO 04-07 01:53:13 [__init__.py:239] Automatically detected platform cuda. 2025-04-07T08:53:16.018078443Z INFO 04-07 01:53:16 [api_server.py:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ug ### Your current environment 2xH200 Runpod `vllm/vllm-openai:v0.8.3` docker image `--model meta-llama/Llama-4-Scout-17B-16E-Instruct --tensor-parallel-size 2 --max-model-len 10000` /chat/completions leads to error lo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=10000, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', di...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: AttributeError: 'Llama4ForConditionalGeneration' object has no attribute 'sampler' with prompt_logprobs bug ### Your current environment 2xH200 Runpod `vllm/vllm-openai:v0.8.3` docker image `--model meta-llama/Ll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='meta-llama/Llama-4-Scout-17B-16E-Ins...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: ne_parallel_size=1, tensor_parallel_size=2, data_parallel_size=1, enable_expert_parallel=False, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, prefix_cachin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
