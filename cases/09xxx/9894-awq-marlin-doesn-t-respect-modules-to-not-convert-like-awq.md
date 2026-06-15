# vllm-project/vllm#9894: AWQ Marlin doesn't respect modules_to_not_convert like AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#9894](https://github.com/vllm-project/vllm/issues/9894) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AWQ Marlin doesn't respect modules_to_not_convert like AWQ

### Issue 正文摘录

When using the AWQ Marlin backend with vLLM, the `modules_to_not_convert` configuration in the model's quantization config is being ignored. This causes an error when attempting to load models that have specific modules marked for exclusion from quantization. ## Steps to Reproduce Attempt to serve Qwen2-VL-2B-Instruct-AWQ model using vLLM with AWQ Marlin backend (on SM>8.0): ```bash vllm serve Qwen/Qwen2-VL-2B-Instruct-AWQ ``` The model fails to load with the following error: ```python ValueError: Unexpected weight: visual.blocks.0.attn.proj.weight ``` ## Expected Behavior - The AWQ Marlin backend should respect the `modules_to_not_convert` configuration - In this case, the "visual" module should be excluded from quantization as specified in the config: ```json "quantization_config": { "bits": 4, "group_size": 128, "modules_to_not_convert": [ "visual" ], "quant_method": "awq", "version": "gemm", "zero_point": true } ``` Originally posted by @cedonley in https://github.com/vllm-project/vllm/issues/9832#issuecomment-2450750777

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: hen using the AWQ Marlin backend with vLLM, the `modules_to_not_convert` configuration in the model's quantization config is being ignored. This causes an error when attempting to load models that have specific modules...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: gnored. This causes an error when attempting to load models that have specific modules marked for exclusion from quantization. ## Steps to Reproduce Attempt to serve Qwen2-VL-2B-Instruct-AWQ model using vLLM with AWQ Ma...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: oesn't respect modules_to_not_convert like AWQ When using the AWQ Marlin backend with vLLM, the `modules_to_not_convert` configuration in the model's quantization config is being ignored. This causes an error when attem...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ve specific modules marked for exclusion from quantization. ## Steps to Reproduce Attempt to serve Qwen2-VL-2B-Instruct-AWQ model using vLLM with AWQ Marlin backend (on SM>8.0): ```bash vllm serve Qwen/Qwen2-VL-2B-Instr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: end with vLLM, the `modules_to_not_convert` configuration in the model's quantization config is being ignored. This causes an error when attempting to load models that have specific modules marked for exclusion from qua...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
