# vllm-project/vllm#36313: [Bug]: gpt-oss vllm 0.17

| 字段 | 值 |
| --- | --- |
| Issue | [#36313](https://github.com/vllm-project/vllm/issues/36313) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;gemm_linear;hardware_porting;moe;quantization |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;gemm;kernel;moe;quantization |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss vllm 0.17

### Issue 正文摘录

### Your current environment ubuntu 22.04 vllm 0.17 RTX 5090 D ### 🐛 Describe the bug ### Environment mismatch when installing `vllm==0.17` vs nightly (CUDA12 vs CUDA13) causing GPT-OSS failures on RTX 5090 I encountered a confusing issue when running **GPT-OSS models on RTX 5090 (Blackwell)** with **vLLM 0.17**. The same configuration sometimes failed with `CUBLAS_STATUS_INVALID_VALUE`, but worked when installing vLLM from the nightly index. After investigation, the root cause appears to be **different CUDA stacks depending on the installation source**. --- # 1. Installation methods produce different CUDA environments ### Installing from PyPI (stable) ```bash uv pip install vllm==0.17 ``` This installs a **CUDA 12 runtime stack**: Example packages: ``` torch 2.10.0 cuda-python 12.9.x nvidia-cublas-cu12 12.8.x nvidia-cuda-runtime-cu12 12.8.x nvidia-cudnn-cu12 9.10.x ``` This environment corresponds to: ``` CUDA 12 runtime ``` --- ### Installing from vLLM nightly index ```bash uv pip install vllm \ --torch-backend=auto \ --extra-index-url https://wheels.vllm.ai/nightly ``` This installs a **CUDA 13 runtime stack**: Example packages: ``` torch 2.10.0+cu130 cuda-python 13.0.x nvidia-...

## 现有链接修复摘要

#36381 [Doc]: Add CUDA 13.0 recommendation for GPT-OSS on Blackwell GPUs

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: m 0.17 RTX 5090 D ### 🐛 Describe the bug ### Environment mismatch when installing `vllm==0.17` vs nightly (CUDA12 vs CUDA13) causing GPT-OSS failures on RTX 5090 I encountered a confusing issue when running **GPT-OSS mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: t-oss vllm 0.17 bug ### Your current environment ubuntu 22.04 vllm 0.17 RTX 5090 D ### 🐛 Describe the bug ### Environment mismatch when installing `vllm==0.17` vs nightly (CUDA12 vs CUDA13) causing GPT-OSS failures on R...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: talling from vLLM nightly index ```bash uv pip install vllm \ --torch-backend=auto \ --extra-index-url https://wheels.vllm.ai/nightly ``` This installs a **CUDA 13 runtime stack**: Example packages: ``` torch 2.10.0+cu1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: time ``` --- # 2. Impact on GPT-OSS models GPT-OSS models rely on: * MXFP4 kernels * FlashInfer kernels * MoE routing kernels * CUTLASS GEMM paths On **RTX 5090 (Blackwell)**, the CUDA 12 stack sometimes leads to runtim...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: gpt-oss vllm 0.17 bug ### Your current environment ubuntu 22.04 vllm 0.17 RTX 5090 D ### 🐛 Describe the bug ### Environment mismatch when installing `vllm==0.17` vs nightly (CUDA12 vs CUDA13) causing GPT-OSS fail...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36381](https://github.com/vllm-project/vllm/pull/36381) | closes_keyword | 0.95 | [Doc]: Add CUDA 13.0 recommendation for GPT-OSS on Blackwell GPUs | Fixes #36313 ## Problem Users running GPT-OSS models (`openai/gpt-oss-120b`, `openai/gpt-oss-20b`) on consumer Blackwell GPUs (e.g., RTX 5090) encounter `CUBLAS_STATUS_INVALID_VA |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
