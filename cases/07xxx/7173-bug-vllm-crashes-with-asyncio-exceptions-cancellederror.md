# vllm-project/vllm#7173: [Bug]: Vllm crashes with asyncio.exceptions.CancelledError

| 字段 | 值 |
| --- | --- |
| Issue | [#7173](https://github.com/vllm-project/vllm/issues/7173) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Vllm crashes with asyncio.exceptions.CancelledError

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 08-05 21:59:09 _custom_ops.py:15] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /opt/dlami/nvme/vllm/vllm/connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm.commit_id' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-1023-aws-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB GPU 4: NVIDIA A100-SXM4-40GB GPU 5: NVIDIA A100-SXM4-40GB GPU 6: NVIDIA A100-SXM4-40GB GPU 7: NVIDIA A100-SXM4-40GB Nvidia driver version: 535.183.01 cuDNN ver...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Vllm crashes with asyncio.exceptions.CancelledError bug;stale ### Your current environment ```text Collecting environment information... WARNING 08-05 21:59:09 _custom_ops.py:15] Failed to import from vllm._C wit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ion__ as VLLM_VERSION PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: bug;stale ### Your current environment ```text Collecting environment information... WARNING 08-05 21:59:09 _custom_ops.py:15] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /opt/dla...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: rch==2.3.1 [pip3] torchvision==0.18.1 [pip3] transformers==4.43.3 [pip3] triton==2.3.1 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.4 vLLM Build Flags: CUDA Archs:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Vllm crashes with asyncio.exceptions.CancelledError bug;stale ### Your current environment ```text Collecting environment information... WARNING 08-05 21:59:09 _custom_ops.py:15] Failed to import from vllm._C wit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
