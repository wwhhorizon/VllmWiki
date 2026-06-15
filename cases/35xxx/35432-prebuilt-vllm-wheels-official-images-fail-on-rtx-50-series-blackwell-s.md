# vllm-project/vllm#35432: Prebuilt vLLM wheels / official images fail on RTX 50-series (Blackwell, SM120/SM121) — "no kernel image" / "sm_120 not compatible"

| 字段 | 值 |
| --- | --- |
| Issue | [#35432](https://github.com/vllm-project/vllm/issues/35432) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda;kernel |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Prebuilt vLLM wheels / official images fail on RTX 50-series (Blackwell, SM120/SM121) — "no kernel image" / "sm_120 not compatible"

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Summary vLLM fails to run on NVIDIA RTX 50-series GPUs (Blackwell, SM120/SM121) when installed from the prebuilt PyPI wheels (and/or official Docker images). The runtime crashes with errors like: - `RuntimeError: CUDA error: no kernel image is available for execution on the device` - or `NVIDIA GeForce RTX 50xx with CUDA capability sm_120 is not compatible with the current PyTorch installation` This looks like the distributed binaries were built without Blackwell arch flags (SM120/SM121), even though the system meets the CUDA minimum for Blackwell. ### Reproduction steps 1. Create a clean environment ```bash python -m venv .venv && source .venv/bin/activate pip install -U pip ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#35568 [Bugfix] Fix SM121 (DGX Spark) exclusion from Marlin/CUTLASS FP8 paths

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Prebuilt vLLM wheels / official images fail on RTX 50-series (Blackwell, SM120/SM121) — "no kernel image" / "sm_120 not compatible" feature request ### 🚀 The feature, motivation and pitch ### Summary vLLM fails to run o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: Prebuilt vLLM wheels / official images fail on RTX 50-series (Blackwell, SM120/SM121) — "no kernel image" / "sm_120 not compatible" feature request ### 🚀 The feature, motivation and pitch ### Summary vLLM fails to run o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: v_dependency #35568 [Bugfix] Fix SM121 (DGX Spark) exclusion from Marlin/CUTLASS FP8 paths 🚀 The feature, motivation and pitch
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ency #35568 [Bugfix] Fix SM121 (DGX Spark) exclusion from Marlin/CUTLASS FP8 paths 🚀 The feature, motivation and pitch
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: well, SM120/SM121) — "no kernel image" / "sm_120 not compatible" feature request ### 🚀 The feature, motivation and pitch ### Summary vLLM fails to run on NVIDIA RTX 50-series GPUs (Blackwell, SM120/SM121) when installed...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35568](https://github.com/vllm-project/vllm/pull/35568) | closes_keyword | 0.95 | [Bugfix] Fix SM121 (DGX Spark) exclusion from Marlin/CUTLASS FP8 paths | Fixes #35432. Fixes #30163. Relates to #30135. Contributed by Second Nature Computing (https://joinsecondnature.com) ## Test plan - [x] Validated on SM121a hardware (DGX Spark) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
