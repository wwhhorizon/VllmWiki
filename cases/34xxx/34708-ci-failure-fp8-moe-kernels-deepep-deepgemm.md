# vllm-project/vllm#34708: [CI Failure]: Fp8 MoE Kernels (DeepEP + DeepGEMM)

| 字段 | 值 |
| --- | --- |
| Issue | [#34708](https://github.com/vllm-project/vllm/issues/34708) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Fp8 MoE Kernels (DeepEP + DeepGEMM)

### Issue 正文摘录

### Name of failing test `kernels/moe/test_deepep_moe.py::test_low_latency_deep_ep_moe` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Maxdiff ``` E torch.multiprocessing.spawn.ProcessRaisedException: -- E E -- Process 1 terminated with the following error: E Traceback (most recent call last): E File "/usr/local/lib/python3.12/dist-packages/torch/multiprocessing/spawn.py", line 87, in _wrap E fn(i, *args) E File "/vllm-workspace/tests/kernels/moe/parallel_utils.py", line 68, in _worker_parallel_launch E worker( E File "/vllm-workspace/tests/kernels/moe/test_deepep_moe.py", line 419, in _deep_ep_moe E torch.testing.assert_close( E File "/usr/local/lib/python3.12/dist-packages/torch/testing/_comparison.py", line 1600, in assert_close E raise error_metas[0].to_error(msg) E AssertionError: Tensor-likes are not close! E E Mismatched elements: 2 / 568320 (0.0%) E Greatest absolute difference: 0.09375 at index (206, 2432) (up to 0.06 allowed) E Greatest relative difference: 0.94140625 at index (206, 947) (up to 0.06 allowed) ``` ### 📝 History of failing test appears to have...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: _latency_deep_ep_moe` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Maxdiff ``` E torch.multiprocessin...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [CI Failure]: Fp8 MoE Kernels (DeepEP + DeepGEMM) ci-failure ### Name of failing test `kernels/moe/test_deepep_moe.py::test_low_latency_deep_ep_moe` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ure]: Fp8 MoE Kernels (DeepEP + DeepGEMM) ci-failure ### Name of failing test `kernels/moe/test_deepep_moe.py::test_low_latency_deep_ep_moe` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Cause...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: Fp8 MoE Kernels (DeepEP + DeepGEMM) ci-failure ### Name of failing test `kernels/moe/test_deepep_moe.py::test_low_latency_deep_ep_moe` ### Basic information - [x] Flaky test - [ ] Can reproduce locally -
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [CI Failure]: Fp8 MoE Kernels (DeepEP + DeepGEMM) ci-failure ### Name of failing test `kernels/moe/test_deepep_moe.py::test_low_latency_deep_ep_moe` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
