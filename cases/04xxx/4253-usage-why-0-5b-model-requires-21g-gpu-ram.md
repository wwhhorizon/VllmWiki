# vllm-project/vllm#4253: [Usage]: Why 0.5B model requires 21G gpu ram ?

| 字段 | 值 |
| --- | --- |
| Issue | [#4253](https://github.com/vllm-project/vllm/issues/4253) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Why 0.5B model requires 21G gpu ram ?

### Issue 正文摘录

### Your current environment I fine-tuned a 0.5B model based on Qwen 0.5B. When running on vllm, it reports 21G . I wonder if I am doing anything wrong, that it is much larger than expected ? Could you give me some suggestion on how to run it in more memory efficient way? ![image](https://github.com/vllm-project/vllm/assets/16278392/05a52970-2a6a-44b4-ae7d-b316ff68f3d2) ![image](https://github.com/vllm-project/vllm/assets/16278392/d8865ea6-92ac-4314-965a-ce68b19852f3) Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.17 Python version: 3.10.9 (main, Mar 1 2023, 18:23:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 Nvidia driver version: 525.116.04 cuDNN version: Proba...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ? Could you give me some suggestion on how to run it in more memory efficient way? ![image](https://github.com/vllm-project/vllm/assets/16278392/05a52970-2a6a-44b4-ae7d-b316ff68f3d2) ![image](https://github.com/vllm-pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat 4.8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Why 0.5B model requires 21G gpu ram ? usage ### Your current environment I fine-tuned a 0.5B model based on Qwen 0.5B. When running on vllm, it reports 21G . I wonder if I am doing anything wrong, that it is mu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2 [pip3] torchaudio==2.0.2+cu118 [pip3] torchvision==0.15.2+cu118 [pip3] triton==2.1.0 [conda] blas 1.0 mkl defaults [conda] cudatoolkit 11.3.1 h2bc3f7f_2 anaconda [conda] ffmpeg 4.3
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
