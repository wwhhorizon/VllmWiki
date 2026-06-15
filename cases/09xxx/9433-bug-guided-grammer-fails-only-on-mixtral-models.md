# vllm-project/vllm#9433: [Bug]: guided_grammer fails only on Mixtral models

| 字段 | 值 |
| --- | --- |
| Issue | [#9433](https://github.com/vllm-project/vllm/issues/9433) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: guided_grammer fails only on Mixtral models

### Issue 正文摘录

### Your current environment ``` Collecting environment information... WARNING 10-16 15:01:13 cuda.py:76] Detected different devices in the system: WARNING 10-16 15:01:13 cuda.py:76] NVIDIA A100-SXM4-80GB WARNING 10-16 15:01:13 cuda.py:76] NVIDIA A100-SXM4-80GB WARNING 10-16 15:01:13 cuda.py:76] NVIDIA A100-SXM4-80GB WARNING 10-16 15:01:13 cuda.py:76] NVIDIA DGX Display WARNING 10-16 15:01:13 cuda.py:76] NVIDIA A100-SXM4-80GB WARNING 10-16 15:01:13 cuda.py:76] Please make sure to set `CUDA_DEVICE_ORDER=PCI_BUS_ID` to avoid unexpected behavior. /home/emehtabuddin/.local/lib/python3.8/site-packages/vllm/connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.16.3 Libc version: glibc-2.31 Python version: 3.8.10 (default, Mar 25 2024, 10:42:49) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-5.4.0-187-generic-x86_64-with-glibc2.29 Is CUDA...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: G 10-16 15:01:13 cuda.py:76] Please make sure to set `CUDA_DEVICE_ORDER=PCI_BUS_ID` to avoid unexpected behavior. /home/emehtabuddin/.local/lib/python3.8/site-packages/vllm/connections.py:8: RuntimeWarning: Failed to re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: nment ``` Collecting environment information... WARNING 10-16 15:01:13 cuda.py:76] Detected different devices in the system: WARNING 10-16 15:01:13 cuda.py:76] NVIDIA A100-SXM4-80GB WARNING 10-16 15:01:13 cuda.py:76] NV...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: guided_grammer fails only on Mixtral models bug;stale ### Your current environment ``` Collecting environment information... WARNING 10-16 15:01:13 cuda.py:76] Detected different devices in the system: WARNING 10...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: guided_grammer fails only on Mixtral models bug;stale ### Your current environment ``` Collecting environment information... WARNING 10-16 15:01:13 cuda.py:76] Detected different devices in the system: WARNING 10...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.45.2 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A (dev) vLLM Build Flags: CUDA Arc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
