# vllm-project/vllm#27152: [Perf][Qwen3-next]: `torch.compile` GDN attn

| 字段 | 值 |
| --- | --- |
| Issue | [#27152](https://github.com/vllm-project/vllm/issues/27152) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | cold_start |
| Operator 关键词 | activation;attention;cache;cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Perf][Qwen3-next]: `torch.compile` GDN attn

### Issue 正文摘录

### Proposal to improve performance Right now GDN attn (`Qwen3NextGatedDeltaNet`) (used in Qwen3-next) aren't covered by `torch.compile`. GDN unlike full attn contain a lot of operators including a lot of elementwise. Below is illustration Right now GDN attn implemented as custom op and `torch.compile` doesn't go inside. I wrote the following script that call vllm's GDN attn and measured performance. Covering `Qwen3NextGatedDeltaNet._forward` with torch.compile(mode=“max-autotune-no-cudagraphs”) gaves 14% perf improvement. That corresponds to 4-5% E2E perf on Qwen3-next.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Perf][Qwen3-next]: `torch.compile` GDN attn performance ### Proposal to improve performance Right now GDN attn (`Qwen3NextGatedDeltaNet`) (used in Qwen3-next) aren't covered by `torch.compile`. GDN unlike full attn con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Perf][Qwen3-next]: `torch.compile` GDN attn performance ### Proposal to improve performance Right now GDN attn (`Qwen3NextGatedDeltaNet`) (used in Qwen3-next) aren't covered by `torch.compile`. GDN unlike full attn con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: model_support activation;attention;cache;cuda;operator build_error;crash dtype;env_dependency;race_condition;shape Proposal to improve performance
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: wen3NextGatedDeltaNet._forward` with torch.compile(mode=“max-autotune-no-cudagraphs”) gaves 14% perf improvement. That corresponds to 4-5% E2E perf on Qwen3-next. performance activation_norm;attention_kv_cache;ci_build;...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
