# vllm-project/vllm#17273: [Usage]: How to terminate vllm completely?

| 字段 | 值 |
| --- | --- |
| Issue | [#17273](https://github.com/vllm-project/vllm/issues/17273) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to terminate vllm completely?

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 8 (x86_64) GCC version: (GCC) 10.5.0 Clang version: Could not collect CMake version: version 3.20.2 Libc version: glibc-2.29 Python version: 3.10.0 (default, Mar 3 2022, 09:58:08) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-4.18.0-348.7.1.el8_5.x86_64-x86_64-with-glibc2.29 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 GPU 2: NVIDIA RTX A6000 GPU 3: NVIDIA RTX A6000 GPU 4: NVIDIA RTX A6000 GPU 5: NVIDIA RTX A6000 GPU 6: NVIDIA RTX A6000 GPU 7: NVIDIA RTX A6000 Nvidia driver version: 550.135 cuDNN version: Probably one of the following: /usr/local/cuda-12.2/targets/x86_64-linux/lib/libcudnn.so.8.9.7 /usr/local/cuda-12.2/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.7 /usr/local/cuda-12.2/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.7 /usr/local/cuda-12.2/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.9.7 /usr/local/cuda-12.2/target...

## 现有链接修复摘要

#40935 [V1][Bugfix] Reap EngineCore on parent death (#19849)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rrent environment ```text Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 8 (x86_64) GCC version...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 8 (x86_64) GCC version: (GCC) 10.5.0 Clang version: Could not co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ly? usage ### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 8...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: torch==2.5.1 [pip3] torchaudio==2.5.1 [pip3] torchvision==0.20.1 [pip3] triton==3.1.0 [conda] gptqmodel 1.9.0+cu124torch2.5 pypi_0 pypi [conda] numpy 1.25.0 pypi_0 pypi [conda] torch 2.5.1
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 8 (x86_64) GCC version: (GCC) 10.5.0 Clang version: Could no...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40935](https://github.com/vllm-project/vllm/pull/40935) | closes_keyword | 0.95 | [V1][Bugfix] Reap EngineCore on parent death (#19849) | Closes (or makes obsolete) the user-facing pain in #19849, #17273, #1908. Complements RFC #24885 (cooperative shutdown clarification) without changing its semantics, and does not c |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
