# vllm-project/vllm#32972: [CI Failure]:  mi325_8: Kernels Attention Test %N

| 字段 | 值 |
| --- | --- |
| Issue | [#32972](https://github.com/vllm-project/vllm/issues/32972) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;quantization |
| 子分类 | debug |
| Operator 关键词 | attention;cuda;fp8;kernel;triton |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_8: Kernels Attention Test %N

### Issue 正文摘录

### Name of failing test `pytest -v -s kernels/attention` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There were several new regressions all related to the cache test: ```log FAILED kernels/attention/test_cache.py::test_reshape_and_cache_flash[cuda-tensor-HND-fp8-cuda:0-0-dtype0-1024-8-80-8-42] FAILED kernels/attention/test_cache.py::test_reshape_and_cache_flash[cuda-tensor-HND-fp8-cuda:0-0-dtype0-1024-16-80-8-42] FAILED kernels/attention/test_cache.py::test_reshape_and_cache_flash[cuda-tensor-HND-fp8-cuda:0-0-dtype0-10000-32-256-8-42] FAILED kernels/attention/test_cache.py::test_reshape_and_cache_flash[cuda-tensor-HND-fp8-cuda:0-0-dtype1-1024-8-80-8-42] FAILED kernels/attention/test_cache.py::test_reshape_and_cache_flash[cuda-tensor-HND-fp8-cuda:0-0-dtype1-1024-32-256-8-42] FAILED kernels/attention/test_cache.py::test_reshape_and_cache_flash[cuda-tensor-HND-fp8-cuda:0-0-dtype1-10000-8-64-8-42] FAILED kernels/attention/test_cache.py::test_reshape_and_cache_flash[cuda-tensor-HND-fp8-cuda:0-0-dtype1-10000-16-80-8-42] FAILED kernels/attention/test_cache.py::test_resh...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ls/attention/test_cache.py::test_reshape_and_cache_flash[cuda-tensor-HND-fp8-cuda:0-0-dtype0-1024-8-80-8-42] FAILED kernels/attention/test_cache.py::test_reshape_and_cache_flash[cuda-tensor-HND-fp8-cuda:0-0-dtype0-1024-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_8: Kernels Attention Test %N ci-failure ### Name of failing test `pytest -v -s kernels/attention` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external librari
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi325_8: Kernels Attention Test %N ci-failure ### Name of failing test `pytest -v -s kernels/attention` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 42] FAILED kernels/attention/test_cache.py::test_reshape_and_cache_flash[triton-tensor-NHD-fp8-cuda:0-0-dtype0-1024-8-64-8-42] FAILED kernels/attention/test_cache.py::test_reshape_and_cache_flash[triton-tensor-NHD-fp8-c...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: -s kernels/attention` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There were several new regressions...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
