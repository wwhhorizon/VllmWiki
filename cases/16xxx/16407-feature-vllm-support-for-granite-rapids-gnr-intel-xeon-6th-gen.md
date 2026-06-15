# vllm-project/vllm#16407: [Feature]: vLLM support for Granite Rapids (GNR - Intel Xeon 6th Gen)

| 字段 | 值 |
| --- | --- |
| Issue | [#16407](https://github.com/vllm-project/vllm/issues/16407) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: vLLM support for Granite Rapids (GNR - Intel Xeon 6th Gen)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Intel Xeon Granite Rapids (GNR) is the 6th Generation Intel Xeon System. I was trying to run vLLM on bare metal which is not working giving an error "No platform detected, vLLM is running on UnspecifiedPlatform". This is a new hardware platform (x86) from Intel. Not sure when the support will be provided. ### Alternatives We can host the model through some custom code and Flask as a temporary solution. This might not get the feature of adaptive batching and scalability required. Added to that multiple Flask instances will have to be locally load balanced using NGINX. ### Additional context vllm serve mistralai/Mistral-7B-Instruct-v0.3 INFO 04-10 10:50:47 [__init__.py:243] No platform detected, vLLM is running on UnspecifiedPlatform INFO 04-10 10:50:48 [api_server.py:981] vLLM API server version 0.8.2 INFO 04-10 10:50:48 [api_server.py:982] args: Namespace(subparser='serve', model_tag='mistralai/Mistral-7B-Instruct-v0.3', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prom...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ure]: vLLM support for Granite Rapids (GNR - Intel Xeon 6th Gen) feature request ### 🚀 The feature, motivation and pitch Intel Xeon Granite Rapids (GNR) is the 6th Generation Intel Xeon System. I was trying to run vLLM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: re when the support will be provided. ### Alternatives We can host the model through some custom code and Flask as a temporary solution. This might not get the feature of adaptive batching and scalability required. Adde...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t working giving an error "No platform detected, vLLM is running on UnspecifiedPlatform". This is a new hardware platform (x86) from Intel. Not sure when the support will be provided. ### Alternatives We can host the mo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: =None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
