# vllm-project/vllm#39521: [Tracking] NIXL >= 1.0.0 Support for NIXL KV Connector

| 字段 | 值 |
| --- | --- |
| Issue | [#39521](https://github.com/vllm-project/vllm/issues/39521) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Tracking] NIXL >= 1.0.0 Support for NIXL KV Connector

### Issue 正文摘录

## Summary NIXL [v1.0.0](https://github.com/ai-dynamo/nixl/releases/tag/v1.0.0) was released on 2026-03-13 with several API changes. vLLM currently pins `nixl[cu13] >= 0.7.1, https://github.com/ai-dynamo/nixl/pull/1574: : This PR will fix a lot of the packaging issues faced by vllm to install nixl. Basically there is no more selector needed, just pip install nixl will be sufficient, both CUDA backends will be installed and the right one will be selected at runtime based on the torch CUDA version ## Changes in NIXL 1.0.0 [API Change ](https://github.com/ai-dynamo/nixl/pull/1342): Doesn't affect vllm implementation. Issues: See comments below. cc @NickLucche ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#39851 [CI][NIXL] Fix PD CI breakage: pin nixl-cu{12,13} versions

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: /1574: : This PR will fix a lot of the packaging issues faced by vllm to install nixl. Basically there is no more selector needed, just pip install nixl will be sufficient, both CUDA backends will be installed and the r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: no more selector needed, just pip install nixl will be sufficient, both CUDA backends will be installed and the right one will be selected at runtime based on the torch CUDA version ## Changes in NIXL 1.0.0 [API Change...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ore selector needed, just pip install nixl will be sufficient, both CUDA backends will be installed and the right one will be selected at runtime based on the torch CUDA version ## Changes in NIXL 1.0.0 [API Change ](ht...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api cuda env_dependency #39851 [CI...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39851](https://github.com/vllm-project/vllm/pull/39851) | closes_keyword | 0.95 | [CI][NIXL] Fix PD CI breakage: pin nixl-cu{12,13} versions | fix: pin `nixl-cu12` and `nixl-cu13` to `< 0.10.0`. @NickLucche is working on the proper version bump in #39797 (tracking #39521). |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
