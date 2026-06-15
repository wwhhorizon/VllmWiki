# vllm-project/vllm#28857: [Bug]: VLLM 0.11.0 with Gemma3-awq is totaly broken to start (not possible to start awq of gemma3-27b-awq

| 字段 | 值 |
| --- | --- |
| Issue | [#28857](https://github.com/vllm-project/vllm/issues/28857) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: VLLM 0.11.0 with Gemma3-awq is totaly broken to start (not possible to start awq of gemma3-27b-awq

### Issue 正文摘录

### Your current environment I used VLLM 0.11.0 with transformers 4.46 vllm serve gaunernst/gemma-3-27b-it-int4-awq -tp 2 --port 10004 --gpu-memory-utilization 0.68 --swap-space 0.01 --served-model-name gemma-3-27b --dtype bfloat16 Value error, torch.bfloat16 is not supported for quantization method awq. Supported dtypes: [torch.float16] [type=value_error, input_value=ArgsKwargs((), {'model_co...additional_config': {}}), input_type=ArgsKwargs] (APIServer pid=4185) For further information visit https://errors.pydantic.dev/2.11/v/value_erro vllm serve gaunernst/gemma-3-27b-it-int4-awq -tp 2 --port 10004 --gpu-memory-utilization 0.68 --swap-space 0.01 --served-model-name gemma-3-27b --dtype half Value error, The model type 'gemma3' does not support float16. Reason: Numerical instability. Please use bfloat16 or float32 instead. [type=value_error, input_value=ArgsKwargs((), {'model': ...rocessor_plugin': None}), input_type=ArgsKwargs vllm serve gaunernst/gemma-3-27b-it-int4-awq -tp 2 --port 10004 --gpu-memory-utilization 0.68 --swap-space 0.01 --served-model-name gemma-3-27b Value error, torch.float32 is not supported for quantization method awq. Supported dtypes: [torch.float16] [type...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: VLLM 0.11.0 with transformers 4.46 vllm serve gaunernst/gemma-3-27b-it-int4-awq -tp 2 --port 10004 --gpu-memory-utilization 0.68 --swap-space 0.01 --served-model-name gemma-3-27b --dtype bfloat16 Value error, torch.bflo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: VLLM 0.11.0 with Gemma3-awq is totaly broken to start (not possible to start awq of gemma3-27b-awq bug;stale ### Your current environment I used VLLM 0.11.0 with transformers 4.46 vllm serve gaunernst/gemma-3-27b...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: f Value error, The model type 'gemma3' does not support float16. Reason: Numerical instability. Please use bfloat16 or float32 instead. [type=value_error, input_value=ArgsKwargs((), {'model': ...rocessor_plugin': None})...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ee: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: VLLM 0.11.0 with Gemma3-awq is totaly broken to start (not possible to start awq of gemma3-27b-awq bug;stale ### Your current environment I used VLLM 0.11.0 with transformers 4.46 vllm serve gaunernst/gemma-3-27b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
