# vllm-project/vllm#18425: [Bug][Failing Test] - Quantization test - quantization/test_cpu_offload.py

| 字段 | 值 |
| --- | --- |
| Issue | [#18425](https://github.com/vllm-project/vllm/issues/18425) |
| 状态 | closed |
| 标签 | bug;ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Failing Test] - Quantization test - quantization/test_cpu_offload.py

### Issue 正文摘录

### Your current environment Failing on main as of commit 9609327fa4 ### 🐛 Describe the bug Failing tests: ``` FAILED quantization/test_cpu_offload.py::test_cpu_offload_gptq - RuntimeError: Server exited unexpectedly. FAILED quantization/test_cpu_offload.py::test_cpu_offload_awq - RuntimeError: Server exited unexpectedly. FAILED quantization/test_cpu_offload.py::test_cpu_offload_compressed_tensors - AssertionError: Results for model='nm-testing/llama7b-one-shot-2_4-w4a16-marlin24-t' are not the same. ref_args=[] ref_envs=None compare_args=['--cpu-offload-gb', '1'] compare_envs=None ref_result={'test': 'single_completion', 'text': ' ... ... . Today I', 'finish_reason': 'length', 'usage': CompletionUsage(completion_tokens=5, prompt_tokens=6, total_tokens=11, completion_tokens_details=None, prompt_tokens_details=None)} compare_result={'test': 'single_completion', 'text': ' ... ... .\n I', 'finish_reason': 'length', 'usage': CompletionUsage(completion_tokens=5, prompt_tokens=6, total_tokens=11, completion_tokens_details=None, prompt_tokens_details=None)} ```

## 现有链接修复摘要

#18543 [Bugfix] Use random hidden states in dummy sampler run

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Failing Test] - Quantization test - quantization/test_cpu_offload.py bug;ci-failure ### Your current environment Failing on main as of commit 9609327fa4 ### 🐛 Describe the bug Failing tests: ``` FAILED quantization/test...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug][Failing Test] - Quantization test - quantization/test_cpu_offload.py bug;ci-failure ### Your current environment Failing on main as of commit 9609327fa4 ### 🐛 Describe the bug Failing tests: ``` FAILED quantizatio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ad.py::test_cpu_offload_compressed_tensors - AssertionError: Results for model='nm-testing/llama7b-one-shot-2_4-w4a16-marlin24-t' are not the same. ref_args=[] ref_envs=None compare_args=['--cpu-offload-gb', '1'] compar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: =None)} ``` performance ci_build;frontend_api;model_support;quantization cuda;quantization crash;slowdown dtype;env_dependency;shape #18543 [Bugfix] Use random hidden states in dummy sampler run Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug][Failing Test] - Quantization test - quantization/test_cpu_offload.py bug;ci-failure ### Your current environment Failing on main as of commit 9609327fa4 ### 🐛 Describe the bug Failing tests: ``` FAILED quantizatio...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18543](https://github.com/vllm-project/vllm/pull/18543) | closes_keyword | 0.95 | [Bugfix] Use random hidden states in dummy sampler run | FIX #18425 FIX #18459 FIX #18462 FIX #18466 FIX #18498 FIX #18525 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
