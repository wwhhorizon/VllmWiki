# vllm-project/vllm#6225: [Bug]:  benchmark_throughput gets TypeError: XFormersMetadata.__init__() got an unexpected keyword argument 'is_prompt' wit CPU 

| 字段 | 值 |
| --- | --- |
| Issue | [#6225](https://github.com/vllm-project/vllm/issues/6225) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  benchmark_throughput gets TypeError: XFormersMetadata.__init__() got an unexpected keyword argument 'is_prompt' wit CPU 

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-91-generic-x86_64-with-glibc2.35 ... [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] torchvision==0.18.0 [pip3] transformers==4.42.3 [pip3] triton==2.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0 pypi_0 pypi [conda] torchvision 0.18.0 pypi_0 pypi [conda] transformers 4.42.3 pypi_0 pypi [conda] triton 2.3.0 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled ``` ### 🐛 Describe the bug Running `benchmark_throughput.py ... --device cpu` throws an exception, it works with GPU. ``` VLLM_CPU_KVCACHE_SPACE=16 time python benchmarks/benchmark_throughput.py --model mosa...

## 现有链接修复摘要

#7807 [Bugfix] Catch up with removed parameter 'is_prompt' in cpu/xpu model runner

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: prompt' wit CPU bug;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC vers...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: rch==2.3.0 [pip3] torchvision==0.18.0 [pip3] transformers==4.42.3 [pip3] triton==2.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: benchmark_throughput gets TypeError: XFormersMetadata.__init__() got an unexpected keyword argument 'is_prompt' wit CPU bug;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 128 --output-len 512 --trust-remote-code --backend=vllm --device cpu --dtype bfloat16 ... WARNING 07-08 21:21:47 cpu_executor.py:119] CUDA graph is not supported on CPU, fallback to the eager mode. INFO 07-08 21:21:48 s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: benchmark_throughput gets TypeError: XFormersMetadata.__init__() got an unexpected keyword argument 'is_prompt' wit CPU bug;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build:...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7807](https://github.com/vllm-project/vllm/pull/7807) | closes_keyword | 0.95 | [Bugfix] Catch up with removed parameter 'is_prompt' in cpu/xpu model runner | FIX #6225 I've encountered the same issue above. There might be refactoring issue from #4681. There is no longer exists a parameter 'is_prompt' in AttentionMetadata class. Look |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
