# vllm-project/vllm#25097: [Feature]: TPU Support for Prompt Embeds

| 字段 | 值 |
| --- | --- |
| Issue | [#25097](https://github.com/vllm-project/vllm/issues/25097) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: TPU Support for Prompt Embeds

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The existing v0 implementation of prompt embeds does not support TPU workers (only GPU). The implementation in #24278 supports both CUDA and CPU, but not TPU. It would be nice to support TPU when using prompt embeds, or at least explicitly raise a error when `--enable-prompt-embeds` EngineArg is True when vLLM is built for TPU support. I don't have easy access to a TPU, nor am I familiar with that platform, so I did not do this work in #24278. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#24278 [CORE] Prompt Embeddings Support for v1 Engine

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pport TPU workers (only GPU). The implementation in #24278 supports both CUDA and CPU, but not TPU. It would be nice to support TPU when using prompt embeds, or at least explicitly raise a error when `--enable-prompt-em...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: TPU Support for Prompt Embeds feature request;stale ### 🚀 The feature, motivation and pitch The existing v0 implementation of prompt embeds does not support TPU workers (only GPU). The implementation in #2427...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: would be nice to support TPU when using prompt embeds, or at least explicitly raise a error when `--enable-prompt-embeds` EngineArg is True when vLLM is built for TPU support. I don't have easy access to a TPU, nor am I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development frontend_api;hardware_porting cuda #24278 [CORE] Prompt Embeddings Suppor...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24278](https://github.com/vllm-project/vllm/pull/24278) | mentioned | 0.45 | [CORE] Prompt Embeddings Support for v1 Engine | u, nor am i familiar with that platform, so i did not do this work in #24278. ### alternatives _no response_ ### additional context _no response_ ### before submitting a new issue… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
