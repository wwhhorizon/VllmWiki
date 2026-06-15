# vllm-project/vllm#5853: [Bug]: server error when hosting TheBloke/Llama-2-7B-Chat-GPTQ  with chunked-prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#5853](https://github.com/vllm-project/vllm/issues/5853) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: server error when hosting TheBloke/Llama-2-7B-Chat-GPTQ  with chunked-prefill

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8.8 (Ootpa) (x86_64) GCC version: (Spack GCC) 11.4.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.28 Python version: 3.9.19 (main, May 6 2024, 19:43:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-477.55.1.el8_8.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB Nvidia driver version: 535.161.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 64 On-line CPU(s) list: 0-63 Thread(s) per core: 1 Core(s) per socket: 64 Socket(s): 1 NUMA node(s): 4 Vendor ID: AuthenticAMD CPU family: 25 Model: 1 Model name: AMD EPYC 7763 64-Core Processor Stepping: 1 CPU MHz: 2445.518 BogoMIPS: 4891.03 Virtu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: python collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8.8 (Ootpa) (x86_64) GCC version: (Spack GCC...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: server error when hosting TheBloke/Llama-2-7B-Chat-GPTQ with chunked-prefill bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: l TheBloke/Llama-2-7B-Chat-GPTQ --seed 0 --enable-chunked-prefill python benchmarks/benchmark_serving.py --model TheBloke/Llama-2-7B-Chat-GPTQ --dataset-path /u/yao1/ShareGPT_V3_unfiltered_cleaned_split.json --request-r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ]: server error when hosting TheBloke/Llama-2-7B-Chat-GPTQ with chunked-prefill bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch vers...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
