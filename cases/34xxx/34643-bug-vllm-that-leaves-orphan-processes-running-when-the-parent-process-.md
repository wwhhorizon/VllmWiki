# vllm-project/vllm#34643: [Bug]: vLLM that leaves orphan processes running when the parent process dies due to OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#34643](https://github.com/vllm-project/vllm/issues/34643) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM that leaves orphan processes running when the parent process dies due to OOM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM that leaves orphan processes running when the parent process dies due to OOM ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ts of frequently asked questions. performance frontend_api;model_support;quantization;sampling_logits;scheduler_memory cuda;quantization crash;oom dtype;env_dependency;shape Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: OOM ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ves orphan processes running when the parent process dies due to OOM bug;stale ### Your current environment ### 🐛 Describe the bug vLLM that leaves orphan processes running when the parent process dies due to OOM ### Be...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n;sampling_logits;scheduler_memory cuda;quantization crash;oom dtype;env_dependency;shape Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: that leaves orphan processes running when the parent process dies due to OOM bug;stale ### Your current environment ### 🐛 Describe the bug vLLM that leaves orphan processes running when the parent process dies due to OO...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
