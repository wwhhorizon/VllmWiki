# vllm-project/vllm#25864: [Bug]:  FlexAttention does not support sliding window yet !!!

| 字段 | 值 |
| --- | --- |
| Issue | [#25864](https://github.com/vllm-project/vllm/issues/25864) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  FlexAttention does not support sliding window yet !!!

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Getting this error. Please resolve this issue. "FlexAttention does not support sliding window yet." ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tion_kv_cache;distributed_parallel;model_support attention;cuda;operator build_error;crash env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t." ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tly asked questions. development attention_kv_cache;distributed_parallel;model_support attention;cuda;operator build_error;crash env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: FlexAttention does not support sliding window yet !!! bug;stale ### Your current environment ### 🐛 Describe the bug Getting this error. Please resolve this issue. "FlexAttention does not support sliding window ye...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development attention_kv_cache;distributed_parallel;model_support attention;cuda;oper...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
