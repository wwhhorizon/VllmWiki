# vllm-project/vllm#16589: [Bug]: Whisper reqires multi-cpu for profiling multi-modal model

| 字段 | 值 |
| --- | --- |
| Issue | [#16589](https://github.com/vllm-project/vllm/issues/16589) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Whisper reqires multi-cpu for profiling multi-modal model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to run `whisper` with this config, but it was stuck at `Starting profile run for multi-modal models`. I resolved this by changing `cpu` resources to 3, but I don't think that this should be required ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory attention;cuda;quantization dtype;env_dependency Your curre...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Whisper reqires multi-cpu for profiling multi-modal model bug;stale ### Your current environment ### 🐛 Describe the bug I tried to run `whisper` with this config, but it was stuck at `Starting profile run for mul...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory attention;cuda;quantization dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: red ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Whisper reqires multi-cpu for profiling multi-modal model bug;stale ### Your current environment ### 🐛 Describe the bug I tried to run `whisper` with this config, but it was stuck at `Starting profile run for mul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
