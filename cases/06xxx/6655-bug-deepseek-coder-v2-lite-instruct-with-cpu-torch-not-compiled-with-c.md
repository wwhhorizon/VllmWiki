# vllm-project/vllm#6655: [Bug]: DeepSeek-Coder-V2-Lite-Instruct with CPU : Torch not compiled with CUDA enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#6655](https://github.com/vllm-project/vllm/issues/6655) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-Coder-V2-Lite-Instruct with CPU : Torch not compiled with CUDA enabled

### Issue 正文摘录

### Your current environment ```test python collect_env.py Collecting environment information... WARNING 07-22 17:54:45 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-1022-aws-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 4 On-line CPU(s) list: 0-3 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Platinum 8259CL CPU @ 2.50GHz CPU family: 6 Model: 85 Thread(s) per...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: DeepSeek-Coder-V2-Lite-Instruct with CPU : Torch not compiled with CUDA enabled bug ### Your current environment ```test python collect_env.py Collecting environment information... WARNING 07-22 17:54:45 _custom_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: n Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Vulnerable Vulnerability Spec rstack overflo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: Bug]: DeepSeek-Coder-V2-Lite-Instruct with CPU : Torch not compiled with CUDA enabled bug ### Your current environment ```test python collect_env.py Collecting environment information... WARNING 07-22 17:54:45 _custom_o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rent environment ```test python collect_env.py Collecting environment information... WARNING 07-22 17:54:45 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: .1+cpu [pip3] torchvision==0.18.1+cpu [pip3] transformers==4.42.4 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.2 vLLM Build Flags: CUDA Archs:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
