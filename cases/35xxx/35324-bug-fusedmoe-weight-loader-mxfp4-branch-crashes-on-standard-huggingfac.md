# vllm-project/vllm#35324: [Bug]: FusedMoE.weight_loader MXFP4 branch crashes on standard HuggingFace MoE checkpoints (per-expert 2-D weights)

| 字段 | 值 |
| --- | --- |
| Issue | [#35324](https://github.com/vllm-project/vllm/issues/35324) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support;moe;quantization |
| 子分类 | shape_align |
| Operator 关键词 | moe;quantization |
| 症状 | crash;mismatch |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FusedMoE.weight_loader MXFP4 branch crashes on standard HuggingFace MoE checkpoints (per-expert 2-D weights)

### Issue 正文摘录

### Your current environment vLLM: 0.15.1 (`vllm/vllm-openai:latest` as of 2025-02-25) Model: `Qwen/Qwen3-30B-A3B` (128 experts, per-expert weight layout) GPU: NVIDIA RTX 5880 Ada (SM89), also reproducible on any GPU ### 🐛 Describe the bug ## Bug Description The MXFP4 early-return path in `FusedMoE.weight_loader` (`vllm/model_executor/layers/fused_moe/layer.py`) assumes all expert weights are stacked into a 3-D tensor `[num_experts, out, in]`. Standard HuggingFace MoE checkpoints (e.g., Qwen3-30B-A3B, Mixtral) store one 2-D tensor `[out, in]` per expert, causing two cascading failures. ## Steps to Reproduce ```python from vllm import LLM llm = LLM(model="Qwen/Qwen3-30B-A3B", quantization="mxfp4") ``` Bug 1: IndexError on 2-D weights The MXFP4 branch unconditionally accesses loaded_weight.shape[2]: ```python # layer.py, FusedMoE.weight_loader if self.quant_config and self.quant_config.get_name() == "mxfp4": if "bias" in weight_name: dim1 = loaded_weight.shape[1] param.data[:, :dim1].copy_(loaded_weight) else: dim1 = loaded_weight.shape[1] dim2 = loaded_weight.shape[2] # = 2: param.data[:, :loaded_weight.shape[1]].copy_(loaded_weight) return True if return_success else None if loade...

## 现有链接修复摘要

#35366 [Bugfix] Fix MXFP4 weight_loader crash on per-expert 2-D weights

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: FusedMoE.weight_loader MXFP4 branch crashes on standard HuggingFace MoE checkpoints (per-expert 2-D weights) bug;stale ### Your current environment vLLM: 0.15.1 (`vllm/vllm-openai:latest` as of 2025-02-25) Model:...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: perts, per-expert weight layout) GPU: NVIDIA RTX 5880 Ada (SM89), also reproducible on any GPU ### 🐛 Describe the bug ## Bug Description The MXFP4 early-return path in `FusedMoE.weight_loader` (`vllm/model_executor/laye...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: per-expert weight layout) GPU: NVIDIA RTX 5880 Ada (SM89), also reproducible on any GPU ### 🐛 Describe the bug ## Bug Description The MXFP4 early-return path in `FusedMoE.weight_loader` (`vllm/model_executor/layers/fuse...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FusedMoE.weight_loader MXFP4 branch crashes on standard HuggingFace MoE checkpoints (per-expert 2-D weights) bug;stale ### Your current environment vLLM: 0.15.1 (`vllm/vllm-openai:latest` as of 2025-02-25) Model:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: wen/Qwen3-30B-A3B` (128 experts, per-expert weight layout) GPU: NVIDIA RTX 5880 Ada (SM89), also reproducible on any GPU ### 🐛 Describe the bug ## Bug Description The MXFP4 early-return path in `FusedMoE.weight_loader`...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35366](https://github.com/vllm-project/vllm/pull/35366) | closes_keyword | 0.95 | [Bugfix] Fix MXFP4 weight_loader crash on per-expert 2-D weights | Fixes #35324 The MXFP4 early-return path in `FusedMoE.weight_loader` (`layer.py:1064-1073`) assumed all expert weights are stacked into a 3-D tensor `[num_experts, out, in]` (gpt- |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
