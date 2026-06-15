# vllm-project/vllm#32269: [Feature]:  Benchmark torch._scaled_mm performance with and without padding

| 字段 | 值 |
| --- | --- |
| Issue | [#32269](https://github.com/vllm-project/vllm/issues/32269) |
| 状态 | closed |
| 标签 | help wanted;feature request |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;gemm;kernel;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]:  Benchmark torch._scaled_mm performance with and without padding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Torch scaled matmul kernels currently pad the batch/token dimension to 17 when batch_size 16. This optimization should be benchmarked to see whether it still helps or not. Ideally end-to-end benchmarks should be performed on a decent variety of models on both CUDA and ROCm platforms. Current Behavior In [vllm/vllm/model_executor/layers/quantization/utils/w8a8_utils.py](https://github.com/vllm-project/vllm/blob/4f3676e72628ac067330e3acbf769d92afc2f7ea/vllm/model_executor/layers/quantization/utils/w8a8_utils.py#L423) ```python # Note: we pad the input because torch._scaled_mm is more performant # for matrices with batch dimension > 16. # This could change in the future. # We also don't pad when using torch.compile, # as it breaks with dynamic shapes. if pad_output is None: config = get_current_vllm_config().compilation_config pad_output = ( config.mode < CompilationMode.VLLM_COMPILE and self.preferred_backend == "torch" ) ``` This padding value is passed to: 1. QuantFP8 as num_token_padding parameter 2. Input tensors are padded before FP8 quantization 3. Output tensors are unpadded after matmul via torch.narrow(output, 0, 0, output_shape[0]) #...

## 现有链接修复摘要

#27814 [Refactor] Make FP8 Linear Ops use kernel abstraction

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: could change in the future. # We also don't pad when using torch.compile, # as it breaks with dynamic shapes. if pad_output is None: config = get_current_vllm_config().compilation_config pad_output = ( config.mode < Com...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature]: Benchmark torch._scaled_mm performance with and without padding help wanted;feature request ### 🚀 The feature, motivation and pitch Torch scaled matmul kernels currently pad the batch/token dimension to 17 wh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: end benchmarks should be performed on a decent variety of models on both CUDA and ROCm platforms. Current Behavior In [vllm/vllm/model_executor/layers/quantization/utils/w8a8_utils.py](https://github.com/vllm-project/vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Ideally end-to-end benchmarks should be performed on a decent variety of models on both CUDA and ROCm platforms. Current Behavior In [vllm/vllm/model_executor/layers/quantization/utils/w8a8_utils.py](https://github.com/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Benchmark torch._scaled_mm performance with and without padding help wanted;feature request ### 🚀 The feature, motivation and pitch Torch scaled matmul kernels currently pad the batch/token dimension to 17 wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27814](https://github.com/vllm-project/vllm/pull/27814) | mentioned | 0.6 | [Refactor] Make FP8 Linear Ops use kernel abstraction | p after merging this PR: - [ ] #31818 and unify `TestFP8Layer` - [x] #32269 - [ ] #32268 - [ ] Add `VLLM_DISABLED_KERNELS` to `vllm.envs` ## Test Plan End-to-end model evaluations… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
