# vllm-project/vllm#1258: Some models with `awq` quantization cannot using 4 tensor parallism

| 字段 | 值 |
| --- | --- |
| Issue | [#1258](https://github.com/vllm-project/vllm/issues/1258) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Some models with `awq` quantization cannot using 4 tensor parallism

### Issue 正文摘录

When i use this https://huggingface.co/TheBloke/WizardCoder-Python-7B-V1.0-AWQ model with TP4, it will raise `Group size should be a multiple of 32` in `gemm_kernels.cu` file. https://github.com/vllm-project/vllm/blob/acbed3ef40f015fcf64460e629813922fab90380/csrc/quantization/awq/gemm_kernels.cu#L465 And i digged it into more, I find that `intermediate_size` of `WizardCoder-Python-7B-V1.0-AWQ` is 11008. So when using TP4, `reshaped_x`'s shape in `apply_weights` of `AWQRowParallelLinear` class will be `11008/4=2752`. https://github.com/vllm-project/vllm/blob/acbed3ef40f015fcf64460e629813922fab90380/vllm/model_executor/layers/quantized_linear/awq.py#L100 Then in line `int group_size = num_in_channels / _scaling_factors.size(0);` will equal to `int group_size = 2752 / 8`, so the group_size will be `344`. And we know `344 % 32 = 24` that doesn'e equal to 0. https://github.com/vllm-project/vllm/blob/acbed3ef40f015fcf64460e629813922fab90380/csrc/quantization/awq/gemm_kernels.cu#L458 I have no idea to solve this.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Some models with `awq` quantization cannot using 4 tensor parallism When i use this https://huggingface.co/TheBloke/WizardCoder-Python-7B-V1.0-AWQ model with TP4, it will raise `Group size should be a multiple of 32` in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Some models with `awq` quantization cannot using 4 tensor parallism When i use this https://huggingface.co/TheBloke/WizardCoder-Python-7B-V1.0-AWQ model with TP4, it will raise `Group size should be a multiple of 32` in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Some models with `awq` quantization cannot using 4 tensor parallism When i use this https://huggingface.co/TheBloke/WizardCoder-Python-7B-V1.0-AWQ model with TP4, it will raise `Group size should be a multiple of 32` in...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: odel with TP4, it will raise `Group size should be a multiple of 32` in `gemm_kernels.cu` file. https://github.com/vllm-project/vllm/blob/acbed3ef40f015fcf64460e629813922fab90380/csrc/quantization/awq/gemm_kernels.cu#L4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
