# vllm-project/vllm#16490: [Performance]: fp8 Online Quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#16490](https://github.com/vllm-project/vllm/issues/16490) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;kernel;quantization |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: fp8 Online Quantization

### Issue 正文摘录

### Proposal to improve performance hello, I saw the following sentence in the official documentation： ``` https://docs.vllm.ai/en/latest/features/quantization/fp8.html vLLM supports FP8 (8-bit floating point) weight and activation quantization using hardware acceleration on GPUs such as Nvidia H100 and AMD MI300x. Currently, only Hopper and Ada Lovelace GPUs are officially supported for W8A8. Ampere GPUs are supported for W8A16 (weight-only FP8) utilizing Marlin kernels. Quantization of models with FP8 allows for a 2x reduction in model memory requirements and up to a 1.6x improvement in throughput with minimal impact on accuracy. ``` After using fp8 quantization, the throughput becomes 2.6 times that of using bf16？ What model did you test on, what GPU and num did you use, what concurrency was used, and what was the input and output length to achieve this effect? can you give the detail information?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: tivation quantization using hardware acceleration on GPUs such as Nvidia H100 and AMD MI300x. Currently, only Hopper and Ada Lovelace GPUs are officially supported for W8A8. Ampere GPUs are supported for W8A16 (weight-o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Performance]: fp8 Online Quantization performance;stale ### Proposal to improve performance hello, I saw the following sentence in the official documentation： ``` https://docs.vllm.ai/en/latest/features/quantization/fp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ng sentence in the official documentation： ``` https://docs.vllm.ai/en/latest/features/quantization/fp8.html vLLM supports FP8 (8-bit floating point) weight and activation quantization using hardware acceleration on GPU...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ed for W8A16 (weight-only FP8) utilizing Marlin kernels. Quantization of models with FP8 allows for a 2x reduction in model memory requirements and up to a 1.6x improvement in throughput with minimal impact on accuracy....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ements and up to a 1.6x improvement in throughput with minimal impact on accuracy. ``` After using fp8 quantization, the throughput becomes 2.6 times that of using bf16？ What model did you test on, what GPU and num did...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
