# vllm-project/vllm#12734: [Installation]: Can't build arm container image with podman without a SELinux relabel of bind mounts

| 字段 | 值 |
| --- | --- |
| Issue | [#12734](https://github.com/vllm-project/vllm/issues/12734) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Can't build arm container image with podman without a SELinux relabel of bind mounts

### Issue 正文摘录

### Your current environment ```text INFO 02-04 09:52:35 __init__.py:186] Automatically detected platform cpu. Collecting environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 15.3 (arm64) GCC version: Could not collect Clang version: 16.0.0 (clang-1600.0.26.6) CMake version: version 3.31.5 Libc version: N/A Python version: 3.12.8 (main, Dec 3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)] (64-bit runtime) Python platform: macOS-15.3-arm64-arm-64bit Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Apple M3 Pro Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] pyzmq==26.2.1 [pip3] torch==2.5.1 [pip3] torchaudio==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.48.2 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.1.dev4414+g73b35cc (git sha: 73b35cc vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: Can't build arm container image with podman without a SELinux relabel of bind mounts installation;stale ### Your current environment ```text INFO 02-04 09:52:35 __init__.py:186] Automatically detected pla
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 15.3 (arm64) GCC version: Could not collect Clang version: 16.0.0 (clang...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: __.py:186] Automatically detected platform cpu. Collecting environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 15.3 (arm64)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: image with podman without a SELinux relabel of bind mounts installation;stale ### Your current environment ```text INFO 02-04 09:52:35 __init__.py:186] Automatically detected platform cpu. Collecting environment informa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Dockerfile using the [Apple silicon CPU docs](https://docs.vllm.ai/en/latest/getting_started/installation/cpu/index.html?device=apple): ``` $ podman build -f Dockerfile.arm -t vllm-cpu-env --shm-size=4g . [1/2] STEP 1/1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
