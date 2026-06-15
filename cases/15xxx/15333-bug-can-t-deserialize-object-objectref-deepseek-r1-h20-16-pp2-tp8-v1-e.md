# vllm-project/vllm#15333: [Bug]: Can't deserialize object: ObjectRef，DeepSeek R1, H20*16, pp2, tp8, v1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#15333](https://github.com/vllm-project/vllm/issues/15333) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't deserialize object: ObjectRef，DeepSeek R1, H20*16, pp2, tp8, v1 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when running DeepSeek-R1-fp8 with H20*16, tp2, pp8, v1 engine, the server hanged with log as follows: + vllm serve /model --tensor-parallel-size 8 --pipeline-parallel-size 2 --trust-remote-code --gpu-memory-utilization 0.92 --max-model-len 98304 --host 0.0.0.0 --port 8102 --served-model-name DeepSeek-R1 --uvicorn-log-level info INFO 03-22 14:13:04 [__init__.py:256] Automatically detected platform cuda. INFO 03-22 14:13:08 [api_server.py:977] vLLM API server version 0.8.1 INFO 03-22 14:13:08 [api_server.py:978] args: Namespace(subparser='serve', model_tag='/model', config='', host='0.0.0.0', port=8102, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_p...

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: current environment ### 🐛 Describe the bug when running DeepSeek-R1-fp8 with H20*16, tp2, pp8, v1 engine, the server hanged with log as follows: + vllm serve /model --tensor-parallel-size 8 --pipeline-parallel-size 2 --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/model', task='auto', tokenizer=None...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: d platform cuda. INFO 03-22 14:13:08 [api_server.py:977] vLLM API server version 0.8.1 INFO 03-22 14:13:08 [api_server.py:978] args: Namespace(subparser='serve', model_tag='/model', config='', host='0.0.0.0', port=8102,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: host='0.0.0.0', port=8102, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: _block_manager=True, num_lookahead_slots=0, seed=None, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.92, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 140 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15333">#15333</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15333">#15333</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15333">#15333</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15333">#15333</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15333">#15333</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
