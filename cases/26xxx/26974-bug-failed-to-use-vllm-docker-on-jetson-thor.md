# vllm-project/vllm#26974: [Bug]: failed to use vllm docker on jetson thor

| 字段 | 值 |
| --- | --- |
| Issue | [#26974](https://github.com/vllm-project/vllm/issues/26974) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: failed to use vllm docker on jetson thor

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug we installed nvidia docker toolkit and used docker nvcr.io/nvidia/vllm:25.09-py3 but it can't runs root@ea1f23a8480d:/workspace# export VLLM_LOGGING_LEVEL=DEBUG root@ea1f23a8480d:/workspace# vllm chat /downloads/Qwen3-30A3/ /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you. import pynvml # type: ignore[import] DEBUG 10-16 01:42:17 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 10-16 01:42:17 [__init__.py:34] Checking if TPU platform is available. DEBUG 10-16 01:42:17 [__init__.py:52] TPU platform is not available because: No module named 'libtpu' DEBUG 10-16 01:42:17 [__init__.py:58] Checking if CUDA platform is available. DEBUG 10-16 01:42:17 [__init__.py:82] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBUG 10-16 01:42:17 [__init__.py:99] CUDA platform is not available because: NVML Shared Library Not Found DEBUG 10-16 01:42:17 [__init__.py:106] Ch...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: failed to use vllm docker on jetson thor bug;stale ### Your current environment ### 🐛 Describe the bug we installed nvidia docker toolkit and used docker nvcr.io/nvidia/vllm:25.09-py3 but it can't runs root@ea1f2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: hat /downloads/Qwen3-30A3/ /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: M_LOGGING_LEVEL=DEBUG root@ea1f23a8480d:/workspace# vllm chat /downloads/Qwen3-30A3/ /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: failed to use vllm docker on jetson thor bug;stale ### Your current environment ### 🐛 Describe the bug we installed nvidia docker toolkit and used docker nvcr.io/nvidia/vllm:25.09-py3 but it can't runs root@ea1f2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;crash;import_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
