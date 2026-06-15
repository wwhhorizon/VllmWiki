# vllm-project/vllm#23256: [Bug]: Qwen2.5-VL GPTQ kernels (Marlin AND Machette) with Tensor Parallelism incorrect AND non-deterministic output since 0.10.0

| 字段 | 值 |
| --- | --- |
| Issue | [#23256](https://github.com/vllm-project/vllm/issues/23256) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL GPTQ kernels (Marlin AND Machette) with Tensor Parallelism incorrect AND non-deterministic output since 0.10.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have a fairly convoluted bug to report which involves very specific conditions. Might be related to https://github.com/vllm-project/vllm/issues/21689 It seems to happen on only a single (closed-source) model, using either vLLM 0.10.0 or 0.10.1, quantized with GPTQModel in int4 W4A16, when tensor parallelism 2 is used, with either 2 A100 or 2 H100 (could not try other GPUs) AND the output depends on the specific GPU model AND on the A100, the output is non-deterministic (even with temperature 0.0). Although ``` --enforce-eager ``` does not resolve the problem, ``` --quantization gptq --dtype float16 ``` does solve the problem (specifying the dtype is mandatory as --quantization gptq is not compatible with bfloat16, the default dtype of the Qwen2.5-VL family). I work at numind and we recently trained models based on Qwen2.5-VL https://huggingface.co/collections/numind/nuextract-20-67c73c445106c12f2b1b6960 . Our models are trained to output json. We also train closed-source models for our clients, including one of our smallest closed-source model, NuExtract32B-GPTQ, baed on Qwen2.5-VL-32B, which is surprisingly the only one affect...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen2.5-VL GPTQ kernels (Marlin AND Machette) with Tensor Parallelism incorrect AND non-deterministic output since 0.10.0 bug;stale ### Your current environment ### 🐛 Describe the bug I have a fairly convoluted b
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 6: GPTQ kernels (Marlin AND Machette) with Tensor Parallelism incorrect AND non-deterministic output since 0.10.0 bug;stale ### Your current environment ### 🐛 Describe the bug I have a fairly convoluted bug to report which...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: only a single (closed-source) model, using either vLLM 0.10.0 or 0.10.1, quantized with GPTQModel in int4 W4A16, when tensor parallelism 2 is used, with either 2 A100 or 2 H100 (could not try other GPUs) AND the output...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: Bug]: Qwen2.5-VL GPTQ kernels (Marlin AND Machette) with Tensor Parallelism incorrect AND non-deterministic output since 0.10.0 bug;stale ### Your current environment ### 🐛 Describe the bug I have a fairly convoluted bu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: the bug I have a fairly convoluted bug to report which involves very specific conditions. Might be related to https://github.com/vllm-project/vllm/issues/21689 It seems to happen on only a single (closed-source) model,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
