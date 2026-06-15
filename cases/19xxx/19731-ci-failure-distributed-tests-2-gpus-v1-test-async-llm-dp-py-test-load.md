# vllm-project/vllm#19731: [CI Failure]: Distributed Tests (2 GPUs) - v1/test_async_llm_dp.py::test_load

| 字段 | 值 |
| --- | --- |
| Issue | [#19731](https://github.com/vllm-project/vllm/issues/19731) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Distributed Tests (2 GPUs) - v1/test_async_llm_dp.py::test_load

### Issue 正文摘录

### Name of failing test TP_SIZE=1 DP_SIZE=2 pytest -s -v "v1/test_async_llm_dp.py::test_load[ray-RequestOutputKind.DELTA]" ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The error ends up looking like a triton bug with `AttributeError: module 'triton.language' has no attribute 'bfloat16'` reported, however very early in the logs you can see the following: ``` INFO 06-17 07:32:31 [utils.py:384] Creating placement groups for data parallel (pid=3893316) INFO 06-17 07:32:33 [importing.py:27] Triton is installed but 0 active driver(s) found (expected 1). Disabling Triton to prevent runtime errors. (pid=3893316) INFO 06-17 07:32:33 [importing.py:47] Triton not installed or not compatible; certain GPU-related functions will not be available. (pid=3893316) WARNING 06-17 07:32:33 [importing.py:59] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation. ``` This is strange because triton is fully installed in my environment as usual. Here is the full command and traceback: ``` TP_SIZE=1 DP_SIZE=2 pytest -s -v "v1/test...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [CI Failure]: Distributed Tests (2 GPUs) - v1/test_async_llm_dp.py::test_load ci-failure ### Name of failing test TP_SIZE=1 DP_SIZE=2 pytest -s -v "v1/test_async_llm_dp.py::test_load[ray-RequestOutputKind.DELTA]" ### Ba
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: ers`) ### 🧪 Describe the failing test The error ends up looking like a triton bug with `AttributeError: module 'triton.language' has no attribute 'bfloat16'` reported, however very early in the logs you can see the foll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ton bug with `AttributeError: module 'triton.language' has no attribute 'bfloat16'` reported, however very early in the logs you can see the following: ``` INFO 06-17 07:32:31 [utils.py:384] Creating placement groups fo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: engine (v0.9.1.dev287+g89b1388d8) with config: model='ibm-research/PowerMoE-3b', speculative_config=None, tokenizer='ibm-research/PowerMoE-3b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: TP_SIZE=1 DP_SIZE=2 pytest -s -v "v1/test_async_llm_dp.py::test_load[ray-RequestOutputKind.DELTA]" ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `tran...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
