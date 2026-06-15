# vllm-project/vllm#22195: [Feature]: Support Mixed-Precision KV Cache Configuration

| 字段 | 值 |
| --- | --- |
| Issue | [#22195](https://github.com/vllm-project/vllm/issues/22195) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Mixed-Precision KV Cache Configuration

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, vLLM's support for FP8 KV Cache only allows a global uniform format (e.g., full e4m3 or e5m2). However, in practice, different model layers exhibit significant variations in sensitivity to quantization precision. For example, middle layers of Llama-3 may be more sensitive to precision loss with e4m3, while early layers may better suit e5m2's dynamic range. This feature proposes to support mixed-precision KV Cache, including: 1. Allowing users to specify layer-wise format policies via configuration files (e.g., JSON/YAML) such as `layer 0-10: e5m2, layer 11-30: e4m3`; 2. Framework-automatic identification of critical layers (via quantization sensitivity analysis, e.g., layers with high impact on output logits) and assigning higher-precision formats (e.g., e4m3) to them, while using e5m2 for non-critical layers; 3. Resolving attention computation compatibility under mixed formats, such as unifying precision before matrix multiplication or leveraging hardware-native FP8 conversion units (e.g., Hopper) to accelerate cross-format calculations. The core value of this feature is to further reduce precision loss while maintaining high thr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Support Mixed-Precision KV Cache Configuration feature request;stale ### 🚀 The feature, motivation and pitch Currently, vLLM's support for FP8 KV Cache only allows a global uniform format (e.g., full e4m3 or...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: [Feature]: Support Mixed-Precision KV Cache Configuration feature request;stale ### 🚀 The feature, motivation and pitch Currently, vLLM's support for FP8 KV Cache only allows a global uniform format (e.g., full e4m3 or...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Support Mixed-Precision KV Cache Configuration feature request;stale ### 🚀 The feature, motivation and pitch Currently, vLLM's support for FP8 KV Cache only allows a global uniform format (e.g., full e4m3 or...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e ### 🚀 The feature, motivation and pitch Currently, vLLM's support for FP8 KV Cache only allows a global uniform format (e.g., full e4m3 or e5m2). However, in practice, different model layers exhibit significant variat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: multiplication or leveraging hardware-native FP8 conversion units (e.g., Hopper) to accelerate cross-format calculations. The core value of this feature is to further reduce precision loss while maintaining high through...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
