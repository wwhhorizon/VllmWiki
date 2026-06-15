# vllm-project/vllm#35868: [Bug] Qwen3-ASR crashes without --enforce-eager: missing dynamic_arg_dims for MRoPE positions

| 字段 | 值 |
| --- | --- |
| Issue | [#35868](https://github.com/vllm-project/vllm/issues/35868) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;multimodal_vlm |
| 子分类 | install |
| Operator 关键词 | cuda;gemm |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Qwen3-ASR crashes without --enforce-eager: missing dynamic_arg_dims for MRoPE positions

### Issue 正文摘录

## Summary `Qwen3ASRForConditionalGeneration` (and its realtime subclass `Qwen3ASRRealtimeGeneration`) crashes during torch.compile warmup when `--enforce-eager` is not set. The root cause is a missing `dynamic_arg_dims` annotation on the `@support_torch_compile` decorator. ## Error ``` torch.fx.experimental.symbolic_shapes.ConstraintViolationError: Constraints violated (L['inputs_embeds'].size()[0])! - You marked L['inputs_embeds'].size()[0] as dynamic but your code specialized it to be a constant (8192). If you're using mark_dynamic, either remove it or use maybe_mark_dynamic. User stack: File "vllm/model_executor/models/qwen3_asr.py", line 423, in forward hidden_states = self.language_model.model( ... File "vllm/model_executor/layers/rotary_embedding/mrope.py", line 302, in forward_native query = query.view(num_tokens, -1, self.head_size) ``` The crash occurs during `profile_run` → `_dummy_run` → model `forward()` → torch.compile tracing. ## Root Cause Qwen3-ASR uses MRoPE (inherited from its Qwen3 backbone). The `positions` tensor has shape `(3, num_tokens)` for MRoPE models, where dim 0 is always 3 (static) and dim 1 is the dynamic batch dimension. **The problem:** `Qwen3ASRF...

## 现有链接修复摘要

#35869 [Bugfix] Add missing dynamic_arg_dims for Qwen3-ASR torch.compile

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug] Qwen3-ASR crashes without --enforce-eager: missing dynamic_arg_dims for MRoPE positions ## Summary `Qwen3ASRForConditionalGeneration` (and its realtime subclass `Qwen3ASRRealtimeGeneration`) crashes during torch.c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: its realtime subclass `Qwen3ASRRealtimeGeneration`) crashes during torch.compile warmup when `--enforce-eager` is not set. The root cause is a missing `dynamic_arg_dims` annotation on the `@support_torch_compile` decora...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Reproduce ```bash vllm serve Qwen/Qwen3-ASR-1.7B \ --hf-overrides '{"architectures": ["Qwen3ASRRealtimeGeneration"]}' \ --max-model-len 4096 \ --limit-mm-per-prompt '{"audio": 1}' ``` (No `--enforce-eager` flag — that's...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: s`: ```python # qwen3.py, qwen2.py, qwen3_vl.py, qwen3_5.py, qwen3_omni_moe_thinker.py, etc. @support_torch_compile( dynamic_arg_dims={ "input_ids": 0, "positions": -1, # <-- critical for MRoPE (3, seq_len) shape "inter...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ediate_tensors": 0, "inputs_embeds": 0, } ) ``` ## Steps to Reproduce ```bash vllm serve Qwen/Qwen3-ASR-1.7B \ --hf-overrides '{"architectures": ["Qwen3ASRRealtimeGeneration"]}' \ --max-model-len 4096 \ --limit-mm-per-p...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35869](https://github.com/vllm-project/vllm/pull/35869) | closes_keyword | 0.95 | [Bugfix] Add missing dynamic_arg_dims for Qwen3-ASR torch.compile | Closes #35868 ## Root Cause Qwen3-ASR uses MRoPE (inherited from its Qwen3 backbone). The `positions` tensor has shape `(3, seq_len)` for MRoPE models, where dim 0 is always 3 (s |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
