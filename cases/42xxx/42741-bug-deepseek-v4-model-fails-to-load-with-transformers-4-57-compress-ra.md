# vllm-project/vllm#42741: [Bug]: DeepSeek V4 model fails to load with transformers ≥ 4.57 — `compress_ratios` attribute removed

| 字段 | 值 |
| --- | --- |
| Issue | [#42741](https://github.com/vllm-project/vllm/issues/42741) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | quantization |
| 症状 | crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V4 model fails to load with transformers ≥ 4.57 — `compress_ratios` attribute removed

### Issue 正文摘录

### Summary `vllm/model_executor/models/deepseek_v4.py:960` reads `config.compress_ratios[layer_id]` directly. Transformers ≥ 4.57 normalizes the legacy `compress_ratios` JSON field on `DeepseekV4Config.__init__` into `layer_types` (list of strings) + `compress_rates` (dict). The original attribute is no longer exposed on the config object. **Result:** Every DeepSeek V4 model fails to load on vLLM ≥ 0.20.2 when paired with transformers ≥ 4.57: ``` AttributeError: 'DeepseekV4Config' object has no attribute 'compress_ratios'. Did you mean: 'compress_rates'? ``` The error fires inside the multiproc worker during `EngineCore` init, propagating as `Engine core initialization failed`. ### Environment - vLLM: 0.21.0 (also reproducible on 0.20.2; the affected code landed in #40860) - Transformers: 4.57.1 (and almost certainly any ≥ 4.57) - Model: `deepseek-ai/DeepSeek-V4-Flash` (likely all DSV4 family) - Hardware: 2× A100 80GB, TP=2, `trust_remote_code=True` ### Repro ```python from vllm import LLM llm = LLM( model="deepseek-ai/DeepSeek-V4-Flash", # or any DSV4 checkpoint quantization=None, tensor_parallel_size=2, max_model_len=2048, gpu_memory_utilization=0.85, trust_remote_code=True, )...

## 现有链接修复摘要

#42806 [Bugfix] DeepSeek V4: support transformers >= 4.57 normalized compress_ratios | #42814 [Bugfix][DeepseekV4] Make WeightsMapper head/embed rules idempotent

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: re initialization failed`. ### Environment - vLLM: 0.21.0 (also reproducible on 0.20.2; the affected code landed in #40860) - Transformers: 4.57.1 (and almost certainly any ≥ 4.57) - Model: `deepseek-ai/DeepSeek-V4-Flas...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `deepseek-ai/DeepSeek-V4-Flash` (likely all DSV4 family) - Hardware: 2× A100 80GB, TP=2, `trust_remote_code=True` ### Repro ```python from vllm import LLM llm = LLM( model="deepseek-ai/DeepSeek-V4-Flash", # or any DSV4...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: essed_sparse_attention": 4, "heavily_compressed_attention": 128}`). The mapping between the two is one-to-one: ```python compress_ratios[i] = compress_rates.get(layer_types[i], 0) ``` ### Proposed fix Update `vllm/model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: DeepSeek V4 model fails to load with transformers ≥ 4.57 — `compress_ratios` attribute removed ### Summary `vllm/model_executor/models/deepseek_v4.py:960` reads `config.compress_ratios[layer_id]` directly. Transf...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: gine core initialization failed`. ### Environment - vLLM: 0.21.0 (also reproducible on 0.20.2; the affected code landed in #40860) - Transformers: 4.57.1 (and almost certainly any ≥ 4.57) - Model: `deepseek-ai/DeepSeek-...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42806](https://github.com/vllm-project/vllm/pull/42806) | closes_keyword | 0.95 | [Bugfix] DeepSeek V4: support transformers >= 4.57 normalized compress_ratios | Closes #42741. `DeepseekV4Attention.__init__` reads `config.compress_ratios[layer_id]` directly (`vllm/model_executor/models/deepseek_v4.py:960`). transformers >= 4.57 reshapes th |
| [#42814](https://github.com/vllm-project/vllm/pull/42814) | mentioned | 0.6 | [Bugfix][DeepseekV4] Make WeightsMapper head/embed rules idempotent | nrelated names untouched; `.ffn_norm.weight` still fires ## Related #42741 and #42769 are unrelated DSV4 loader issues found in the same validation pass. Related: #42777 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
