# vllm-project/vllm#19964: [CI Failure]: Quantization Test - quantization/test_bitsandbytes.py::test_4bit_bnb_embedding_model

| 字段 | 值 |
| --- | --- |
| Issue | [#19964](https://github.com/vllm-project/vllm/issues/19964) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Quantization Test - quantization/test_bitsandbytes.py::test_4bit_bnb_embedding_model

### Issue 正文摘录

### Name of failing test `quantization/test_bitsandbytes.py::test_4bit_bnb_embedding_model[half-intfloat/e5-mistral-7b-instruct-quantize embedding model inflight]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` pytest -s -v "quantization/test_bitsandbytes.py::test_4bit_bnb_embedding_model[half-intfloat/e5-mistral-7b-instruct-quantize embedding model inflight]" INFO 06-23 04:48:10 [__init__.py:244] Automatically detected platform cuda. /home/mgoin/venvs/vllm/lib/python3.12/site-packages/pytest_asyncio/plugin.py:208: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset. The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session" warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET)) ======...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [CI Failure]: Quantization Test - quantization/test_bitsandbytes.py::test_4bit_bnb_embedding_model ci-failure ### Name of failing test `quantization/test_bitsandbytes.py::test_4bit_bnb_embedding_model[half-intfloat/e5-mi
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: zation Test - quantization/test_bitsandbytes.py::test_4bit_bnb_embedding_model ci-failure ### Name of failing test `quantization/test_bitsandbytes.py::test_4bit_bnb_embedding_model[half-intfloat/e5-mistral-7b-instruct-q...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: ed as DP rank 0, PP rank 0, TP rank 0, EP rank 0 WARNING 06-23 04:48:42 [topk_topp_sampler.py:59] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best pe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [CI Failure]: Quantization Test - quantization/test_bitsandbytes.py::test_4bit_bnb_embedding_model ci-failure ### Name of failing test `quantization/test_bitsandbytes.py::test_4bit_bnb_embedding_model[half-intfloat/e5-m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 0, TP rank 0, EP rank 0 WARNING 06-23 04:48:42 [topk_topp_sampler.py:59] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
