# vllm-project/vllm#1070: Can't build vLLM from Docker due to AWQ's minimum architecture requirements - TORCH_CUDA_ARCH_LIST does not help

| 字段 | 值 |
| --- | --- |
| Issue | [#1070](https://github.com/vllm-project/vllm/issues/1070) |
| 状态 | closed |
| 标签 |  |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Can't build vLLM from Docker due to AWQ's minimum architecture requirements - TORCH_CUDA_ARCH_LIST does not help

### Issue 正文摘录

@casper-hansen @WoosukKwon I'm trying to build a test vLLM Docker container with the latest vLLM commit. My Docker container has this: ```Dockerfile ARG CUDA_VERSION="11.8.0" ARG CUDNN_VERSION="8" ARG UBUNTU_VERSION="22.04" # Base NVidia CUDA Ubuntu image FROM nvidia/cuda:$CUDA_VERSION-cudnn$CUDNN_VERSION-devel-ubuntu$UBUNTU_VERSION AS base ENV PATH="/usr/local/cuda/bin:${PATH}" ENV TORCH_CUDA_ARCH_LIST="8.0;8.6+PTX;8.9;9.0" RUN pip3 install torch --index-url https://download.pytorch.org/whl/cu118 RUN git clone https://github.com/vllm-project/vllm && \ cd vllm && \ git checkout ff36139ffc66294c19b503c1e52dc42c2cd265f6 && \ pip3 install -r requirements.txt && \ pip3 install -e . && \ pip3 install --no-cache-dir huggingface-hub hf_transfer && \ pip3 cache purge ``` This structure worked fine to build vLLM before, and to build other servers/apps that use Torch. The line `ENV TORCH_CUDA_ARCH_LIST="8.0;8.6+PTX;8.9;9.0"` usually works fine to ensure that an app can built in a Docker even though Docker cannot see any GPU. But trying to build vLLM fails with this: ``` #11 509.5 ptxas /tmp/tmpxft_00000226_00000000-11_gemm_kernels.compute_70.ptx, line 892; error : Feature 'ldmatrix' require...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Can't build vLLM from Docker due to AWQ's minimum architecture requirements - TORCH_CUDA_ARCH_LIST does not help @casper-hansen @WoosukKwon I'm trying to build a test vLLM Docker container with the latest vLLM commit. M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Can't build vLLM from Docker due to AWQ's minimum architecture requirements - TORCH_CUDA_ARCH_LIST does not help @casper-hansen @WoosukKwon I'm trying to build a test vLLM Docker container with the latest vLLM commit. M...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ents.txt && \ pip3 install -e . && \ pip3 install --no-cache-dir huggingface-hub hf_transfer && \ pip3 cache purge ``` This structure worked fine to build vLLM before, and to build other servers/apps that use Torch. The...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: like `TORCH_CUDA_ARCH_LIST`? Thanks development ci_build;model_support;quantization cuda;quantization build_error env_dependency @casper-hansen @WoosukKwon
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ls with this: ``` #11 509.5 ptxas /tmp/tmpxft_00000226_00000000-11_gemm_kernels.compute_70.ptx, line 892; error : Feature 'ldmatrix' requires .target sm_75 or higher #11 509.5 ptxas /tmp/tmpxft_00000226_00000000-11_gemm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
