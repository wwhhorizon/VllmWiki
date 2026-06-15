# vllm-project/vllm#177: Container Build Fail - Cannot find CUDA at CUDA_HOME

| 字段 | 值 |
| --- | --- |
| Issue | [#177](https://github.com/vllm-project/vllm/issues/177) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
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

> Container Build Fail - Cannot find CUDA at CUDA_HOME

### Issue 正文摘录

Whatever I try, I get: ``` RuntimeError: Cannot find CUDA at CUDA_HOME: /usr/local/cuda. CUDA must be available in order to build the package. ---------------------------------------- WARNING: Discarding https://files.pythonhosted.org/packages/39/a1/42e126432a166dcca8d93c430a5c733b1734f4e0f7ffbaf7cbbdb22662a1/vllm-0.1.0.tar.gz#sha256=14425335ac80b17d60a1633f03c5d05d2c6b46a06b196eccab900e2150d96c79 (from https://pypi.org/simple/vllm/) (requires-python:>=3.8). Command errored out with exit status 1: /usr/bin/python /usr/local/lib/python3.8/dist-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /tmp/tmp6ex7hkl2 Check the logs for full command output. ``` **Dockerfile:** ``` FROM nvcr.io/nvidia/pytorch:22.12-py3 WORKDIR /app RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl RUN apt-get install unzip RUN apt-get -y install python3 wget RUN apt-get -y install python3-pip RUN pip uninstall -y torch RUN pip install vllm ``` I also tried with FROM nvcr.io/nvidia/cuda:11.8.0-runtime-ubuntu20.04

## 现有链接修复摘要

#282 [Setup] Check CUDA_HOME instead of cuda.is_available() in setup.py | #36529 [Compile] Fix compile warning in `moe_permute` | #38573 [Compile] Fix nvfp4 compile warning

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Container Build Fail - Cannot find CUDA at CUDA_HOME installation Whatever I try, I get: ``` RuntimeError: Cannot find CUDA at CUDA_HOME: /usr/local/cuda. CUDA must be available in order to build the package. ----------...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 29 [Compile] Fix compile warning in `moe_permute` | #38573 [Compile] Fix nvfp4 compile warning Whatever I try, I get:
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: da.is_available() in setup.py | #36529 [Compile] Fix compile warning in `moe_permute` | #38573 [Compile] Fix nvfp4 compile warning Whatever I try, I get:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Container Build Fail - Cannot find CUDA at CUDA_HOME installation Whatever I try, I get: ``` RuntimeError: Cannot find CUDA at CUDA_HOME: /usr/local/cuda. CUDA must be available in order to build the package. ----------...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#282](https://github.com/vllm-project/vllm/pull/282) | mentioned | 0.6 | [Setup] Check CUDA_HOME instead of cuda.is_available() in setup.py | CUDA_HOME instead of cuda.is_available() in setup.py This is to solve #177 The issue is when building a docker image, `torch.cuda.is_available()` always shows False even `CUDA_HOM… |
| [#36529](https://github.com/vllm-project/vllm/pull/36529) | mentioned | 0.6 | [Compile] Fix compile warning in `moe_permute` | rmute_unpermute_kernels/moe_permute_unpermute_kernel.inl(19): warning #177-D: variable "expert_id" was declared but never referenced int expert_id = sorted_experts[expanded_dest_ro |
| [#38573](https://github.com/vllm-project/vllm/pull/38573) | mentioned | 0.6 | [Compile] Fix nvfp4 compile warning | 6/vllm-source/csrc/quantization/fp4/nvfp4_quant_entry.cu(57): warning #177-D: function "nvfp4_quant_sm_supported" was declared but never referenced static bool nvfp4_quant_sm_supp… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
