# vllm-project/vllm#31689: [Feature][Quantization][Help Wanted]: Clean up GPTQ + AWQ Quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#31689](https://github.com/vllm-project/vllm/issues/31689) |
| 状态 | closed |
| 标签 | help wanted;feature request |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Quantization][Help Wanted]: Clean up GPTQ + AWQ Quantization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We are in process of cleaning up the quantization integrations in vllm (see the FusedMoE refactor PRs I am working on) In general, this means we are trying to separate concerns of the quantization INTEGRATION (on disk format --- responsible for weight loading) from the quantization KERNEL (runtime format --- responsible for executing at runtime). For GPTQ/AWQ, we have tech debt in that we have different quantization integrations (`gptq.py`, `gptq_marlin.py`, `awq.py`, `awq_marlin.py`, `wna16.py`, `cpuwna16.py`) and we use the `override_quantization_method` to select between them during initialization. This is generally hard to follow and is not adhereing to the abstractions we have in vllm. Currently, some (but not all) quantization schemes follow the proper abstractions, where we have a full separating of concerns. Examples are: - [Fp8Moe](https://github.com/vllm-project/vllm/blob/b53b89fdb3f4a857eabee5091187cfa937502711/vllm/model_executor/layers/quantization/fp8.py#L722) which follows the proper structure to run a variety of different kernels hooked up to fp8 models - [CompressedTensorsWNA16](https://github.com/vllm-project/vllm/blob/b53b...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature][Quantization][Help Wanted]: Clean up GPTQ + AWQ Quantization help wanted;feature request ### 🚀 The feature, motivation and pitch We are in process of cleaning up the quantization integrations in vllm (see the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: are trying to separate concerns of the quantization INTEGRATION (on disk format --- responsible for weight loading) from the quantization KERNEL (runtime format --- responsible for executing at runtime). For GPTQ/AWQ, w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ocess of cleaning up the quantization integrations in vllm (see the FusedMoE refactor PRs I am working on) In general, this means we are trying to separate concerns of the quantization INTEGRATION (on disk format --- re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tion][Help Wanted]: Clean up GPTQ + AWQ Quantization help wanted;feature request ### 🚀 The feature, motivation and pitch We are in process of cleaning up the quantization integrations in vllm (see the FusedMoE refactor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
