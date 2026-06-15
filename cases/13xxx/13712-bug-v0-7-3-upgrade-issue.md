# vllm-project/vllm#13712: [Bug]: v0.7.3 upgrade issue,

| 字段 | 值 |
| --- | --- |
| Issue | [#13712](https://github.com/vllm-project/vllm/issues/13712) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.7.3 upgrade issue,

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug issue after upgrade from v0.7,2 to v0.7.3 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory attention;cache;cuda;operator;quantization;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory attention;cache;cuda;operator;quantization;sampling build_error;crash;slowdown dtype;env_dependency;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 7.3 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: v0.7.3 upgrade issue, bug;stale ### Your current environment ### 🐛 Describe the bug issue after upgrade from v0.7,2 to v0.7.3 ### Before submitting a new issue... - [x] Make sure you already searched for relevant...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: erformance attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory attention;cache;cuda;operator;quantization;sampling build_error;crash;slowdown dtype;e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
