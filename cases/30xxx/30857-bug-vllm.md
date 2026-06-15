# vllm-project/vllm#30857: [Bug]: 使用VLLM进行推理会卡死

| 字段 | 值 |
| --- | --- |
| Issue | [#30857](https://github.com/vllm-project/vllm/issues/30857) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: 使用VLLM进行推理会卡死

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.0.3 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.4.250-5-velinux1-amd64-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version : 535.161.08 cuDNN version : Could no...

## 现有链接修复摘要

#16384 [CI][Bugfix] Pin triton version for CPU

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.0.3 Libc version : glibc-2.35 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: untime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Unknown: No mitigations Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: OMPILE_THREADS=1 CUDA_MODULE_LOADING=LAZY ### 🐛 Describe the bug 这是在VLMEvalKit中的一段代码， 我在以下两个地方设置了use_vllm 分别是： config.py: "xx": partial( Qwen2VLChat, model_path="xx", min_pixels=256 * 28 * 28, max_pixels=8192*28*28, #16...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#16384](https://github.com/vllm-project/vllm/pull/16384) | mentioned | 0.45 | [CI][Bugfix] Pin triton version for CPU | xx", min_pixels=256 * 28 * 28, max_pixels=8192*28*28, #16384 * 28 * 28, # use_custom_prompt=false system_prompt=r"you are a helpful multimodal assistant. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
