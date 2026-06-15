# vllm-project/vllm#5212: [Installation]: Failed to build punica

| 字段 | 值 |
| --- | --- |
| Issue | [#5212](https://github.com/vllm-project/vllm/issues/5212) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Failed to build punica

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.el7.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.7.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800 80GB PCIe GPU 1: NVIDIA A800 80GB PCIe GPU 2: NVIDIA A800 80GB PCIe GPU 3: NVIDIA A800 80GB PCIe Nvidia driver version: 515.65.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True ``` ### How you are installing vllm ```sh python3 setup.py bdist_wheel --dist-dir=dist ``` ``` FAILED: /workspace/build/lib.linux-x86_64-3.10/vllm/_punica_C.cpython-310-x86_64-linux-gnu.so : && /usr/bin/c++ -fPIC -O2 -g -DNDEBUG -shared -o /workspace/build/lib.linux-x...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: Failed to build punica installation;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.0.1+cu117 Is debug build: Fal
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: onment information... PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: n-310-x86_64-linux-gnu.so CMakeFiles/_punica_C.dir/csrc/punica/bgmv/bgmv_bf16_bf16_bf16.cu.o CMakeFiles/_punica_C.dir/csrc/punica/bgmv/bgmv_bf16_fp32_bf16.cu.o CMakeFiles/_punica_C.dir/csrc/punica/bgmv/bgmv_fp16_fp16_fp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
