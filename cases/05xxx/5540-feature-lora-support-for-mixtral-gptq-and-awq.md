# vllm-project/vllm#5540: [Feature]: LoRA support for Mixtral GPTQ and AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#5540](https://github.com/vllm-project/vllm/issues/5540) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;kernel;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: LoRA support for Mixtral GPTQ and AWQ

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Please consider adding support for GPTQ and AWQ quantized Mixtral models. I guess that after #4012 it's technically possible. ### Alternatives _No response_ ### Additional context

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: es _No response_ ### Additional context performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization attention;cuda;kernel;quantization crash dtype;env_dependency 🚀 The feature, m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e, motivation and pitch Please consider adding support for GPTQ and AWQ quantized Mixtral models. I guess that after #4012 it's technically possible. ### Alternatives _No response_ ### Additional context performance att...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: LoRA support for Mixtral GPTQ and AWQ feature request;stale ### 🚀 The feature, motivation and pitch Please consider adding support for GPTQ and AWQ quantized Mixtral models. I guess that after #4012 it's tech...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d;distributed_parallel;frontend_api;model_support;quantization attention;cuda;kernel;quantization crash dtype;env_dependency 🚀 The feature, motivation and pitch
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: pitch Please consider adding support for GPTQ and AWQ quantized Mixtral models. I guess that after #4012 it's technically possible. ### Alternatives _No response_ ### Additional context performance attention_kv_cache;ci...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
