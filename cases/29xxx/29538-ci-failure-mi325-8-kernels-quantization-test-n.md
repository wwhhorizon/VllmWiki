# vllm-project/vllm#29538: [CI Failure]: mi325_8: Kernels Quantization Test %N

| 字段 | 值 |
| --- | --- |
| Issue | [#29538](https://github.com/vllm-project/vllm/issues/29538) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_8: Kernels Quantization Test %N

### Issue 正文摘录

### Name of failing test `pytest -v -s kernels/quantization --shard-id=$BUILDKITE_PARALLEL_JOB --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests Summary:** **test_cutlass_w4a8 in test_cutlass_w4a8.py** Tests: CUTLASS W4A8 (4-bit weights, 8-bit activations) mixed precision GEMM with various matrix sizes and schedules Failure: Multiple test cases with different MNK dimensions failing (256x32_1x1x1-types0-1x4096x4096, 128x64_1x1x1-types0 variants, 256x64_1x1x1-types0 variants, 128x256 variants) Configuration: dtype=fp8/int4, various matrix dimensions, group_size=128, channel/token scales Likely cause: CUTLASS W4A8 kernel implementation missing or incompatible on ROCm, or kernel dispatch logic not routing correctly for ROCm backend on compute capability 9.0+ hardware **test_w4a8_cuda_graph in test_cutlass_w4a8.py** Tests: CUDA graph compatibility with W4A8 kernel in torch.nn.Module Failure: AttributeError during graph capture Configuration: m=512, n=4096, k=4096, quant_type=int4, group_size=128 Likely cause: CUDA g...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [CI Failure]: mi325_8: Kernels Quantization Test %N ci-failure ### Name of failing test `pytest -v -s kernels/quantization --shard-id=$BUILDKITE_PARALLEL_JOB --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT` ### Basic informa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: s`) ### 🧪 Describe the failing test **Failing Tests Summary:** **test_cutlass_w4a8 in test_cutlass_w4a8.py** Tests: CUTLASS W4A8 (4-bit weights, 8-bit activations) mixed precision GEMM with various matrix sizes and sche...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: E_PARALLEL_JOB_COUNT` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests Summary:** **test_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: mi325_8: Kernels Quantization Test %N ci-failure ### Name of failing test `pytest -v -s kernels/quantization --shard-id=$BUILDKITE_PARALLEL_JOB --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT` ### Basic informa
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ely cause: CUTLASS W4A8 kernel implementation missing or incompatible on ROCm, or kernel dispatch logic not routing correctly for ROCm backend on compute capability 9.0+ hardware **test_w4a8_cuda_graph in test_cutlass_w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
