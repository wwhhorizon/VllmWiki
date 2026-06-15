# vllm-project/vllm#19281: [CI Failure]: buildkite/ci/v1-test

| 字段 | 值 |
| --- | --- |
| Issue | [#19281](https://github.com/vllm-project/vllm/issues/19281) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: buildkite/ci/v1-test

### Issue 正文摘录

### Name of failing test tests/v1/kv_connector/unit/test_multi_connector.py::test_multi_shared_storage_connector_consistency ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` python -m pytest -v -s tests/v1/kv_connector/unit/test_multi_connector.py::test_multi_shared_storage_connector_consistency INFO 06-06 13:08:08 [__init__.py:244] Automatically detected platform cuda. /home/ubuntu/vllm/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:208: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset. The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session" warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET)) =========================================================================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [CI Failure]: buildkite/ci/v1-test ci-failure ### Name of failing test tests/v1/kv_connector/unit/test_multi_connector.py::test_multi_shared_storage_connector_consistency ### Basic information - [ ] Flaky test - [x] Ca
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: . Defaulting to 'generate'. INFO 06-06 13:08:20 [config.py:2182] Chunked prefill is enabled with max_num_batched_tokens=8192. WARNING 06-06 13:08:20 [cuda.py:91] To see benefits of async output processing, enable CUDA g...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disabl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nnector.py::test_multi_shared_storage_connector_consistency ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
