# vllm-project/vllm#32840: [Bug]: [CPU Backend] Engine crashed due to error on flashinfer op registration

| 字段 | 值 |
| --- | --- |
| Issue | [#32840](https://github.com/vllm-project/vllm/issues/32840) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [CPU Backend] Engine crashed due to error on flashinfer op registration

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Build vLLM on CPU only machine - e.g. `VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel` Then run: `vllm bench throughout` and you'll hit this error: ``` (EngineCore_DP0 pid=29197) ERROR 01-22 09:14:05 [core.py:935] EngineCore failed to start. (EngineCore_DP0 pid=29197) ERROR 01-22 09:14:05 [core.py:935] Traceback (most recent call last): (EngineCore_DP0 pid=29197) ERROR 01-22 09:14:05 [core.py:935] File "/home/fadara01/vllm-torch-update/venv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 926, in run_engine_core (EngineCore_DP0 pid=29197) ERROR 01-22 09:14:05 [core.py:935] engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore_DP0 pid=29197) ERROR 01-22 09:14:05 [core.py:935] File "/home/fadara01/vllm-torch-update/venv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 691, in __init__ (EngineCore_DP0 pid=29197) ERROR 01-22 09:14:05 [core.py:935] super().__init__( (EngineCore_DP0 pid=29197) ERROR 01-22 09:14:05 [core.py:935] File "/home/fadara01/vllm-torch-update/venv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 105, in __init__ (EngineCore_DP0 pid=29197) ERROR 01-22 0...

## 现有链接修复摘要

#32855 [BugFix] Fix invalid flashinfer_fused_moe_blockscale_fp8 op registration

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: tration bug;cpu ### Your current environment ### 🐛 Describe the bug Build vLLM on CPU only machine - e.g. `VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel` Then run: `vllm bench throughout` and you'll hit this error...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: OR 01-22 09:14:05 [core.py:935] from vllm.model_executor.warmup.deep_gemm_warmup import deep_gemm_warmup (EngineCore_DP0 pid=29197) ERROR 01-22 09:14:05 [core.py:935] File "/home/fadara01/vllm-torch-update/venv/lib/pyth...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ) ERROR 01-22 09:14:05 [core.py:935] from vllm.model_executor.layers.quantization.fp8 import Fp8LinearMethod (EngineCore_DP0 pid=29197) ERROR 01-22 09:14:05 [core.py:935] File "/home/fadara01/vllm-torch-update/venv/lib/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: [CPU Backend] Engine crashed due to error on flashinfer op registration bug;cpu ### Your current environment ### 🐛 Describe the bug Build vLLM on CPU only machine - e.g. `VLLM_TARGET_DEVICE=cpu python3 setup.py b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32855](https://github.com/vllm-project/vllm/pull/32855) | closes_keyword | 0.95 | [BugFix] Fix invalid flashinfer_fused_moe_blockscale_fp8 op registration | Fixes: #32840 ## Purpose Fix invalid numeric default value in flashinfer_fused_moe_blockscale_fp8 op registration The default value has to be an int an not an enum as the error i |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
