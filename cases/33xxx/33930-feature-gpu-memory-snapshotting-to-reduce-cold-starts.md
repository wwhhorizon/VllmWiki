# vllm-project/vllm#33930: [Feature]: GPU Memory Snapshotting to reduce cold starts

| 字段 | 值 |
| --- | --- |
| Issue | [#33930](https://github.com/vllm-project/vllm/issues/33930) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;moe |
| 子分类 | memory |
| Operator 关键词 | cuda;moe |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: GPU Memory Snapshotting to reduce cold starts

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I noticed that Modal (https://modal.com/blog/gpu-mem-snapshots) and InferX (https://inferx.net/) have implemented the CUDA checkpoint/restore API to drastically reduce cold start. I tried both of the services and it seems to work extremelly well. InferX told me they build it on top of vLLM so it definitly seems possible to do. Right now, I'm not aware of any open source implementation of this tech. I would love to see this feature implemented in vLLM as it would allow for truely usable multi-model capabilities. It would also allow hosting platforms to host more models and to be able to host custom models for way cheaper make users only pay for working GPU time. Note that I'm really not an expert. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#35934 feat: add suspend()/resume() for CRIU-safe snapshots

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: f the services and it seems to work extremelly well. InferX told me they build it on top of vLLM so it definitly seems possible to do. Right now, I'm not aware of any open source implementation of this tech. I would lov...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: gpu-mem-snapshots) and InferX (https://inferx.net/) have implemented the CUDA checkpoint/restore API to drastically reduce cold start. I tried both of the services and it seems to work extremelly well. InferX told me th...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: r make users only pay for working GPU time. Note that I'm really not an expert. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already search...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: GPU Memory Snapshotting to reduce cold starts feature request ### 🚀 The feature, motivation and pitch I noticed that Modal (https://modal.com/blog/gpu-mem-snapshots) and InferX (https://inferx.net/) have impl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: is feature implemented in vLLM as it would allow for truely usable multi-model capabilities. It would also allow hosting platforms to host more models and to be able to host custom models for way cheaper make users only...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35934](https://github.com/vllm-project/vllm/pull/35934) | mentioned | 0.6 | feat: add suspend()/resume() for CRIU-safe snapshots | quires (NCCL teardown before checkpoint, rebuild after restore). \| \| [#33930](https://github.com/vllm-project/vllm/issues/33930) \| [Feature]: GPU Memory Snapshotting to reduce col… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
