# vllm-project/vllm#41920: [Bug]: get_expert_mapping is inconsistent with load_weights for EPLB in DeepseekV2 and AXK1

| 字段 | 值 |
| --- | --- |
| Issue | [#41920](https://github.com/vllm-project/vllm/issues/41920) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | hardware_porting;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | moe;quantization |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: get_expert_mapping is inconsistent with load_weights for EPLB in DeepseekV2 and AXK1

### Issue 正文摘录

### Describe the bug `get_expert_mapping` and `load_weights` are inconsistent in `DeepseekV2ForCausalLM` and `AXK1ForCausalLM` when EPLB (Expert Parallelism Load Balancer) is enabled. `load_weights` correctly uses `num_redundant_experts=self.num_redundant_experts` and accounts for ROCm AITER fusion shared experts, but `get_expert_mapping` hardcodes `num_redundant_experts=0` and ignores shared experts: **`deepseek_v2.py` line 1472 / `AXK1.py`:** ```python def get_expert_mapping(self) -> list[tuple[str, str, int, str]]: return fused_moe_make_expert_params_mapping( self, num_experts=self.config.n_routed_experts, # missing shared experts when AITER enabled num_redundant_experts=0, # should be self.num_redundant_experts ) ``` `get_expert_mapping` is called externally by the BitsAndBytes loader (`bitsandbytes_loader.py`) and the LoRA system (`lora/utils.py`) via `get_moe_expert_mapping()`. The incorrect mapping may cause wrong weight loading under BitsAndBytes quantization or LoRA when EPLB is active. ### Origin This was introduced in PR #18343 which added EPLB support to `load_weights` but did not update `get_expert_mapping`. `AXK1ForCausalLM` inherited the same pattern when the model...

## 现有链接修复摘要

#18343 [Feature] Expert Parallelism Load Balancer (EPLB) | #41930 [Bugfix] Fix EPLB expert mapping for DeepSeekV2 and AXK1

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: `DeepseekV2ForCausalLM` and `AXK1ForCausalLM` when EPLB (Expert Parallelism Load Balancer) is enabled. `load_weights` correctly uses `num_redundant_experts=self.num_redundant_experts` and accounts for ROCm AITER fusion...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: d_moe_make_expert_params_mapping( self, num_experts=self.config.n_routed_experts, # missing shared experts when AITER enabled num_redundant_experts=0, # should be self.num_redundant_experts ) ``` `get_expert_mapping` is...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: get_expert_mapping is inconsistent with load_weights for EPLB in DeepseekV2 and AXK1 ### Describe the bug `get_expert_mapping` and `load_weights` are inconsistent in `DeepseekV2ForCausalLM` and `AXK1ForCausalLM`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: `num_redundant_experts=self.num_redundant_experts` and accounts for ROCm AITER fusion shared experts, but `get_expert_mapping` hardcodes `num_redundant_experts=0` and ignores shared experts: **`deepseek_v2.py` line 1472...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ectness hardware_porting;model_support;moe;quantization moe;quantization mismatch env_dependency #18343 [Feature] Expert Parallelism Load Balancer (EPLB) | #41930 [Bugfix] Fix EPLB expert mapping for DeepSeekV2 and AXK1...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18343](https://github.com/vllm-project/vllm/pull/18343) | mentioned | 0.45 | [Feature] Expert Parallelism Load Balancer (EPLB) | n or lora when eplb is active. ### origin this was introduced in pr #18343 which added eplb support to `load_weights` but did not update `get_expert_mapping`. `axk1forcausallm` in… |
| [#41930](https://github.com/vllm-project/vllm/pull/41930) | closes_keyword | 0.95 | [Bugfix] Fix EPLB expert mapping for DeepSeekV2 and AXK1 | Fixes #41920. `get_expert_mapping()` for DeepSeekV2 and AXK1 used only `n_routed_experts` and hard-coded `num_redundant_experts=0`. Their `load_weights()` paths include shared exp |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
