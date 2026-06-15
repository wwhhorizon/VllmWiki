# vllm-project/vllm#40587: [Bug]: `+rotary_embedding` error with DeepSeek-V3.2-NVFP4

| 字段 | 值 |
| --- | --- |
| Issue | [#40587](https://github.com/vllm-project/vllm/issues/40587) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `+rotary_embedding` error with DeepSeek-V3.2-NVFP4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## TL;DR "Inductor replace_by_example node-count mismatch on multi-arg mutating custom ops with shared symbolic dims (triggered by vLLM sparse-MLA rotary fusion)" ## Details torch._inductor.exc.InductorError: AssertionError File ".../torch/_inductor/pattern_matcher.py", line 316, in replace_by_example assert len(graph_with_eager_vals.graph.nodes) == len(replacement.graph.nodes) Root cause is in upstream torch (over-strict assertion), but vLLM's flashinfer_rotary_embedding custom op is the trigger because it takes query and key as two independent mutated Tensor args that happen to share a symbolic leading dim. Code pointers: - pytorch: [pattern_matcher.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/pattern_matcher.py#L348-L353) - vllm: [deepseek_v2.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/deepseek_v2.py#L683) ## Reproduce - Enable `enable_qk_norm_rope_fusion` for DSv3.2 in e2e tp1 test (or use branch in vllm-project/vllm/pull/40586), and then Run `test_tp1_quant.py` on B200 - Alternatively, run model serve with cc config should also surface the error: ``` vllm serve nvidia/Dee...

## 现有链接修复摘要

#40910 [Bugfix] Skip flashinfer-rope variant in QK norm+RoPE fusion

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: # 🐛 Describe the bug ## TL;DR "Inductor replace_by_example node-count mismatch on multi-arg mutating custom ops with shared symbolic dims (triggered by vLLM sparse-MLA rotary fusion)" ## Details torch._inductor.exc.Indu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this especially if you're reporting a bug to PyTorch). For even more developer context, set TORCH_LOGS="+dynamo" [test 1] (EngineCore pid=2328) ``` ## Prop...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: `+rotary_embedding` error with DeepSeek-V3.2-NVFP4 bug ### Your current environment ### 🐛 Describe the bug ## TL;DR "Inductor replace_by_example node-count mismatch on multi-arg mutating custom ops with shared sy...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: es) Root cause is in upstream torch (over-strict assertion), but vLLM's flashinfer_rotary_embedding custom op is the trigger because it takes query and key as two independent mutated Tensor args that happen to share a s...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ### 🐛 Describe the bug ## TL;DR "Inductor replace_by_example node-count mismatch on multi-arg mutating custom ops with shared symbolic dims (triggered by vLLM sparse-MLA rotary fusion)" ## Details torch._inductor.exc.In...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40910](https://github.com/vllm-project/vllm/pull/40910) | closes_keyword | 0.95 | [Bugfix] Skip flashinfer-rope variant in QK norm+RoPE fusion | Fixes #40587 Co-authored-by: Claude ## Purpose ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklis |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
