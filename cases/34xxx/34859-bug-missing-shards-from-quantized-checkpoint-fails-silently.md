# vllm-project/vllm#34859: [Bug]: missing shards from quantized checkpoint fails silently

| 字段 | 值 |
| --- | --- |
| Issue | [#34859](https://github.com/vllm-project/vllm/issues/34859) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: missing shards from quantized checkpoint fails silently

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Loading a partial checkpoint due to missing shards does not raise neither an error nor a warning in the case of quantized models loaded via the default_loader. This is because a strict check between checkpoint parameters and model parameters is only enabled for non-quantized models: https://github.com/vllm-project/vllm/blob/e99ba957ec3953abd65332c26880efa489effc3a/vllm/model_executor/model_loader/default_loader.py#L298-L306 It makes sense not to validate exact equivalency between checkpoint and model parameters in case of quantized models, as some keywords from a quantized checkpoint may not need to be loaded into the model. However, a check on the presence of all expected shards could be performed separately to avoid silent failure. TO REPRODUCE: - generate a quantized, sharded checkpoint (e.g., FP8 via llm_compressor) - remove one shard from the save folder - the following minimal example will succeed without neither errors nor warnings, even though the model has not been correctly initialized: ```python from vllm import LLM llm = LLM(model=my/model/path) ``` ### Before submitting a new issue... - [x] Make sure you already sear...

## 现有链接修复摘要

#34967 Fix: Add shard validation for quantized models to prevent silent failures

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: though the model has not been correctly initialized: ```python from vllm import LLM llm = LLM(model=my/model/path) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: missing shards from quantized checkpoint fails silently bug;stale ### Your current environment ### 🐛 Describe the bug Loading a partial checkpoint due to missing shards does not raise neither an error nor a warni...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: pected shards could be performed separately to avoid silent failure. TO REPRODUCE: - generate a quantized, sharded checkpoint (e.g., FP8 via llm_compressor) - remove one shard from the save folder - the following minima...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s does not raise neither an error nor a warning in the case of quantized models loaded via the default_loader. This is because a strict check between checkpoint parameters and model parameters is only enabled for non-qu...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34967](https://github.com/vllm-project/vllm/pull/34967) | closes_keyword | 0.95 | Fix: Add shard validation for quantized models to prevent silent failures | Fixes:** #34859 ## Problem Loading quantized checkpoints with missing shards fails silently, which can lead to incorrect model initialization and inference results. This happens b |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
