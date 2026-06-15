# vllm-project/vllm#38520: [Bug]: LoRA loading fails for Qwen 3.5 MoE (35b-A3b) due to expert module name mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#38520](https://github.com/vllm-project/vllm/issues/38520) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: LoRA loading fails for Qwen 3.5 MoE (35b-A3b) due to expert module name mismatch

### Issue 正文摘录

When starting the engine with **Qwen 3.5-35b-a3b** and LoRA enabled, the system throws a `ValueError`. It appears that the current expert module parsing logic in `lora_model.py` is incompatible with the naming convention used by Qwen 3.5. **Error Log:** ```text (EngineCore pid=1114) ERROR 03-30 05:34:48 [core.py:1308] raise ValueError(^M (EngineCore pid=1114) ERROR 03-30 05:34:48 [core.py:1308] ValueError: While loading /models/model_deploy/models/xxxxx_xxxxx/, expected target modules in {'in_proj_z', 'v_proj', 'in_proj_qkv', 'linear_fc2', 'q_proj', 'k_proj', 'gate', 'down_proj', 'gate_proj', 'experts', 'shared_expert_gate', 'conv1d', 'proj', 'qkv', 'o_proj', 'linear_fc1', 'in_proj_b', 'in_proj_a', 'out_proj', 'up_proj'} but received ['language_model.model.layers.0.mlp.experts.0.down_proj', 'language_model.model.layers.0.mlp.experts.0.down_proj', 'language_model.model.layers.0.mlp.experts.0.gate_proj', 'language_model.model.layers.0.mlp.experts.0.gate_proj', ...] ``` **Current Implementation Issue:** The current logic in `/lora_model.py` incorrectly parses the expert module name, leading to a mismatch with `expected_lora_modules`: ```python module_name, _ = parse_fine_tuned_lora_n...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: oRA loading fails for Qwen 3.5 MoE (35b-A3b) due to expert module name mismatch bug When starting the engine with **Qwen 3.5-35b-a3b** and LoRA enabled, the system throws a `ValueError`. It appears that the current expe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: LoRA loading fails for Qwen 3.5 MoE (35b-A3b) due to expert module name mismatch bug When starting the engine with **Qwen 3.5-35b-a3b** and LoRA enabled, the system throws a `ValueError`. It appears that the curr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: LoRA loading fails for Qwen 3.5 MoE (35b-A3b) due to expert module name mismatch bug When starting the engine with **Qwen 3.5-35b-a3b** and LoRA enabled, the system throws a `ValueError`. It appears that the curr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: LoRA loading fails for Qwen 3.5 MoE (35b-A3b) due to expert module name mismatch bug When starting the engine with **Qwen 3.5-35b-a3b** and LoRA enabled, the system throws a `ValueError`. It appears that the current exp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: base module name (e.g., `down_proj`) by splitting from the last dot, specifically for MoE layers: ```python if ".experts" in module_name: # Fix: Correctly get the last component of the module path expert_suffix = module...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
