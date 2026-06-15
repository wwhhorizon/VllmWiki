# vllm-project/vllm#42777: [Bug]: DeepSeek V4 WeightsMapper rule `head.weight` -> `lm_head.weight` is non-idempotent

| 字段 | 值 |
| --- | --- |
| Issue | [#42777](https://github.com/vllm-project/vllm/issues/42777) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;moe |
| 子分类 |  |
| Operator 关键词 | moe |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V4 WeightsMapper rule `head.weight` -> `lm_head.weight` is non-idempotent

### Issue 正文摘录

### Summary `vllm/model_executor/models/deepseek_v4.py:1626` registers this suffix rule in the DSV4 `WeightsMapper`: ```python orig_to_new_suffix={ "head.weight": "lm_head.weight", ... } ``` The rule is **not idempotent**: `lm_head.weight` also ends with `head.weight`, so a canonical (already-correctly-named) `lm_head.weight` tensor gets the suffix replaced and becomes `lm_lm_head.weight`. The downstream lookup then fails: ``` ValueError: There is no module or parameter named 'lm_lm_head' in DeepseekV4ForCausalLM. ``` ### Environment - vLLM: 0.21.0 (also on `main` as of 2026-05-15 — `_make_deepseek_v4_weights_mapper` is unchanged) - Transformers: 4.57.1 - Hardware: 2× A100 80GB, TP=2 - Trigger: any checkpoint that exposes the head as `lm_head.weight` directly rather than via the bare `head.weight` shape the DSV4 release uses. We hit it on a TQ3-native variant of DeepSeek-V4-Flash. ### Affected code `vllm/model_executor/models/deepseek_v4.py`: ```python def _make_deepseek_v4_weights_mapper(expert_dtype: str) -> WeightsMapper: ... return WeightsMapper( ... orig_to_new_suffix={ "head.weight": "lm_head.weight", # ... other suffix mappings ... }, ... ) ``` The `WeightsMapper.orig_to_ne...

## 现有链接修复摘要

#42806 [Bugfix] DeepSeek V4: support transformers >= 4.57 normalized compress_ratios | #42814 [Bugfix][DeepseekV4] Make WeightsMapper head/embed rules idempotent

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: the head tensor is already named `lm_head.weight`: ```python from vllm import LLM llm = LLM( model=" ", tensor_parallel_size=2, trust_remote_code=True, ) ``` Workers fail during `load_weights` looking up the (non-existe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: DeepSeek V4 WeightsMapper rule `head.weight` -> `lm_head.weight` is non-idempotent ### Summary `vllm/model_executor/models/deepseek_v4.py:1626` registers this suffix rule in the DSV4 `WeightsMapper`: ```python or...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: /models/deepseek_v4.py`: ```python def _make_deepseek_v4_weights_mapper(expert_dtype: str) -> WeightsMapper: ... return WeightsMapper( ... orig_to_new_suffix={ "head.weight": "lm_head.weight", # ... other suffix mapping...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: /deepseek_v4.py`: ```python def _make_deepseek_v4_weights_mapper(expert_dtype: str) -> WeightsMapper: ... return WeightsMapper( ... orig_to_new_suffix={ "head.weight": "lm_head.weight", # ... other suffix mappings ... }...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "head.weight": "lm_head.weight", # ... other suffix mappings ... }, ... ) ``` The `WeightsMapper.orig_to_new_suffix` rules are applied via `name.endswith(orig)` → `name[:-len(orig)] + new`. With `orig = "head.weight"`:...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42806](https://github.com/vllm-project/vllm/pull/42806) | mentioned | 0.6 | [Bugfix] DeepSeek V4: support transformers >= 4.57 normalized compress_ratios | 9 / PR #42804: `name_mapped` `UnboundLocalError` in expert loading. - #42777 / PR #42805: `WeightsMapper.orig_to_new_suffix` non-idempotent. Issue author originally offered to bun… |
| [#42814](https://github.com/vllm-project/vllm/pull/42814) | mentioned | 0.6 | [Bugfix][DeepseekV4] Make WeightsMapper head/embed rules idempotent | lated DSV4 loader issues found in the same validation pass. Related: #42777 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
