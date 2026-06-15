# vllm-project/vllm#4385: [Bug]: vllm 0.4.1 and transformers 4.40.1 have conflicting dependencies on pydantic

| 字段 | 值 |
| --- | --- |
| Issue | [#4385](https://github.com/vllm-project/vllm/issues/4385) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.4.1 and transformers 4.40.1 have conflicting dependencies on pydantic

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC) 10.2.1 20210130 (Red Hat 10.2.1-11) Clang version: Could not collect CMake version: version 3.28.3 Libc version: glibc-2.33 Python version: 3.8.18 (default, Sep 11 2023, 13:40:15) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.9.151-015.ali3000.alios7.x86_64-x86_64-with-glibc2.17 Is CUDA available: N/A CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB Nvidia driver version: 470.82.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Thread(s) per core: 2 Core(s) per socket: 32 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 106 Model name: Intel(R) Xeon(R) Platinum 8369B CPU @ 2.90GHz Stepping: 6 CPU MHz: 3499.859 CP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: vllm 0.4.1 and transformers 4.40.1 have conflicting dependencies on pydantic installation ### Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: ntic installation ### Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: (look up to see its traceback): If you use `@root_validator` with pre=False (the default) you MUST specify `skip_on_failure=True`. Note that `@root_validator` is deprecated and should be replaced with `@model_validator`...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e the bug ```python from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest llm = LLM(model="/mnt/ismartservice/Llama-2-7b-hf", enable_lora=True) ``` error information: RuntimeError: Failed to imp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
