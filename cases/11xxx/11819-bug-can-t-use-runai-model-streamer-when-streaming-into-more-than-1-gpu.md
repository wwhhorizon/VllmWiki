# vllm-project/vllm#11819: [Bug]: Can't Use RunAI Model Streamer When Streaming Into More Than 1 GPU - Pickling Error

| 字段 | 值 |
| --- | --- |
| Issue | [#11819](https://github.com/vllm-project/vllm/issues/11819) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't Use RunAI Model Streamer When Streaming Into More Than 1 GPU - Pickling Error

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is what I encountered when trying to load into 2 GPUs on my EC2 through Vllm It gave me this `Can't pickle : attribute lookup S3 on botocore.client failed` It was setup following this guide: https://docs.vllm.ai/en/stable/serving/runai_model_streamer.html AWS Credential was set through environment variables of `AWS_ACCESS_KEY_ID` `AWS_SECRET_ACCESS_KEY` and `AWS_SESSION_TOKEN` #### Command line used: `vllm serve s3://llama/llama-3.1-8B --load-format runai_streamer --tensor-parallel-size 2 --model-loader-extra-config '{"concurrency":2}'` ``` [ec2-user@ip-172-31-36-112 ~]$ vllm serve s3://llama/llama-3.1-8B --load-format runai_streamer --tensor-parallel-size 2 --model-loader-extra-config '{"concurrency":2}' INFO 01-07 20:42:53 api_server.py:712] vLLM API server version 0.6.6.post1 INFO 01-07 20:42:53 api_server.py:713] args: Namespace(subparser='serve', model_tag='s3://llama/llama-3.1-8B', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=Non...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: "concurrency":2}' INFO 01-07 20:42:53 api_server.py:712] vLLM API server version 0.6.6.post1 INFO 01-07 20:42:53 api_server.py:713] args: Namespace(subparser='serve', model_tag='s3://llama/llama-3.1-8B', config='', host...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Can't Use RunAI Model Streamer When Streaming Into More Than 1 GPU - Pickling Error bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is what I encountered when tryi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='s3://llama/llama-3.1-8B', task='auto...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =None, download_dir=None, load_format='runai_streamer', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_patter...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_paral...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
