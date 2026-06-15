# vllm-project/vllm#27437: [Bug]: Extremely slow FA3 on Hopper for CUDA 13.0

| 字段 | 值 |
| --- | --- |
| Issue | [#27437](https://github.com/vllm-project/vllm/issues/27437) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Extremely slow FA3 on Hopper for CUDA 13.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running these test scripts, the avg time for each FA3 iteration takes about 0.024s, which translates to ~50GB/s memory bandwidth. This issue doesn't occur on H200 (which only takes 0.00033s). Update: The slowness on h100 was due to CUDA 13.0 compiler; changing to CUDA 12.8 and recompiling solved the speed problem. ```python # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project import time import pytest import torch from vllm.platforms import current_platform from vllm.vllm_flash_attn import ( fa_version_unsupported_reason, flash_attn_varlen_func, is_fa_version_supported, ) NUM_HEADS = [(8, 1)] HEAD_SIZES = [128] BLOCK_SIZES = [16] DTYPES = [torch.bfloat16] QDTYPES = [None] # one value large enough to test overflow in index calculation. # one value small enough to test the schema op check NUM_BLOCKS = [131072] SOFT_CAPS = [None] SLIDING_WINDOWS = [None] kwargs={ "use_out": True, "seq_lens": [(6, 2048)] * 1023, "num_heads": (8, 1), "head_size": 128, "block_size": 16, "sliding_window": None, "dtype": torch.bfloat16, "soft_cap": None, "num_blocks": 131072, "fa_version": 3, "q_...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: supported, ) NUM_HEADS = [(8, 1)] HEAD_SIZES = [128] BLOCK_SIZES = [16] DTYPES = [torch.bfloat16] QDTYPES = [None] # one value large enough to test overflow in index calculation. # one value small enough to test the sch...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: only takes 0.00033s). Update: The slowness on h100 was due to CUDA 13.0 compiler; changing to CUDA 12.8 and recompiling solved the speed problem. ```python # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Extremely slow FA3 on Hopper for CUDA 13.0 bug;stale ### Your current environment ### 🐛 Describe the bug When running these test scripts, the avg time for each FA3 iteration takes about 0.024s, which translates t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Extremely slow FA3 on Hopper for CUDA 13.0 bug;stale ### Your current environment ### 🐛 Describe the bug When running these test scripts, the avg time for each FA3 iteration takes about 0.024s, which translates t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: is_fa_version_supported, ) NUM_HEADS = [(8, 1)] HEAD_SIZES = [128] BLOCK_SIZES = [16] DTYPES = [torch.bfloat16] QDTYPES = [None] # one value large enough to test overflow in index calculation. # one value small enough t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
