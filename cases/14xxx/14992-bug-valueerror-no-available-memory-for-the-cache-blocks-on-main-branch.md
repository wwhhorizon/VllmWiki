# vllm-project/vllm#14992: [Bug]: ValueError: No available memory for the cache blocks on main branch after commit 46f98893

| 字段 | 值 |
| --- | --- |
| Issue | [#14992](https://github.com/vllm-project/vllm/issues/14992) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cache;cuda;fp8;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: ValueError: No available memory for the cache blocks on main branch after commit 46f98893

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug how to product: run vllm serve, ``` vllm serve /root/HuggingFaceCache/models--google--gemma-3-27b-it --trust-remote-code --served-model-name gpt-4o --gpu-memory-utilization 0.99 --tensor-parallel-size 4 --port 8000 --api-key sk-123456 --max-model-len 32768 --enable-chunked-prefill --limit-mm-per-prompt image=3 ``` error log: ``` INFO 03-18 10:21:18 [__init__.py:256] Automatically detected platform cuda. INFO 03-18 10:21:20 [api_server.py:966] vLLM API server version 0.7.4.dev474+g3556a414 INFO 03-18 10:21:20 [api_server.py:967] args: Namespace(subparser='serve', model_tag='/root/HuggingFaceCache/models--google--gemma-3-27b-it', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key='sk-123456', lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_r...

## 现有链接修复摘要

#12721 Update to torch==2.6.0 | #14464 [Bugfix] EAGLE output norm bug | #14812 [VLM] Clean up Phi-4-MM ViT implementation | #14842 [Attention] Get rid of mla cache alignment | #14846 [V1][TPU] Apply the ragged paged attention kernel fix and remove the padding. | #14910 [BugFix] Fix MLA + V1 + TP==1 causing reinitialization of cuda context | #14921 [V1] Default MLA to V1 | #14950 [Bugfix] Fix bnb quantization for models with both HF-format and Mistral-format weights | #14974 [V1] TPU - Fix CI/CD runner for V1 and remove V0 tests

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: Describe the bug how to product: run vllm serve, ``` vllm serve /root/HuggingFaceCache/models--google--gemma-3-27b-it --trust-remote-code --served-model-name gpt-4o --gpu-memory-utilization 0.99 --tensor-parallel-size 4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: 4 --port 8000 --api-key sk-123456 --max-model-len 32768 --enable-chunked-prefill --limit-mm-per-prompt image=3 ``` error log: ``` INFO 03-18 10:21:18 [__init__.py:256] Automatically detected platform cuda. INFO 03-18 10...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: d platform cuda. INFO 03-18 10:21:20 [api_server.py:966] vLLM API server version 0.7.4.dev474+g3556a414 INFO 03-18 10:21:20 [api_server.py:967] args: Namespace(subparser='serve', model_tag='/root/HuggingFaceCache/models...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', di...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: type='auto', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#12721](https://github.com/vllm-project/vllm/pull/12721) | mentioned | 0.45 | Update to torch==2.6.0 | 677783 [ci] add tpu v1 test (#14834) 14f301b5 update to torch==2.6.0 (#12721) 46f98893 [v1] fix model parameterization for structured output tests (#14833) ``` ### before submitti… |
| [#14464](https://github.com/vllm-project/vllm/pull/14464) | mentioned | 0.45 | [Bugfix] EAGLE output norm bug | put cache by memory (#14805) 9ed6ee92 [bugfix] eagle output norm bug (#14464) ee3778d5 [build/ci] upgrade jinja2 to get 3 moderate cve fixes (#14839) aaacf173 [doc] v1 user guide… |
| [#14812](https://github.com/vllm-project/vllm/pull/14812) | mentioned | 0.45 | [VLM] Clean up Phi-4-MM ViT implementation | kenizer (#14873) def232e1 [vlm] clean up phi-4-mm vit implementation (#14812) 3453b964 [misc][doc] minor benchmark readme update (#14874) 61c6a5a7 [vlm] merged multi-modal process… |
| [#14842](https://github.com/vllm-project/vllm/pull/14842) | mentioned | 0.45 | [Attention] Get rid of mla cache alignment | as test (#14849) 5952d8ab [attention] get rid of mla cache alignment (#14842) a2ae4965 [cpu] support fp8 kv cache (#14741) 877e3522 [docs] add new east coast vllm meetup slides to… |
| [#14846](https://github.com/vllm-project/vllm/pull/14846) | mentioned | 0.45 | [V1][TPU] Apply the ragged paged attention kernel fix and remove the padding. | apply the ragged paged attention kernel fix and remove the padding. (#14846) 69698f25 fix minor miscalled method (#14327) cd0cd851 [misc] more amd unused var clean up (#14926) 0a7… |
| [#14910](https://github.com/vllm-project/vllm/pull/14910) | mentioned | 0.45 | [BugFix] Fix MLA + V1 + TP==1 causing reinitialization of cuda context | ugfix] fix mla + v1 + tp==1 causing reinitialization of cuda context (#14910) 7f6c5ee0 [v1][minor] add __repr__ to constantlist (#14907) faa02757 [v1] optimize the overhead of rew… |
| [#14921](https://github.com/vllm-project/vllm/pull/14921) | mentioned | 0.45 | [V1] Default MLA to V1 | line too long in pixtral.py (#14960) 89fca671 [v1] default mla to v1 (#14921) d20b0c13 add patch merger (#14957) 166a168b [doc] fix misleading log during multi-modal profiling (#1… |
| [#14950](https://github.com/vllm-project/vllm/pull/14950) | mentioned | 0.45 | [Bugfix] Fix bnb quantization for models with both HF-format and Mistral-format weights | antization for models with both hf-format and mistral-format weights (#14950) 18551e82 [v1] tpu - fix ci/cd runner (#14974) e41e1602 [v1] guard against main thread usage (#14972)… |
| [#14974](https://github.com/vllm-project/vllm/pull/14974) | mentioned | 0.45 | [V1] TPU - Fix CI/CD runner for V1 and remove V0 tests | mistral-format weights (#14950) 18551e82 [v1] tpu - fix ci/cd runner (#14974) e41e1602 [v1] guard against main thread usage (#14972) b89fb2a4 [ci/build] use `automodelforimagetext… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
