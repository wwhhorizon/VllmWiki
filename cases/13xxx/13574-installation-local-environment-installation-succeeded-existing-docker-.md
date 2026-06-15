# vllm-project/vllm#13574: [Installation]: Local environment installation succeeded, Existing docker environment failed log

| 字段 | 值 |
| --- | --- |
| Issue | [#13574](https://github.com/vllm-project/vllm/issues/13574) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Local environment installation succeeded, Existing docker environment failed log

### Issue 正文摘录

### Your current environment **Local environment:** - System: Ubuntu 22.04 - CUDA: 12.4 - PyTorch: 2.4.0 - CMake: 2.31.4 - GCC: 11.4.0 **Docker environment:** - System: Ubuntu 24.04 - CUDA: 12.6 - PyTorch: 2.6.0 - CMake: 2.31.4 - GCC: 13.3.0 ### How you are installing vllm Code version: 2025.2.19, main branch Local environment: - System: Ubuntu 22.04 - CUDA: 12.4 - PyTorch: 2.4.0 - CMake: 2.31.4 - GCC: 11.4.0 Compiled and installed successfully using the documentation. However, errors occurred when attempting to install in the Docker environment: **Docker environment:** - System: Ubuntu 24.04 - CUDA: 12.6 - PyTorch: 2.6.0 - CMake: 2.31.4 - GCC: 13.3.0 ### Issues from the Docker environment: 1. Issue: Configured the `nvcc` environment variable, but the folder `/usr/local/cuda-12.6/bin/nvcc` was not found. Solution: Edit `~/.bash_profile` or `~/.bashrc` Modify the configuration to: ```bash export PATH=/usr/local/cuda/bin${PATH:+:${PATH}} ``` Change `cuda-12.6` to just `cuda`. 2. Issue: `subprocess.CalledProcessError: Command '['cmake', '--build', '.', '-j=40', '--target=_moe_C', '--target=_C']' returned non-zero exit status 1` – CMake compilation error. Solution: Tried other methods...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: Local environment installation succeeded, Existing docker environment failed log installation ### Your current environment **Local environment:** - System: Ubuntu 22.04 - CUDA: 12.4 - PyTorch: 2.4.0
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r current environment **Local environment:** - System: Ubuntu 22.04 - CUDA: 12.4 - PyTorch: 2.4.0 - CMake: 2.31.4 - GCC: 11.4.0 **Docker environment:** - System: Ubuntu 24.04 - CUDA: 12.6 - PyTorch: 2.6.0 - CMake: 2.31....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ocal/cuda-12.6/bin/nvcc` was not found. Solution: Edit `~/.bash_profile` or `~/.bashrc` Modify the configuration to: ```bash export PATH=/usr/local/cuda/bin${PATH:+:${PATH}} ``` Change `cuda-12.6` to just `cuda`. 2. Iss...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 1.4 - GCC: 13.3.0 ### Issues from the Docker environment: 1. Issue: Configured the `nvcc` environment variable, but the folder `/usr/local/cuda-12.6/bin/nvcc` was not found. Solution: Edit `~/.bash_profile` or `~/.bashr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: lledProcessError: Command '['cmake', '--build', '.', '-j=40', '--target=_moe_C', '--target=_C']' returned non-zero exit status 1` – CMake compilation error. Solution: Tried other methods, but unable to resolve the issue...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
