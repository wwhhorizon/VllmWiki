# vllm-project/vllm#9986: [Bug]: Deploying glm4 reported an error："auto" tool choice requires --enable-auto-tool-choice and --tool-call-parser to be set

| 字段 | 值 |
| --- | --- |
| Issue | [#9986](https://github.com/vllm-project/vllm/issues/9986) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deploying glm4 reported an error："auto" tool choice requires --enable-auto-tool-choice and --tool-call-parser to be set

### Issue 正文摘录

### Your current environment Collecting environment information... WARNING 11-04 15:56:19 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /home/shn/Desktop/vllm/vllm/connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang version: Could not collect CMake version: version 3.30.2 Libc version: glibc-2.39 Python version: 3.9.19 (main, May 6 2024, 19:43:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-48-generic-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 2080 Ti Nvidia driver version: 550.127.05 cuDNN version: Probably one of the following: /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn.so.8 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-12.1/targets/x86_6...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: nment information... WARNING 11-04 15:56:19 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /home/shn/Desktop/vllm/vllm/connections.py:8: RuntimeWarning: Failed to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ion__ as VLLM_VERSION PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Cla...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ser to be set bug ### Your current environment Collecting environment information... WARNING 11-04 15:56:19 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /home/sh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Mitigation; Clear Register File Vulnerability Retbleed: Not affected Vulnerability Spec rstack ov...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.45.2 [pip3] triton==3.0.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.1.105

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
