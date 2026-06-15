# vllm-project/vllm#42769: [Bug]: DeepSeek V4 load_weights UnboundLocalError: 'name_mapped' when expert mapping has no match

| 字段 | 值 |
| --- | --- |
| Issue | [#42769](https://github.com/vllm-project/vllm/issues/42769) |
| 状态 | open |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;moe;quantization |
| 子分类 | wrong_output |
| Operator 关键词 | moe;quantization |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V4 load_weights UnboundLocalError: 'name_mapped' when expert mapping has no match

### Issue 正文摘录

### Summary `vllm/model_executor/models/deepseek_v4.py` has an unbound-local bug in `DeepseekV4ForCausalLM.load_weights()`'s expert branch. The variable `name_mapped` is assigned **inside** a `for mapping in expert_mapping` loop, but referenced **after** the loop. When no entry in `expert_mapping` matches the incoming tensor name (all iterations hit the early `continue`), `name_mapped` is never bound — but the subsequent `loaded_params.add(name_mapped)` still runs: ``` File "vllm/model_executor/models/deepseek_v4.py", line 1557, in load_weights loaded_params.add(name_mapped) UnboundLocalError: cannot access local variable 'name_mapped' where it is not associated with a value ``` ### Environment - vLLM: 0.21.0 (also reproducible on `main` as of 2026-05-15) - Transformers: 4.57.1 - Hardware: 2× A100 80GB, TP=2 - Trigger: any DSV4 checkpoint whose expert weight tensor names don't match every entry in `get_expert_mapping()` (e.g., custom quantization-aware suffixes like `.tq_packed`). ### Affected code `vllm/model_executor/models/deepseek_v4.py` around lines 1532-1558 (line numbers from main as of 2026-05-15, may drift slightly): ```python if ".experts." in name: # E8M0 scales special...

## 现有链接修复摘要

#42806 [Bugfix] DeepSeek V4: support transformers >= 4.57 normalized compress_ratios | #42814 [Bugfix][DeepseekV4] Make WeightsMapper head/embed rules idempotent | #43442 [Bugfix][DeepseekV4] Gate expert weight load on success | #44030 [Bugfix] DeepSeek V4: skip expert tensor when no mapping succeeds (AMD + NVIDIA)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: calError: cannot access local variable 'name_mapped' where it is not associated with a value ``` ### Environment - vLLM: 0.21.0 (also reproducible on `main` as of 2026-05-15) - Transformers: 4.57.1 - Hardware: 2× A100 8...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: s not associated with a value ``` ### Environment - vLLM: 0.21.0 (also reproducible on `main` as of 2026-05-15) - Transformers: 4.57.1 - Hardware: 2× A100 80GB, TP=2 - Trigger: any DSV4 checkpoint whose expert weight te...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: or names don't match every entry in `get_expert_mapping()` (e.g., custom quantization-aware suffixes like `.tq_packed`). ### Affected code `vllm/model_executor/models/deepseek_v4.py` around lines 1532-1558 (line numbers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ucible on `main` as of 2026-05-15) - Transformers: 4.57.1 - Hardware: 2× A100 80GB, TP=2 - Trigger: any DSV4 checkpoint whose expert weight tensor names don't match every entry in `get_expert_mapping()` (e.g., custom qu...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: DeepSeek V4 load_weights UnboundLocalError: 'name_mapped' when expert mapping has no match ### Summary `vllm/model_executor/models/deepseek_v4.py` has an unbound-local bug in `DeepseekV4ForCausalLM.load_weights()...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42806](https://github.com/vllm-project/vllm/pull/42806) | mentioned | 0.6 | [Bugfix] DeepSeek V4: support transformers >= 4.57 normalized compress_ratios | n on the modified file. ## Related work Same DSV4 bug-report set: - #42769 / PR #42804: `name_mapped` `UnboundLocalError` in expert loading. - #42777 / PR #42805: `WeightsMapper.o… |
| [#42814](https://github.com/vllm-project/vllm/pull/42814) | mentioned | 0.6 | [Bugfix][DeepseekV4] Make WeightsMapper head/embed rules idempotent | mes untouched; `.ffn_norm.weight` still fires ## Related #42741 and #42769 are unrelated DSV4 loader issues found in the same validation pass. Related: #42777 |
| [#43442](https://github.com/vllm-project/vllm/pull/43442) | closes_keyword | 0.95 | [Bugfix][DeepseekV4] Gate expert weight load on success | Closes #42769 |
| [#44030](https://github.com/vllm-project/vllm/pull/44030) | closes_keyword | 0.95 | [Bugfix] DeepSeek V4: skip expert tensor when no mapping succeeds (AMD + NVIDIA) | Closes #42769 ## Test Plan - [ ] Existing DeepSeek V4 load_weights coverage via CI. ## Duplicate-work check `gh pr list --repo vllm-project/vllm --state open --search "deepseek |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
