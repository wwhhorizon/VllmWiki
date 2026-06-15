# vllm-project/vllm#15385: [Bug]: gcs_rpc_client.h:151: Failed to connect to GCS at address 192.168.2.40:6379 within 5 seconds.

| 字段 | 值 |
| --- | --- |
| Issue | [#15385](https://github.com/vllm-project/vllm/issues/15385) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gcs_rpc_client.h:151: Failed to connect to GCS at address 192.168.2.40:6379 within 5 seconds.

### Issue 正文摘录

### Your current environment ubuntu 23.10 cuda 12.0 vllm==0.7.3 transformers==4.49.0 ### 🐛 Describe the bug 我使用vllm部署Qwen2.5-VL-7B-Instruct，使用 `vllm serve /home/wzx/cv/vllm/demo/Qwen2.5-VL-7B-Instruct --served-model-name qwen2.5-vl-7b --gpu-memory-utilization 0.6 --tensor-parallel-size 4 --port 48000`命令启动服务，打印信息如下： `vllm serve /home/wzx/cv/vllm/demo/Qwen2.5-VL-7B-Instruct --served-model-name qwen2.5-vl-7b --gpu-memory-utilization 0.6 --tensor-parallel-size 4 --port 48000 INFO 03-24 17:14:41 [__init__.py:256] Automatically detected platform cuda. INFO 03-24 17:14:42 [api_server.py:977] vLLM API server version 0.8.0 INFO 03-24 17:14:42 [api_server.py:978] args: Namespace(subparser='serve', model_tag='/home/wzx/cv/vllm/demo/Qwen2.5-VL-7B-Instruct', config='', host=None, port=48000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_tok...

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: to connect to GCS at address 192.168.2.40:6379 within 5 seconds. bug;ray;stale ### Your current environment ubuntu 23.10 cuda 12.0 vllm==0.7.3 transformers==4.49.0 ### 🐛 Describe the bug 我使用vllm部署Qwen2.5-VL-7B-Instruct，...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 12.0 vllm==0.7.3 transformers==4.49.0 ### 🐛 Describe the bug 我使用vllm部署Qwen2.5-VL-7B-Instruct，使用 `vllm serve /home/wzx/cv/vllm/demo/Qwen2.5-VL-7B-Instruct --served-model-name qwen2.5-vl-7b --gpu-memory-utilization 0.6 --...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: d platform cuda. INFO 03-24 17:14:42 [api_server.py:977] vLLM API server version 0.8.0 INFO 03-24 17:14:42 [api_server.py:978] args: Namespace(subparser='serve', model_tag='/home/wzx/cv/vllm/demo/Qwen2.5-VL-7B-Instruct'...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: '', host=None, port=48000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 140 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15385">#15385</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>🔧 Upd… |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15385">#15385</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>🔧 Upd… |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15385">#15385</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>🔧 Upd… |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15385">#15385</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>🔧 Upd… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15385">#15385</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>🔧 Upd… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
