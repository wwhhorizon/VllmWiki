# vllm-project/vllm#38658: [Bug]: MLA attention casts activations to int32 when using Marlin FP8 on GPUs without native FP8 support (sm < 89)

| 字段 | 值 |
| --- | --- |
| Issue | [#38658](https://github.com/vllm-project/vllm/issues/38658) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MLA attention casts activations to int32 when using Marlin FP8 on GPUs without native FP8 support (sm < 89)

### Issue 正文摘录

### Your current environment ``` For security purposes, please feel free to check the contents of collect_env.py before running it. python collect_env.py --2026-03-31 17:05:06-- https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env.py Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8001::154, 2606:50c0:8000::154, 2606:50c0:8003::154, ... Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8001::154|:443... connected. HTTP request sent, awaiting response... 200 OK Length: 27835 (27K) [text/plain] Saving to: ‘collect_env.py’ collect_env.py 100%[=========================================================================================================>] 27.18K --.-KB/s in 0.001s 2026-03-31 17:05:06 (18.5 MB/s) - ‘collect_env.py’ saved [27835/27835] Collecting environment information... ============================== System Info ============================== OS : Debian GNU/Linux 11 (bullseye) (x86_64) GCC version : (Debian 10.2.1-6) 10.2.1 20210110 Clang version : 11.0.1-2 CMake version : version 3.18.4 Libc version : glibc-2.31 ============================== PyTorch Info ============================== PyTorch...

## 现有链接修复摘要

#38771 [Bugfix] Fix MLA kv_b_proj activation dtype with Marlin FP8

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : Debian GNU/Linux 11 (bullseye) (x86_64) GCC version : (Debian 10.2.1-6) 10.2.1 20210110 Clang version : 11.0.1-2 CMake version : version 3.18.4 Libc version : glibc-2.31 ==============================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: tions to int32 when using Marlin FP8 on GPUs without native FP8 support (sm < 89) bug ### Your current environment ``` For security purposes, please feel free to check the contents of collect_env.py before running it. p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 5 MB/s) - ‘collect_env.py’ saved [27835/27835] Collecting environment information... ============================== System Info ============================== OS : Debian GNU/Linux 11 (bullseye) (x86_64) GCC version : (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: (raw.githubusercontent.com)|2606:50c0:8001::154|:443... connected. HTTP request sent, awaiting response... 200 OK Length: 27835 (27K) [text/plain] Saving to: ‘collect_env.py’ collect_env.py 100%[========================...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: MLA attention casts activations to int32 when using Marlin FP8 on GPUs without native FP8 support (sm < 89) bug ### Your current environment ``` For security purposes, please feel free to check the contents of co...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38771](https://github.com/vllm-project/vllm/pull/38771) | closes_keyword | 0.95 | [Bugfix] Fix MLA kv_b_proj activation dtype with Marlin FP8 | Fixes #38658. This PR fixes an MLA prefill dtype bug when FP8 weights are served through the Marlin path on GPUs without native FP8 support (`sm < 89`). On affected GPUs, Mar |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
