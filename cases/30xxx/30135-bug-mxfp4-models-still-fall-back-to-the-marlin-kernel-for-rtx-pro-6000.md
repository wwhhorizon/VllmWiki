# vllm-project/vllm#30135: [Bug]: MXFP4 models still fall back to the Marlin kernel for RTX PRO 6000 (Blackwell SM120)

| 字段 | 值 |
| --- | --- |
| Issue | [#30135](https://github.com/vllm-project/vllm/issues/30135) |
| 状态 | open |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MXFP4 models still fall back to the Marlin kernel for RTX PRO 6000 (Blackwell SM120)

### Issue 正文摘录

### Your current environment python collect_env.py --2025-12-05 21:50:34-- https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env.py Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.108.133, 185.199.109.133, ... Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected. HTTP request sent, awaiting response... 200 OK Length: 28050 (27K) [text/plain] Saving to: ‘collect_env.py’ collect_env.py 100%[====================================================================================================>] 27.39K --.-KB/s in 0.01s 2025-12-05 21:50:35 (2.06 MB/s) - ‘collect_env.py’ saved [28050/28050] Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A...

## 现有链接修复摘要

#33516 [Bugfix] Add SM110/SM120 device capability checks for NVFP4 MoE backends | #35568 [Bugfix] Fix SM121 (DGX Spark) exclusion from Marlin/CUTLASS FP8 paths

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: [Bug]: MXFP4 models still fall back to the Marlin kernel for RTX PRO 6000 (Blackwell SM120) bug ### Your current environment python collect_env.py --2025-12-05 21:50:34-- https://raw.githubusercontent.com/vllm-project/v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: MXFP4 models still fall back to the Marlin kernel for RTX PRO 6000 (Blackwell SM120) bug ### Your current environment python collect_env.py --2025-12-05 21:50:34-- https://raw.githubusercontent.com/vllm-project/v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: .com (raw.githubusercontent.com)|185.199.110.133|:443... connected. HTTP request sent, awaiting response... 200 OK Length: 28050 (27K) [text/plain] Saving to: ‘collect_env.py’ collect_env.py 100%[=======================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] numpy==2.1.2 [pip3] nvidia-cublas==13.0.0.19 [pip3] nvidia-cuda-cupti==13.0.48 [pip3] nvidia-cuda-nvrtc==13.0.48 [...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33516](https://github.com/vllm-project/vllm/pull/33516) | closes_keyword | 0.95 | [Bugfix] Add SM110/SM120 device capability checks for NVFP4 MoE backends | Fixes #30135 Fixes #29141 Related to #28589 |
| [#35568](https://github.com/vllm-project/vllm/pull/35568) | closes_keyword | 0.95 | [Bugfix] Fix SM121 (DGX Spark) exclusion from Marlin/CUTLASS FP8 paths | Fixes #30163. Relates to #30135. Contributed by Second Nature Computing (https://joinsecondnature.com) ## Test plan - [x] Validated on SM121a hardware (DGX Spark) - [x] Marlin F |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
