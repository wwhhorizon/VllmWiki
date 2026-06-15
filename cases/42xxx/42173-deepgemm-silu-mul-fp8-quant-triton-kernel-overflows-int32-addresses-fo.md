# vllm-project/vllm#42173: DeepGEMM SiLU/mul FP8 quant Triton kernel overflows int32 addresses for large DPEP warmup shapes

| 字段 | 值 |
| --- | --- |
| Issue | [#42173](https://github.com/vllm-project/vllm/issues/42173) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;distributed_parallel;hardware_porting;moe;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | activation;cuda;fp8;kernel;moe;quantization;sampling;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> DeepGEMM SiLU/mul FP8 quant Triton kernel overflows int32 addresses for large DPEP warmup shapes

### Issue 正文摘录

### Problem `vllm.model_executor.layers.quantization.utils.fp8_utils._silu_mul_per_token_group_quant_fp8_colmajor` does row-based pointer arithmetic in int32. With large DeepGEMM MoE warmup/workspace shapes this overflows and the Triton launch fails with CUDA illegal memory access. The failure is easy to hit for GLM-style MoE inference with DPEP=16 and 36k max tokens per rank. The DeepGEMM activation-quant workspace for the SiLU/mul path is: ```text M = round_up(tokens_per_rank * dpep_size * top_k + local_experts * 127, 128) = round_up(36000 * 16 * 8 + 16 * 127, 128) = 4,610,048 N = 4096 # 2 * GLM MoE intermediate size max input element offset = M * N - 1 = 18,882,756,607 int32 max = 2,147,483,647 ``` The kernel is called from `DeepGemmExperts._act_mul_quant` for the Hopper/non-E8M0 SiLU path. ### Environment Validated on 2 nodes x 8 NVIDIA H200 GPUs: ```text vllm 0.19.0 torch 2.10.0+cu128 triton 3.6.0 cuda 12.8 deep_gemm 2.5.0+891d57b deep_ep 1.2.1+29d31c0 ``` ### Minimal reproducer Save as `repro_vllm_deepgemm_silu_int32.py`: ```python import os import socket import torch import torch.distributed as dist from vllm.model_executor.layers.quantization.utils.fp8_utils import ( silu_...

## 现有链接修复摘要

#42201 [Bugfix] Fix int32 overflow in DeepGEMM SiLU/mul FP8 Triton kernel

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: DeepGEMM SiLU/mul FP8 quant Triton kernel overflows int32 addresses for large DPEP warmup shapes ### Problem `vllm.model_executor.layers.quantization.utils.fp8_utils._silu_mul_per_token_group_quant_fp8_colmajor` does ro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: imal reproducer Save as `repro_vllm_deepgemm_silu_int32.py`: ```python import os import socket import torch import torch.distributed as dist from vllm.model_executor.layers.quantization.utils.fp8_utils import ( silu_mul...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: er_token_group_quant_fp8_colmajor, ) os.environ.setdefault("CUDA_LAUNCH_BLOCKING", "1") rank = int(os.environ.get("RANK", os.environ.get("SLURM_PROCID", "0"))) world = int(os.environ.get("WORLD_SIZE", os.environ.get("SL...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: DeepGEMM SiLU/mul FP8 quant Triton kernel overflows int32 addresses for large DPEP warmup shapes ### Problem `vllm.model_executor.layers.quantization.utils.fp8_utils._silu_mul_per_token_group_quant_fp8_colmajor` does ro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: warmup/workspace shapes this overflows and the Triton launch fails with CUDA illegal memory access. The failure is easy to hit for GLM-style MoE inference with DPEP=16 and 36k max tokens per rank. The DeepGEMM activatio...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42201](https://github.com/vllm-project/vllm/pull/42201) | closes_keyword | 0.95 | [Bugfix] Fix int32 overflow in DeepGEMM SiLU/mul FP8 Triton kernel | Fixes #42173 _silu_mul_per_token_group_quant_fp8_colmajor computes row/column offsets using int32 arithmetic: ```python m_offset = pid_m * BLOCK_M n_offset = pid_n * BLOCK_N |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
