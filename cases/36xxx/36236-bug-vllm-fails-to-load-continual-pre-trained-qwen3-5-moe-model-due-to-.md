# vllm-project/vllm#36236: [Bug]: vllm fails to load continual pre-trained Qwen3.5-MoE model due to missing support for transformers 5.x renamed class (Qwen3_5MoeTextConfig)

| 字段 | 值 |
| --- | --- |
| Issue | [#36236](https://github.com/vllm-project/vllm/issues/36236) |
| 状态 | open |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;moe |
| 子分类 | install |
| Operator 关键词 | cuda;moe |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm fails to load continual pre-trained Qwen3.5-MoE model due to missing support for transformers 5.x renamed class (Qwen3_5MoeTextConfig)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### LLM models - Base model: Qwen/Qwen3.5-122B-A10B (MoE) - Model type: CPT (Continued Pre-Training) from base model using transformers 5.3.0 ### Bug Description vllm fails to load a CPT model based on Qwen3.5-122B-A10B when using transformers >= 5.x. transformers 5.x renamed `Qwen3_5MoeConfig` to `Qwen3_5MoeTextConfig`, but vllm still references the old class name internally. Since the CPT (Continued Pre-Training) was performed using transformers 5.3.0, the output `config.json` uses the new class names, making it incompatible with the current vllm. ### Error ``` TypeError: Invalid type of HuggingFace config. Expected type: but found type: ``` #### Model config.json (base model output) ```json { "architectures": ["Qwen3_5MoeForConditionalGeneration"], "model_type": "qwen3_5_moe", "transformers_version": "4.57.0.dev0", } ``` #### Model config.json (CPT model output) ```json { "architectures": ["Qwen3_5MoeForCausalLM"], "model_type": "qwen3_5_moe_text", "transformers_version": "5.3.0", } ``` ### Steps to Reproduce 1. Perform CPT on Qwen/Qwen3.5-122B-A10B using transformers >= 5.x 2. Attempt to serve the CPT checkpoint with vllm ###...

## 现有链接修复摘要

#36353 [Bugfix]: Support transformers 5.x Qwen3_5MoeTextConfig | #39476 [Model] Add IsHybrid support to Qwen3_5MoeForCausalLM

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vllm fails to load continual pre-trained Qwen3.5-MoE model due to missing support for transformers 5.x renamed class (Qwen3_5MoeTextConfig) bug ### Your current environment ### 🐛 Describe the bug ### LLM models -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rConditionalGeneration"], "model_type": "qwen3_5_moe", "transformers_version": "4.57.0.dev0", } ``` #### Model config.json (CPT model output) ```json { "architectures": ["Qwen3_5MoeForCausalLM"], "model_type": "qwen3_5_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ound type: ``` #### Model config.json (base model output) ```json { "architectures": ["Qwen3_5MoeForConditionalGeneration"], "model_type": "qwen3_5_moe", "transformers_version": "4.57.0.dev0", } ``` #### Model config.js...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: wen3_5_moe_text", "transformers_version": "5.3.0", } ``` ### Steps to Reproduce 1. Perform CPT on Qwen/Qwen3.5-122B-A10B using transformers >= 5.x 2. Attempt to serve the CPT checkpoint with vllm ### Expected Behavior v...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: vllm fails to load continual pre-trained Qwen3.5-MoE model due to missing support for transformers 5.x renamed class (Qwen3_5MoeTextConfig) bug ### Your current environment ### 🐛 Describe the bug ### LLM models -...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36353](https://github.com/vllm-project/vllm/pull/36353) | closes_keyword | 0.95 | [Bugfix]: Support transformers 5.x Qwen3_5MoeTextConfig | Fixes #36236 ### Checklist - [x] Bug fix (non-breaking change) - [x] Code follows project style - [x] Linked issue |
| [#39476](https://github.com/vllm-project/vllm/pull/39476) | mentioned | 0.6 | [Model] Add IsHybrid support to Qwen3_5MoeForCausalLM | max_model_len, block_size * get_total_cp_world_size() ``` Related: #36236 🤖 Generated with [Claude Code](https://claude.com/claude-code) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
