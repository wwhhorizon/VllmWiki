# vllm-project/vllm#12567: [Bug]: V1 Regression: ValueError: could not broadcast input array from shape (y,) into shape (x,)

| 字段 | 值 |
| --- | --- |
| Issue | [#12567](https://github.com/vllm-project/vllm/issues/12567) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 Regression: ValueError: could not broadcast input array from shape (y,) into shape (x,)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When running v0.7.0 with the v1 architecture, I'm frequently encountering: ```ValueError: could not broadcast input array from shape (y,) into shape (x,)``` where x = max_model_len and y > x. This is using the batched/offline interface, and causes the run to error. Without the v1 architecture, it typically handles such cases more gracefully and does not cause the whole run to crash. May be related to: https://github.com/vllm-project/vllm/issues/9848. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error;crash env_dependency;shape Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _No response_ ### 🐛 Describe the bug When running v0.7.0 with the v1 architecture, I'm frequently encountering: ```ValueError: could not broadcast input array from shape (y,) into shape (x,)``` where x = max_model_len a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: V1 Regression: ValueError: could not broadcast input array from shape (y,) into shape (x,) bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When running v0.7.0 with the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error;crash env_dependency;shape Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: from shape (y,) into shape (x,) bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When running v0.7.0 with the v1 architecture, I'm frequently encountering: ```ValueError: could...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
