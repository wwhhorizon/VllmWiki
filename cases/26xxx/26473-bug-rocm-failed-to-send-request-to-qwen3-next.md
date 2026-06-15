# vllm-project/vllm#26473: [Bug][ROCm]: Failed to send request to Qwen3-Next

| 字段 | 值 |
| --- | --- |
| Issue | [#26473](https://github.com/vllm-project/vllm/issues/26473) |
| 状态 | closed |
| 标签 | bug;feature request;rocm |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm]: Failed to send request to Qwen3-Next

### Issue 正文摘录

### Your current environment ## Bug info Platform: AMD GPU MI355X Docker version: rocm/vllm-dev:nightly_main_20251008 a841ff1c934f ### 🐛 Describe the bug ## Reproduce steps pull docker of `rocm/vllm-dev:nightly_main_20251008` and run following script ## Error message ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#31380 [Bugfix][ROCm]Fix Qwen3-Next-80B-A3B-Thinking inference and optimize non-standard block size (544) support under rocm_atten | #38180 [Bugfix][Backport][ROCm] Backport PR #31380 to v0.13.0: Fix Qwen3-Next inference with non-standard block size (544)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: cm ### Your current environment ## Bug info Platform: AMD GPU MI355X Docker version: rocm/vllm-dev:nightly_main_20251008 a841ff1c934f ### 🐛 Describe the bug ## Reproduce steps pull docker of `rocm/vllm-dev:nightly_main_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug][ROCm]: Failed to send request to Qwen3-Next bug;feature request;rocm ### Your current environment ## Bug info Platform: AMD GPU MI355X Docker version: rocm/vllm-dev:nightly_main_20251008 a841ff1c934f ### 🐛 Describ
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug][ROCm]: Failed to send request to Qwen3-Next bug;feature request;rocm ### Your current environment ## Bug info Platform: AMD GPU MI355X Docker version: rocm/vllm-dev:nightly_main_20251008 a841ff1c934f ### 🐛 Describ...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug][ROCm]: Failed to send request to Qwen3-Next bug;feature request;rocm ### Your current environment ## Bug info Platform: AMD GPU MI355X Docker version: rocm/vllm-dev:nightly_main_20251008 a841ff1c934f ### 🐛 Describ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: hardware_porting;model_support;speculative_decoding cuda;kernel;operator;triton build_error env_dependency #31380 [Bugfix][ROCm]Fix Qwen3-Next-80B-A3B-Thinking inference and optimize non-standard block size (544) suppor...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31380](https://github.com/vllm-project/vllm/pull/31380) | closes_keyword | 0.95 | [Bugfix][ROCm]Fix Qwen3-Next-80B-A3B-Thinking inference and optimize non-standard block size (544) support under rocm_atten | Fixes #26473 This PR refactors the rocm_attn backend kernels to support models with non-power-of-2 block sizes, specifically the Qwen/Qwen3-Next-80B-A3B-Thinking model. The core |
| [#38180](https://github.com/vllm-project/vllm/pull/38180) | mentioned | 0.6 | [Bugfix][Backport][ROCm] Backport PR #31380 to v0.13.0: Fix Qwen3-Next inference with non-standard block size (544) | ginal PR: #31380 - Target branch: `releases/v0.13.0` - Related issue: #26473 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
