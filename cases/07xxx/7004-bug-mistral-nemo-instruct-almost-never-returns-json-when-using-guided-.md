# vllm-project/vllm#7004: [Bug]: Mistral Nemo Instruct almost never returns JSON when using `guided_json`

| 字段 | 值 |
| --- | --- |
| Issue | [#7004](https://github.com/vllm-project/vllm/issues/7004) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral Nemo Instruct almost never returns JSON when using `guided_json`

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: (GCC) 7.3.1 20180712 (Red Hat 7.3.1-17) Clang version: Could not collect CMake version: version 3.27.7 Libc version: glibc-2.26 Python version: 3.10.9 | packaged by conda-forge | (main, Feb 2 2023, 20:20:04) [GCC 11.3.0] (64-bit runtime) Python platform: Linux-5.10.220-209.869.amzn2.x86_64-x86_64-with-glibc2.26 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 Nvidia driver version: 550.90.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 8 On-line CPU(s) list: 0-7 Thread(s) per core: 2 Core(s) per socket: 4 Socket(s): 1 NUMA node(s): 1 Vendor ID: AuthenticAMD CPU family: 25 Model: 1 Model name: AMD EPYC 7R13 Processor Stepping: 1 CPU MHz: 3634.954 BogoMIPS: 5300.00 Hypervisor v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC versio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: (GCC) 7.3.1 20180712 (Red Hat 7.3.1-17)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: using `vLLM` and `Nemo Instruct` and playing around with the new model (fp8) and even with vLLMs' `guided_json` and including the schema in prompt, nemo almost never returns a output if JSON is involved however it does...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -nccl-cu12==2.20.5 [pip3] torch==2.3.1 [pip3] torchvision==0.18.1 [pip3] triton==2.3.1 [pip3] vllm-nccl-cu12==2.18.1.0.4.0 [conda] numpy 1.26.2 pypi_0 pypi [conda] nvidia-nccl-cu11 2.14.3 pypi_0 pypi [conda] nvidia-nccl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
