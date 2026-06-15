# vllm-project/vllm#24112: [RFC]:  Improve MoE triton kernel tuning

| 字段 | 值 |
| --- | --- |
| Issue | [#24112](https://github.com/vllm-project/vllm/issues/24112) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]:  Improve MoE triton kernel tuning

### Issue 正文摘录

### Motivation. Different triton versions produce different MoE tuned configurations. For example, the triton `3.4.0` [tuned config](https://github.com/jeejeelee/vllm/blob/improve-moe-tune-config/vllm/model_executor/layers/fused_moe/configs/triton_3_4_0/E%3D128%2CN%3D768%2Cdevice_name%3DNVIDIA_H20-3e%2Cdtype%3Dfp8_w8a8%2Cblock_shape%3D%5B128%2C128%5D.json) differs from [the config](https://github.com/vllm-project/vllm/blob/v0.10.1.1/vllm/model_executor/layers/fused_moe/configs/E%3D128%2CN%3D768%2Cdevice_name%3DNVIDIA_H20-3e%2Cdtype%3Dfp8_w8a8%2Cblock_shape%3D%5B128%2C128%5D.json) on version 0.10.1.1. These differences may impact model performance. This RFC mainly discusses how to handle different versions of triton tuned config. ### Proposed Change. We want to: - Split the MoE tuned config into N folders (currently only contains `legacy_configs` and `triton_3_4_0`). `legacy_configs` represents the folder for configurations that cannot be traced back to the committed triton version, while `triton_3_4_0` represents the folder for the corresponding triton version, which is currently `3.4.0`. As triton versions are updated, there may be more triton version folders. See: https://github...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e/configs/triton_3_4_0/E%3D128%2CN%3D768%2Cdevice_name%3DNVIDIA_H20-3e%2Cdtype%3Dfp8_w8a8%2Cblock_shape%3D%5B128%2C128%5D.json) differs from [the config](https://github.com/vllm-project/vllm/blob/v0.10.1.1/vllm/model_ex...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e ### Motivation. Different triton versions produce different MoE tuned configurations. For example, the triton `3.4.0` [tuned config](https://github.com/jeejeelee/vllm/blob/improve-moe-tune-config/vllm/model_executor/l...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: /github.com/vllm-project/vllm/pull/24113 - Add documentation related to `benchmark_moe`, including how to benchmark, how to pass local tuned configs through `VLLM_TUNED_CONFIG_FOLDER`, etc. This will encourage more user...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [RFC]: Improve MoE triton kernel tuning RFC;stale ### Motivation. Different triton versions produce different MoE tuned configurations. For example, the triton `3.4.0` [tuned config](https://github.com/jeejeelee/vllm/bl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ove MoE triton kernel tuning RFC;stale ### Motivation. Different triton versions produce different MoE tuned configurations. For example, the triton `3.4.0` [tuned config](https://github.com/jeejeelee/vllm/blob/improve-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
