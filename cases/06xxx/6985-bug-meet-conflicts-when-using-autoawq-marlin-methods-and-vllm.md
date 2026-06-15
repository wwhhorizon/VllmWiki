# vllm-project/vllm#6985: [Bug]: Meet conflicts when using AutoAWQ marlin methods and vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#6985](https://github.com/vllm-project/vllm/issues/6985) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Meet conflicts when using AutoAWQ marlin methods and vLLM

### Issue 正文摘录

### Your current environment yTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A Python version: 3.11.6 (main, Jun 19 2024, 15:40:26) (64-bit runtime) Python platform: Linux-5.4.241-1-tlinux4-0017.1-x86_64-with-glibc2.38 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10 Nvidia driver version: 545.23.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 56 On-line CPU(s) list: 0-55 Vendor ID: AuthenticAMD Model name: AMD EPYC 7K83 64-Core Processor CPU family: 25 Model: 1 Thread(s) per core: 2 Core(s) per socket: 28 Socket(s): 1 Stepping: 0 BogoMIPS: 5090.43 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm rep_good nopl cpuid extd_apicid amd_dcm tsc_known_freq pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: AutoAWQ marlin methods and vLLM bug ### Your current environment yTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A Python version: 3.11.6 (main, Jun 19 20...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: r current environment yTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A Python version: 3.11.6 (main, Jun 19 2024, 15:40:26) (64-bit runtime) Python platf...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10 Nvidia driver version: 545.23.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runti...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: layers/quantization/utils/marlin_utils.py#L87-L91 My scripts using vLLM benchmark is: ```bash python3 vllm/benchmarks/benchmark_throughput.py --model {awq_marlin_path} --quantization awq_marlin --input-len 4096 --output...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.3.1 [pip3] torchvision==0.18.1 [pip3] transformers==4.42.4 [pip3] triton==2.3.1 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.3.post1 vLLM Build Flags: CUDA A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
