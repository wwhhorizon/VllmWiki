# vllm-project/vllm#19004: [Bug]: quantization cli choice not setup after SkipValidation

| 字段 | 值 |
| --- | --- |
| Issue | [#19004](https://github.com/vllm-project/vllm/issues/19004) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: quantization cli choice not setup after SkipValidation

### Issue 正文摘录

### Your current environment vllm main ### 🐛 Describe the bug This is a issue relate to https://github.com/vllm-project/vllm/pull/18843 ### Issue vllm ascend has a quantization extension to extend quantization choice: https://github.com/vllm-project/vllm-ascend/blob/92bc5576d8899cff4e041e20af11a4f1d46aa066/vllm_ascend/platform.py#L76-L80 But after https://github.com/vllm-project/vllm/commit/3c49dbdd03f33fb938bc67230dbc2e8f536ed490 , the quantization choices return None. The problem are found in: https://github.com/vllm-project/vllm-ascend/issues/1042 ``` File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/platform.py", line 79, in pre_register_and_update if ASCEND_QUATIZATION_METHOD not in quant_action.choices: TypeError: argument of type 'NoneType' is not iterable ``` ### Invisitigation: https://github.com/vllm-project/vllm/blob/432ec9926ebd3ce826f0d49df0a2a5ae3cc81ec0/vllm/engine/arg_utils.py#L449 - Expected (Without `SkipValidation`): ``` type_hints { , typing.Literal['aqlm', 'awq', 'deepspeedfp', 'tpu_int8', 'fp8', 'ptpc_fp8', 'fbgemm_fp8', 'modelopt', 'modelopt_fp4', 'marlin', 'bitblas', 'gguf', 'gptq_marlin_24', 'gptq_marlin', 'gptq_bitblas', 'awq_marlin', 'gptq', 'compressed-ten...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: quantization cli choice not setup after SkipValidation bug ### Your current environment vllm main ### 🐛 Describe the bug This is a issue relate to https://github.com/vllm-project/vllm/pull/18843 ### Issue vllm as...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: .Literal['aqlm', 'awq', 'deepspeedfp', 'tpu_int8', 'fp8', 'ptpc_fp8', 'fbgemm_fp8', 'modelopt', 'modelopt_fp4', 'marlin', 'bitblas', 'gguf', 'gptq_marlin_24', 'gptq_marlin', 'gptq_bitblas', 'awq_marlin', 'gptq', 'compre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lm', 'awq', 'deepspeedfp', 'tpu_int8', 'fp8', 'ptpc_fp8', 'fbgemm_fp8', 'modelopt', 'modelopt_fp4', 'marlin', 'bitblas', 'gguf', 'gptq_marlin_24', 'gptq_marlin', 'gptq_bitblas', 'awq_marlin', 'gptq', 'compressed-tensors...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
