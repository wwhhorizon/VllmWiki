# vllm-project/vllm#43263: [Bug]: AttributeError in mla_attention.py L2094 (_compute_prefill_context) on long prefill with AWQ model — regression after PR #34695

| 字段 | 值 |
| --- | --- |
| Issue | [#43263](https://github.com/vllm-project/vllm/issues/43263) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: AttributeError in mla_attention.py L2094 (_compute_prefill_context) on long prefill with AWQ model — regression after PR #34695

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Your current environment ## 🐛 Describe the bug In `vllm/model_executor/layers/attention/mla_attention.py`, function `_compute_prefill_context` (around line 2094), the code defines a safe local variable `_kv_b_proj_w_dtype` with a `hasattr(self.kv_b_proj, "weight")` fallback, but then **a few lines below still uses `self.kv_b_proj.weight.dtype` directly** in the `.to()` call. This crashes AWQ/GPTQ quantized models on long-prompt prefill with: ``` AttributeError: 'ColumnParallelLinear' object has no attribute 'weight' ``` The crash kills the EngineCore (not just the request), requiring server restart. This appears to be a regression introduced **after** PR #34695 was merged — likely by a subsequent commit that added NVFP4 support and rewrote the surrounding `if` condition but forgot to use the safe variable inside the `.to()` call. ### The problematic code (current state in the running container) `vllm/model_executor/layers/attention/mla_attention.py` lines ~2080–2095: ```python # For quantized layers (AWQ/GPTQ) that lack a .weight attribute, # use params_dtype which is the expected input dtype. _kv_b_proj_w_dtype = ( self.kv_b_...

## 现有链接修复摘要

#34695 [Bugfix] Fix MLA attention crash with AWQ/GPTQ quantized models | #43264 Fix AttributeError in mla_attention.py for AWQ-quantized models

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: (around line 2094), the code defines a safe local variable `_kv_b_proj_w_dtype` with a `hasattr(self.kv_b_proj, "weight")` fallback, but then **a few lines below still uses `self.kv_b_proj.weight.dtype` directly** in th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: # ← line 2094, BUG ``` The `_kv_b_proj_w_dtype` variable is defined precisely to be used here, but the `.to()` call still goes to `self.kv_b_proj.weight.dtype` directly, bypassing the `hasattr` guard. ### Symptom: only...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d. ### Symptom: only triggered by long-prompt prefill - Short prompts (smoke test with tool calling, ~163 tokens) work fine. - Engine startup, warmup, and model loading succeed. - API endpoints respond normally. - **But...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [multiproc_executor.py:962] File ".../vllm/model_executor/models/glm4_moe_lite.py", line 606, in forward (Worker_TP0 pid=142) ERROR 05-20 23:24:00 [multiproc_executor.py:962] File ".../vllm/model_executor/layers/attenti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: AttributeError in mla_attention.py L2094 (_compute_prefill_context) on long prefill with AWQ model — regression after PR #34695 bug ### Your current environment ### 🐛 Describe the bug ## Your current environment...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34695](https://github.com/vllm-project/vllm/pull/34695) | mentioned | 0.45 | [Bugfix] Fix MLA attention crash with AWQ/GPTQ quantized models | ver restart. this appears to be a regression introduced **after** pr #34695 was merged — likely by a subsequent commit that added nvfp4 support and rewrote the surrounding `if` co… |
| [#43264](https://github.com/vllm-project/vllm/pull/43264) | closes_keyword | 0.95 | Fix AttributeError in mla_attention.py for AWQ-quantized models | Fix Summary **Issue**: vllm-project/vllm#43263 - AttributeError in mla_attention.py L2094 (_compute_prefill_context) on long prefill with AWQ model ### Root Cause The bug had tw |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
