# vllm-project/vllm#11623: [Installation]: Request to include vllm==0.6.3.post1 for cuda 11.8

| 字段 | 值 |
| --- | --- |
| Issue | [#11623](https://github.com/vllm-project/vllm/issues/11623) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Request to include vllm==0.6.3.post1 for cuda 11.8

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` WARNING 12-30 17:06:52 _custom_ops.py:19] Failed to import from vllm._C with ImportError('/usr/local/app/.local/lib/python3.8/site-packages/vllm/_C.abi3.so: undefined symbol: cuTensorMapEncodeTiled') Collecting environment information... /usr/local/lib64/python3.8/site-packages/torch/cuda/__init__.py:128: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 11040). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx Alternatively, go to: https://pytorch.org to install a PyTorch version that has been compiled with your version of the CUDA driver. (Triggered internally at ../c10/cuda/CUDAFunctions.cpp:108.) return torch._C._cuda_getDeviceCount() > 0 PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: TencentOS Linux 3.1 (Core) (x86_64) GCC version: (GCC) 8.4.1 20200928 (Red Hat 8.4.1-1) Clang version: 8.0.1 (Red Hat 8.0.1-1.module_el8.1.0+215+a01033fb) CMake version: version 3.18.2 Libc version: glibc-2.28 Python version:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: Request to include vllm==0.6.3.post1 for cuda 11.8 installation ### Your current environment ```text The output of `python collect_env.py` ``` WARNING 12-30 17:06:52 _custom_ops.py:19] Failed to import fr
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Installation]: Request to include vllm==0.6.3.post1 for cuda 11.8 installation ### Your current environment ```text The output of `python collect_env.py` ``` WARNING 12-30 17:06:52 _custom_ops.py:19] Failed to import f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: .so: undefined symbol: cuTensorMapEncodeTiled') Collecting environment information... /usr/local/lib64/python3.8/site-packages/torch/cuda/__init__.py:128: UserWarning: CUDA initialization: The NVIDIA driver on your syst...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.46.3 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.3.post1 vLLM Build Flags: CUDA A...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cuda_getDeviceCount() > 0 PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: TencentOS Linux 3.1 (Core) (x86_64) GCC version: (GCC) 8.4.1 20200928 (Re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
