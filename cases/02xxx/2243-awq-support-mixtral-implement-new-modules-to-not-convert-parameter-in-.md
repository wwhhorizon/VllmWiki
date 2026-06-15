# vllm-project/vllm#2243: AWQ (Support Mixtral): Implement new `modules_to_not_convert` parameter in config

| 字段 | 值 |
| --- | --- |
| Issue | [#2243](https://github.com/vllm-project/vllm/issues/2243) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AWQ (Support Mixtral): Implement new `modules_to_not_convert` parameter in config

### Issue 正文摘录

AutoAWQ now supports Mixtral on the main branch. It requires that we do not quantize the `gate` in the model. To prevent quantizing and loading it as a quantized linear layer, you have to skip loading the `modules_to_not_convert` as quantized linear layers. You can load this 4-bit model in ~24 GB VRAM, but you probably need a bit more for actual KV-caching and inference. I used a 48 GB VRAM GPU for my testing. ```json "quantization_config": { "bits": 4, "group_size": 128, "modules_to_not_convert": [ "gate" ], "quant_method": "awq", "version": "gemm", "zero_point": true }, ``` Model reference: https://huggingface.co/casperhansen/mixtral-instruct-awq

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Q (Support Mixtral): Implement new `modules_to_not_convert` parameter in config AutoAWQ now supports Mixtral on the main branch. It requires that we do not quantize the `gate` in the model. To prevent quantizing and loa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s_to_not_convert": [ "gate" ], "quant_method": "awq", "version": "gemm", "zero_point": true }, ``` Model reference: https://huggingface.co/casperhansen/mixtral-instruct-awq
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: oAWQ now supports Mixtral on the main branch. It requires that we do not quantize the `gate` in the model. To prevent quantizing and loading it as a quantized linear layer, you have to skip loading the `modules_to_not_c...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: nvert": [ "gate" ], "quant_method": "awq", "version": "gemm", "zero_point": true }, ``` Model reference: https://huggingface.co/casperhansen/mixtral-instruct-awq
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: more for actual KV-caching and inference. I used a 48 GB VRAM GPU for my testing. ```json "quantization_config": { "bits": 4, "group_size": 128, "modules_to_not_convert": [ "gate" ], "quant_method": "awq", "version": "g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
