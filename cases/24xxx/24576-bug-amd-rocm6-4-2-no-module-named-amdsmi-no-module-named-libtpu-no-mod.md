# vllm-project/vllm#24576: [Bug]: AMD ROCM6.4.2 No module named 'amdsmi' No module named 'libtpu' No module named 'intel_extension_for_pytorch'

| 字段 | 值 |
| --- | --- |
| Issue | [#24576](https://github.com/vllm-project/vllm/issues/24576) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: AMD ROCM6.4.2 No module named 'amdsmi' No module named 'libtpu' No module named 'intel_extension_for_pytorch'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug $ vllm --version DEBUG 09-10 18:43:10 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 09-10 18:43:10 [__init__.py:34] Checking if TPU platform is available. DEBUG 09-10 18:43:10 [__init__.py:52] TPU platform is not available because: No module named 'libtpu' DEBUG 09-10 18:43:10 [__init__.py:58] Checking if CUDA platform is available. DEBUG 09-10 18:43:10 [__init__.py:82] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBUG 09-10 18:43:10 [__init__.py:99] CUDA platform is not available because: NVML Shared Library Not Found DEBUG 09-10 18:43:10 [__init__.py:106] Checking if ROCm platform is available. DEBUG 09-10 18:43:10 [__init__.py:120] ROCm platform is not available because: No module named 'amdsmi' DEBUG 09-10 18:43:10 [__init__.py:127] Checking if XPU platform is available. DEBUG 09-10 18:43:10 [__init__.py:146] XPU platform is not available because: No module named 'intel_extension_for_pytorch' DEBUG 09-10 18:43:10 [__init__.py:153] Checking if CPU platform is available. INFO 09-10 18:43:10 [__init__.py:220] No platform detected, vLLM is running on UnspecifiedPlatform...

## 现有链接修复摘要

#41585 [ROCm] Fix platform detection failures in unprivileged containers

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ;stale ### Your current environment ### 🐛 Describe the bug $ vllm --version DEBUG 09-10 18:43:10 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 09-10 18:43:10 [__init__.py:34] Checking if TPU p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: AMD ROCM6.4.2 No module named 'amdsmi' No module named 'libtpu' No module named 'intel_extension_for_pytorch' bug;rocm;stale ### Your current environment ### 🐛 Describe the bug $ vllm --version DEBUG 09-10 18:43:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ed on current platform. Traceback (most recent call last): File "/home/modelscope/anaconda3/bin/vllm", line 7, in sys.exit(main()) ^^^^^^ File "/home/modelscope/ai/vllm/vllm/entrypoints/cli/main.py", line 46, in main cm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: le named 'libtpu' No module named 'intel_extension_for_pytorch' bug;rocm;stale ### Your current environment ### 🐛 Describe the bug $ vllm --version DEBUG 09-10 18:43:10 [__init__.py:28] No plugins for group vllm.platfor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;crash;nan_inf env_dependency #41585 [ROCm] Fix platform detection failures in unprivileged containers Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41585](https://github.com/vllm-project/vllm/pull/41585) | mentioned | 0.6 | [ROCm] Fix platform detection failures in unprivileged containers | o warning is emitted when amdsmi fails Related issues: #40081, #24576, #34573, #39378 🤖 Generated with [Claude Code](https://claude.ai/code) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
