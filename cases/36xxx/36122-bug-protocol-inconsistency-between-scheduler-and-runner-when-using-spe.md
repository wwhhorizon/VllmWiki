# vllm-project/vllm#36122: [Bug]: Protocol inconsistency between Scheduler and Runner when using Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#36122](https://github.com/vllm-project/vllm/issues/36122) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Protocol inconsistency between Scheduler and Runner when using Speculative Decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug very specific and serious internal logic error in vLLM, which directly caused the engine to crash (Engine Dead). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#36239 [Bugfix] Remove incorrect assertion blocking mixed decode+spec-decode batches in GDN attention

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ing bug ### Your current environment ### 🐛 Describe the bug very specific and serious internal logic error in vLLM, which directly caused the engine to crash (Engine Dead). ### Before submitting a new issue... - [x] Mak...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Protocol inconsistency between Scheduler and Runner when using Speculative Decoding bug ### Your current environment ### 🐛 Describe the bug very specific and serious internal logic error in vLLM, which directly c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ions. development attention_kv_cache;ci_build;frontend_api;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cuda;quantization;sampling build_error;crash dtype;env_dependency;sha...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: sh dtype;env_dependency;shape #36239 [Bugfix] Remove incorrect assertion blocking mixed decode+spec-decode batches in GDN attention Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36239](https://github.com/vllm-project/vllm/pull/36239) | closes_keyword | 0.95 | [Bugfix] Remove incorrect assertion blocking mixed decode+spec-decode batches in GDN attention | Closes #36122 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
