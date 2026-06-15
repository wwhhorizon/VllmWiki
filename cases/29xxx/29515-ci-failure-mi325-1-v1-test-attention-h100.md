# vllm-project/vllm#29515: [CI Failure]: mi325_1: V1 Test attention (H100)

| 字段 | 值 |
| --- | --- |
| Issue | [#29515](https://github.com/vllm-project/vllm/issues/29515) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe |
| 子分类 | wrong_output |
| Operator 关键词 | attention;moe |
| 症状 | build_error |
| 根因提示 | shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: V1 Test attention (H100)

### Issue 正文摘录

### Name of failing test `pytest -v -s v1/attention` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests in v1/attention/** **test_causal_backend_correctness** - Tests causal attention backend correctness against SDPA reference - Failures: All variants with tensor_parallel_size=2 and tensor_parallel_size=4 - Configuration: meta-llama/Meta-Llama-3-8B model with various batch specs (small_prefill, mixed_small, medium_decode, medium_prefill, mixed_medium, large_decode, large_prefill, single_decode, single_prefill) - Likely cause: The test simulates head partitioning by overriding model config to use fewer heads (original_num_heads // tensor_parallel_size). When TP>1, the mocked head count configuration may not properly initialize attention backends or the head partitioning logic may have issues with the specific head counts being tested. **test_sliding_window_backend_correctness** - Tests sliding window attention correctness - Failures: All variants with tensor_parallel_size=1, 2, and 4 - Configuration: microsoft/Phi-tiny-MoE-instruct model with batch specs (...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ilure ### Name of failing test `pytest -v -s v1/attention` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ribe the failing test **Failing Tests in v1/attention/** **test_causal_backend_correctness** - Tests causal attention backend correctness against SDPA reference - Failures: All variants with tensor_parallel_size=2 and t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [CI Failure]: mi325_1: V1 Test attention (H100) ci-failure ### Name of failing test `pytest -v -s v1/attention` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: V1 Test attention (H100) ci-failure ### Name of failing test `pytest -v -s v1/attention` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: lures: All variants with tensor_parallel_size=1, 2, and 4, both kv_cache_dtype values (fp8_ds_mla, auto) - Configuration: DeepSeek-V2-Lite-Chat model with various prefill/mixed batch specs - Likely cause: FlashMLA spars...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
