# vllm-project/vllm#42369: [Bug]: Compiling from source (after pr#8146) fails in current image.

| 字段 | 值 |
| --- | --- |
| Issue | [#42369](https://github.com/vllm-project/vllm/issues/42369) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Compiling from source (after pr#8146) fails in current image.

### Issue 正文摘录

### Your current environment The output of python collect_env.py ```shell Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (aarch64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : 15.0.7 CMake version : version 4.3.2 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.14 (main, Feb 26 2026, 03:57:04) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.10.0-182.0.0.95.r1941_123.hce2.aarch64-aarch64-with-glibc2.35 ============================== CPU Info ============================== Architecture: aarch64 CPU op-mode(s): 64-bit Byte Order: Little Endian CPU(s): 320 On-line CPU(s) list: 0-319 Vendor ID: HiSilicon Model: 0 Thread(s) per core: 1 Core(s) per cluster: 80 Socket(s): - Cluster(s): 4 Stepping: 0x0 Frequency boost: disabled CPU max MHz: 3000.0000 CPU min MHz: 400.000...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ======== OS : Ubuntu 22.04.5 LTS (aarch64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : 15.0.7 CMake version : version 4.3.2 Libc version : glibc-2.35 ===========================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ==================== OS : Ubuntu 22.04.5 LTS (aarch64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : 15.0.7 CMake version : version 4.3.2 Libc version : glibc-2.35 ===============
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: udio==2.9.0 [pip3] torchvision==0.24.0 [pip3] transformers==5.5.3 [pip3] triton-ascend==3.2.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: The output of python collect_env.py ```shell Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (aarch64) GCC version : (Ubuntu 11.4.0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: flagm ssbs sb paca pacg dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng ecv L1d cache: 20 MiB (320 instances) L1i cache: 20 MiB (320 instances) L2 cache: 400 MiB (320 instances) L3 cache:

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | clude.zip' [2026-05-11 11:22:10] -- retry after 15 seconds (attempt #4) ... [2026-05-11 11:22:25] -- using src='https://gitcode.com/cann-src-third-party/json/releases/download/v3 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
