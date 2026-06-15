# vllm-project/vllm#23935: [Bug]: No platform detected, vLLM is running on UnspecifiedPlatform in Docker with Kubernetes, Nvidia L4

| 字段 | 值 |
| --- | --- |
| Issue | [#23935](https://github.com/vllm-project/vllm/issues/23935) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: No platform detected, vLLM is running on UnspecifiedPlatform in Docker with Kubernetes, Nvidia L4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to deploy multiple models in GKE using docker images version > 0.8.5 (like mistral-small-3.2 and gptoss-20b) and I get the following error: ```text DEBUG 08-29 04:29:54 [__init__.py:30] No plugins for group vllm.platform_plugins found. DEBUG 08-29 04:29:54 [__init__.py:34] Checking if TPU platform is available. DEBUG 08-29 04:29:54 [__init__.py:52] TPU platform is not available because: No module named 'libtpu' DEBUG 08-29 04:29:54 [__init__.py:58] Checking if CUDA platform is available. DEBUG 08-29 04:29:54 [__init__.py:82] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBUG 08-29 04:29:54 [__init__.py:99] CUDA platform is not available because: NVML Shared Library Not Found DEBUG 08-29 04:29:54 [__init__.py:106] Checking if ROCm platform is available. DEBUG 08-29 04:29:54 [__init__.py:120] ROCm platform is not available because: No module named 'amdsmi' DEBUG 08-29 04:29:54 [__init__.py:127] Checking if XPU platform is available. DEBUG 08-29 04:29:54 [__init__.py:146] XPU platform is not available because: No module named 'intel_extension_for_pytorch' DEBUG 08-29 04:29:54 [__init__.py:1...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: No platform detected, vLLM is running on UnspecifiedPlatform in Docker with Kubernetes, Nvidia L4 bug;stale ### Your current environment ### 🐛 Describe the bug I'm trying to deploy multiple models in GKE using do...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: multiple models in GKE using docker images version > 0.8.5 (like mistral-small-3.2 and gptoss-20b) and I get the following error: ```text DEBUG 08-29 04:29:54 [__init__.py:30] No plugins for group vllm.platform_plugins...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;crash;nan_inf env_dependency #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag Your current enviro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nt environment ### 🐛 Describe the bug I'm trying to deploy multiple models in GKE using docker images version > 0.8.5 (like mistral-small-3.2 and gptoss-20b) and I get the following error: ```text DEBUG 08-29 04:29:54 [...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: running on UnspecifiedPlatform in Docker with Kubernetes, Nvidia L4 bug;stale ### Your current environment ### 🐛 Describe the bug I'm trying to deploy multiple models in GKE using docker images version > 0.8.5 (like mis...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | etection analysis: #23943: Should have ROCm label: NO (0 matches) #23935: Should have ROCm label: NO (0 matches) #23934: Should have ROCm label: NO (0 matches) #23926: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
