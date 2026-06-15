# vllm-project/vllm#8051: [Bug]: flakey test found in #7874

| 字段 | 值 |
| --- | --- |
| Issue | [#8051](https://github.com/vllm-project/vllm/issues/8051) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: flakey test found in #7874

### Issue 正文摘录

#7874 adjusted chunked prefill the scheduling order fp8_e4m3 model FAILED FAILED basic_correctness/test_chunked_prefill.py::test_models_with_fp8_kv_cache[True-1-False-4-4-fp8_e4m3-nm-testing/Qwen2-1.5B-Instruct-FP8-K-V] - AssertionError: Test7: FAILED basic_correctness/test_chunked_prefill.py::test_models_with_fp8_kv_cache[True-1-True-4-4-fp8_e4m3-nm-testing/Qwen2-1.5B-Instruct-FP8-K-V] - AssertionError: Test7: but bf16 model PASS tests/basic_correctness/test_chunked_prefill.py::test_models_with_fp8_kv_cache[True-1-False-4-4-auto-Qwen/Qwen2-1.5B-Instruct] tests/basic_correctness/test_chunked_prefill.py::test_models_with_fp8_kv_cache[True-1-True-4-4-auto-Qwen/Qwen2-1.5B-Instruct] Test 7 is stuck on the resolution of fp8_e4m3， ### 🐛 Describe the bug as @jon-chuang said: The test using top k log probs may have been bound to be flakey. Perhaps testing style like this is more reliable especially given hardware differences or drift across kernels. https://github.com/vllm-project/vllm/pull/8013 (However note that this is just top 1 log probs I.e. greedy decode so not sure if even this testing strategy will be reliable) ### Before submitting a new issue... - [X] Make sure you already sear...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: found in #7874 bug #7874 adjusted chunked prefill the scheduling order fp8_e4m3 model FAILED FAILED basic_correctness/test_chunked_prefill.py::test_models_with_fp8_kv_cache[True-1-False-4-4-fp8_e4m3-nm-testing/Qwen2-1.5...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: #7874 bug #7874 adjusted chunked prefill the scheduling order fp8_e4m3 model FAILED FAILED basic_correctness/test_chunked_prefill.py::test_models_with_fp8_kv_cache[True-1-False-4-4-fp8_e4m3-nm-testing/Qwen2-1.5B-Instruc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: flakey test found in #7874 bug #7874 adjusted chunked prefill the scheduling order fp8_e4m3 model FAILED FAILED basic_correctness/test_chunked_prefill.py::test_models_with_fp8_kv_cache[True-1-False-4-4-fp8_e4m3-n...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tyle like this is more reliable especially given hardware differences or drift across kernels. https://github.com/vllm-project/vllm/pull/8013 (However note that this is just top 1 log probs I.e. greedy decode so not sur...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: bound to be flakey. Perhaps testing style like this is more reliable especially given hardware differences or drift across kernels. https://github.com/vllm-project/vllm/pull/8013 (However note that this is just top 1 lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
