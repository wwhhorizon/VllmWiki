# vllm-project/vllm#6217: [Bug]: issue with Phi3 mini GPTQ 4Bit/8Bit

| 字段 | 值 |
| --- | --- |
| Issue | [#6217](https://github.com/vllm-project/vllm/issues/6217) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: issue with Phi3 mini GPTQ 4Bit/8Bit

### Issue 正文摘录

### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: (GCC) 7.3.1 20180712 (Red Hat 7.3.1-17) Clang version: Could not collect CMake version: version 3.29.0 Libc version: glibc-2.26 Python version: 3.10.8 | packaged by conda-forge | (main, Nov 22 2022, 08:23:14) [GCC 10.4.0] (64-bit runtime) Python platform: Linux-5.10.215-203.850.amzn2.x86_64-x86_64-with-glibc2.26 Is CUDA available: N/A CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA L4 Nvidia driver version: 535.161.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 4 On-line CPU(s) list: 0-3 Thread(s) per core: 2 Core(s) per socket: 2 Socket(s): 1 NUMA node(s): 1 Vendor ID: AuthenticAMD CPU family: 25 Model: 1 Model name: AMD EPYC 7R13 Processor Stepping: 1 CPU MHz: 3655.646 BogoMIPS: 5300.00 Hypervisor vendor: KVM Virtualization type: full L1d cache: 32K L1i cache: 32K L2 cache: 512K L3 cac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: i3 mini GPTQ 4Bit/8Bit bug ### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: (GCC) 7.3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ection traversing a bonded set of # NVLinks ``` ### 🐛 Describe the bug quantization of Phi3 mini as 4Bit or 8Bit, but none of them worked with vllm 0.5.1 ```python from transformers import AutoModelForCausalLM, AutoToke...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ur current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: (GCC) 7.3.1 20180712 (Red Hat 7.3.1-17) Cl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: : N/A CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA L4 Nvidia driver version: 535.161.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 150 engine_args, usage_context=UsageContext.LLM_CLASS) 151 self.request_counter = Counter() File ~/anaconda3/envs/pytorch_p310/lib/python3.10/site-packages/vllm/engine/llm_engine.py:414, in LLMEngine.from_engine_args(cl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
