# vllm-project/vllm#28490: [CI Failure][AMD]:  test_prefix_prefill failing on AMD with numeric issues

| 字段 | 值 |
| --- | --- |
| Issue | [#28490](https://github.com/vllm-project/vllm/issues/28490) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cache;cuda;fp8;kernel |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure][AMD]:  test_prefix_prefill failing on AMD with numeric issues

### Issue 正文摘录

### Name of failing test tests/kernels/attention/test_prefix_prefill.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test In https://github.com/vllm-project/vllm/pull/28424 we refactored the test from using xformers to pytorch SDPA since xformers are not supported on ROCm & fixed some incompatibilities on AMD: a. The ROCm paged attention kernel expects 32-bit int tensors, but the test passes 64-bit torch.long tensors. b. ROCm paged attention kernel only supports auto, fp8, and fp8_e4m3 KV cache dtypes. However, the test is still failing on MI300with some numeric issues: https://gist.github.com/zhewenl/3224057e57aad300341c8a0d66bd9878 ``` pytest -s -v 'tests/kernels/attention/test_prefix_prefill.py' ... ================================================================= short test summary info ================================================================== FAILED tests/kernels/attention/test_prefix_prefill.py::test_contexted_kv_attention[chunked_prefill_paged_decode-0-cuda:0-auto-dtype0-128-1-64] - AssertionError: Tensor-likes are not close! FAILED tests/kernels/attenti...

## 现有链接修复摘要

#28905 [CI/Build] Fix test_prefix_prefill for AMD

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure][AMD]: test_prefix_prefill failing on AMD with numeric issues rocm;ci-failure ### Name of failing test tests/kernels/attention/test_prefix_prefill.py ### Basic information - [ ] Flaky test - [ ] Can reprod
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: t torch.long tensors. b. ROCm paged attention kernel only supports auto, fp8, and fp8_e4m3 KV cache dtypes. However, the test is still failing on MI300with some numeric issues: https://gist.github.com/zhewenl/3224057e57...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: I Failure][AMD]: test_prefix_prefill failing on AMD with numeric issues rocm;ci-failure ### Name of failing test tests/kernels/attention/test_prefix_prefill.py ### Basic information - [ ] Flaky test - [ ] Can reproduce...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI Failure][AMD]: test_prefix_prefill failing on AMD with numeric issues rocm;ci-failure ### Name of failing test tests/kernels/attention/test_prefix_prefill.py ### Basic information - [ ] Flaky test - [ ] Can reproduc...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: rs. b. ROCm paged attention kernel only supports auto, fp8, and fp8_e4m3 KV cache dtypes. However, the test is still failing on MI300with some numeric issues: https://gist.github.com/zhewenl/3224057e57aad300341c8a0d66bd...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#28905](https://github.com/vllm-project/vllm/pull/28905) | closes_keyword | 0.95 | [CI/Build] Fix test_prefix_prefill for AMD | Resolves issue #28490. ## Purpose This PR moves the typecast after torch.cumsum, to prevent unwanted promotion to int64. ## Test Plan `pytest -s -v 'tests/kernels/attention/test_ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
