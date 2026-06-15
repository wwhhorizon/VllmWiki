# vllm-project/vllm#8655: [Bug]: [Usage]: is_xpu should return true when the torch.xpu.is_available is true even w/o IPEX

| 字段 | 值 |
| --- | --- |
| Issue | [#8655](https://github.com/vllm-project/vllm/issues/8655) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Usage]: is_xpu should return true when the torch.xpu.is_available is true even w/o IPEX

### Issue 正文摘录

### Your current environment Collecting environment information... /home/sdp/miniforge3/envs/liangan1/lib/python3.10/site-packages/transformers/utils/hub.py:128: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and will be removed in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( WARNING 09-20 00:31:48 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.5.0a0+git136e28f Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 20.0.0 (++20240812042341+3176f255c9dd-1~exp1~20240812162447.1861) CMake version: version 3.30.3 Libc version: glibc-2.35 Python version: 3.10.14 | packaged by conda-forge | (main, Mar 20 2024, 12:45:18) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.15.0-121-generic-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: Tr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ad. warnings.warn( WARNING 09-20 00:31:48 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.5.0a0+git136e28f Is debug build: False CUDA used to bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ed 'vllm._C'") PyTorch version: 2.5.0a0+git136e28f Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: /o IPEX bug;stale ### Your current environment Collecting environment information... /home/sdp/miniforge3/envs/liangan1/lib/python3.10/site-packages/transformers/utils/hub.py:128: FutureWarning: Using `TRANSFORMERS_CACH...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ld return true when the torch.xpu.is_available is true even w/o IPEX bug;stale ### Your current environment Collecting environment information... /home/sdp/miniforge3/envs/liangan1/lib/python3.10/site-packages/transform...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ant libraries: [pip3] numpy==1.26.4 [pip3] optree==0.12.1 [pip3] pytorch-triton-xpu==3.0.0+cc981feba1 [pip3] pyzmq==26.2.0 [pip3] torch==2.5.0a0+git136e28f [pip3] torchao==0.5.0 [pip3] transformers==4.45.0.dev0 [pip3] z...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
