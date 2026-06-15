# vllm-project/vllm#25464: [Usage]: The added API server endpoint is not working.

| 字段 | 值 |
| --- | --- |
| Issue | [#25464](https://github.com/vllm-project/vllm/issues/25464) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: The added API server endpoint is not working.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ============================== System Info ============================== OS : Microsoft Windows 11 Education GCC version : Could not collect Clang version : Could not collect CMake version : Could not collect Libc version : N/A ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cpu Is debug build : False CUDA used to build PyTorch : Could not collect ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] (64-bit runtime) Python platform : Windows-11-10.0.26100-SP0 ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : N/A GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 Nvidia driver version : 581.08 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info =================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ====== OS : Microsoft Windows 11 Education GCC version : Could not collect Clang version : Could not collect CMake version : Could not collect Libc version : N/A ============================== PyT
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ch version : 2.8.0+cpu Is debug build : False CUDA used to build PyTorch : Could not collect ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python versi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rsion : Could not collect CUDA_MODULE_LOADING set to : N/A GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 Nvidia driver version : 581.08 cuDNN version : Could not collect HIP runtime version : N/A MIOpen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: de below is the new endpoint that i added under [get_server_load_metrics(request:Request)]( #[url](https://github.com/vllm-project/vllm/blob/c98be0a232764fb68353e2c9e26d3495a979044d/vllm/entrypoints/openai/api_server.py...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: point to be accessible and to be listed in the /docs page. ### Steps to Reproduce 1. cloned the official vLLM GitHub repository. 2. modified the vllm/vllm/entrypoints/openai/api_server.py file to add a new APIRouter pat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
