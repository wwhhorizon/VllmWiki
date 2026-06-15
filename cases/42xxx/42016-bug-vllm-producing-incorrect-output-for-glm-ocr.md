# vllm-project/vllm#42016: [Bug]: vLLM producing incorrect output for GLM-OCR

| 字段 | 值 |
| --- | --- |
| Issue | [#42016](https://github.com/vllm-project/vllm/issues/42016) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM producing incorrect output for GLM-OCR

### Issue 正文摘录

### Your current environment AMD MI300 env: Collecting environment information... ``` ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : 22.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.2.1 26084 f58b06dce1f9c15707c5f808fd002e18c2accf7e) CMake version : version 3.31.10 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+git8514f05 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 7.2.53211 XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-176-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : (gfx942:sramecc+:xnack-) Nvidia driver version : Could not collect cuDNN version : Coul...

## 现有链接修复摘要

#42765 [Bugfix] _triton_mrope_forward: support GPT-J-style rotation (#42016)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: vLLM producing incorrect output for GLM-OCR bug;rocm ### Your current environment AMD MI300 env: Collecting environment information... ``` ============================== System Info ==============================...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: vLLM producing incorrect output for GLM-OCR bug;rocm ### Your current environment AMD MI300 env: Collecting environment information... ``` ============================== System Info ==============================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: cm ### Your current environment AMD MI300 env: Collecting environment information... ``` ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected V...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: en='St')} ``` where vLLM is producing even worse output on the h100. To reproduce: `pytest -sv models/multimodal/generation/test_common.py::test_multi_image_models[glm_ocr-test_case103]` This also produces gibberish whe...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42765](https://github.com/vllm-project/vllm/pull/42765) | closes_keyword | 0.95 | [Bugfix] _triton_mrope_forward: support GPT-J-style rotation (#42016) | Fixes #42016: GLM-OCR and GLM-4.1V produce incorrect output on image inputs (text-only generation is unaffected). `MRotaryEmbedding.forward_cuda` dispatches every 2-D mrope posi |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
