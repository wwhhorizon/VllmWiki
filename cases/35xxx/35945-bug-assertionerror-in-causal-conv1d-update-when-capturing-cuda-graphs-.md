# vllm-project/vllm#35945: [Bug]: AssertionError in causal_conv1d_update when capturing CUDA graphs for Qwen3.5/GDN layers

| 字段 | 值 |
| --- | --- |
| Issue | [#35945](https://github.com/vllm-project/vllm/issues/35945) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError in causal_conv1d_update when capturing CUDA graphs for Qwen3.5/GDN layers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When starting vLLM with Qwen3.5-4B model (which uses GDN - Gated Delta Net attention), the server fails during CUDA Graph capture with an `AssertionError` in `causal_conv1d_update`. ## code # 1. install depend export VLLM_PRECOMPILED_WHEEL_LOCATION=/root/wheel/vllm-0.16.1rc1.dev175+gb8401cde0.cu130-cp38-abi3-manylinux_2_35_x86_64.whl export VLLM_USE_PRECOMPILED=1 VLLM_USE_PRECOMPILED=1 uv pip install --editable . # 2. Start server with Qwen3.5 model vllm serve /path/to/Qwen3.5-4B --max-model-len 8192 ## err (EngineCore_DP0 pid=XXXXX) ERROR 03-04 09:54:26 [core.py:1079] File "/root/vscode/vllm/vllm/model_executor/layers/mamba/ops/causal_conv1d.py", line 1162, in causal_conv1d_update (EngineCore_DP0 pid=XXXXX) ERROR 03-04 09:54:26 [core.py:1079] assert num_cache_lines >= batch (EngineCore_DP0 pid=XXXXX) ERROR 03-04 09:54:26 [core.py:1079] ^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=XXXXX) ERROR 03-04 09:54:26 [core.py:1079] AssertionError ## Root Cause Analysis The assertion `assert num_cache_lines >= batch` at line 1162 is **incorrect** when `conv_state_indices` is provided: 1. **What `num_cache_lines` actually is:** - For GDN la...

## 现有链接修复摘要

#36324 [Bugfix] Remove incorrect assertion in causal_conv1d_update for Qwen3.5 GDN layersfix: remove incorrect assertion in causal_conv1d_u… | #36325 [Bugfix] Disable TMA on Blackwell GPUs to fix Triton autotuner OOM in fla/solve_trilfix: disable TMA on Blackwell (sm_12x) to preven…

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: apture with an `AssertionError` in `causal_conv1d_update`. ## code # 1. install depend export VLLM_PRECOMPILED_WHEEL_LOCATION=/root/wheel/vllm-0.16.1rc1.dev175+gb8401cde0.cu130-cp38-abi3-manylinux_2_35_x86_64.whl export...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: AssertionError in causal_conv1d_update when capturing CUDA graphs for Qwen3.5/GDN layers bug ### Your current environment ### 🐛 Describe the bug When starting vLLM with Qwen3.5-4B model (which uses GDN - Gated De...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ]: AssertionError in causal_conv1d_update when capturing CUDA graphs for Qwen3.5/GDN layers bug ### Your current environment ### 🐛 Describe the bug When starting vLLM with Qwen3.5-4B model (which uses GDN - Gated Delta...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rt;sampling_logits;speculative_decoding attention;cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency;shape #36324 [Bugfix] Remove incorrect assertion in causal_conv1d_update for Qwen3.5 GDN layers...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: speculative_decoding attention;cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency;shape #36324 [Bugfix] Remove incorrect assertion in causal_conv1d_update for Qwen3.5 GDN layersfix: remove incorre...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36324](https://github.com/vllm-project/vllm/pull/36324) | mentioned | 0.6 | [Bugfix] Remove incorrect assertion in causal_conv1d_update for Qwen3.5 GDN layersfix: remove incorrect assertion in causal_conv1d_update for GDN index… | wen3.5-35B-A3B-AWQ, Qwen3.5-27B-AWQ - CUDA: 12.8 ## Related Issues - #35945 (same root cause, closed without merge) - #35743 (Qwen3.5 AWQ CUDA graph failures) - #34571 (related fi… |
| [#36325](https://github.com/vllm-project/vllm/pull/36325) | mentioned | 0.6 | [Bugfix] Disable TMA on Blackwell GPUs to fix Triton autotuner OOM in fla/solve_trilfix: disable TMA on Blackwell (sm_12x) to prevent Triton autotuner OO… | ated Issues - #35743 (Qwen3.5 AWQ CUDA graph failures on Blackwell) - #35945 (causal_conv1d AssertionError - related GDN bug) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
