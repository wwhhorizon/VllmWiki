# vllm-project/vllm#6219: [Bug]: VllmWorkerProcess does not exit correctly when TP > 1 

| 字段 | 值 |
| --- | --- |
| Issue | [#6219](https://github.com/vllm-project/vllm/issues/6219) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VllmWorkerProcess does not exit correctly when TP > 1 

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-1055-nvidia-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.5.40 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version: 555.42.02 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.2.0 /usr/lib/x86_64-linux-gnu/l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: tly when TP > 1 bug;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 12.5.40 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 5_10 NIC11: mlx5_11 ``` ### 🐛 Describe the bug Reproduce: ``` python benchmarks/benchmark_latency.py \ --model meta-llama/Llama-2-70b-chat-hf \ --tensor-parallel-size 8 \ --batch-size 1 ``` Error message: ``` Warmup ite...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: x async abort: Not affected Versions of relevant libraries: [pip3] flashinfer==0.0.8+cu121torch2.3 [pip3] mypy==1.9.0 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] onnx==1.14....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
