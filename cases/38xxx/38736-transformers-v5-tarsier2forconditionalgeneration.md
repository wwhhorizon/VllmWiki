# vllm-project/vllm#38736: [Transformers v5] Tarsier2ForConditionalGeneration

| 字段 | 值 |
| --- | --- |
| Issue | [#38736](https://github.com/vllm-project/vllm/issues/38736) |
| 状态 | open |
| 标签 | help wanted;good first issue |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Transformers v5] Tarsier2ForConditionalGeneration

### Issue 正文摘录

This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, please read the description of this issue before beginning to work on this one. ## Which test is failing? Tarsier 2 has a malformed `config.json` in its checkpoint and vLLM already has some workarounds to account for this (the `Tarsier2Config` that gets registered in vLLM). This appears to not be working correctly with the latest Transformers. ```console $ pytest tests/models/test_initialization.py::test_can_initialize_large_subset[Tarsier2ForConditionalGeneration] ... [2026-04-01T10:33:31Z] Value error, The text_config extracted from the model config does not have `num_attention_heads` attribute. This indicates a mismatch between the model config and vLLM's expectations. Please ensure that the model config is compatible with vLLM. [type=value_error, input_value=ArgsKwargs((), {'model': ...nderer_num_workers': 1}), input_type=ArgsKwargs] ``` ## How to configure my environment? It's very important that you install both vLLM and Transformers from source so that your test results reflect the current state of both libraries. ```console # Or your fork git clone https://github.com/huggingf...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: put_type=ArgsKwargs] ``` ## How to configure my environment? It's very important that you install both vLLM and Transformers from source so that your test results reflect the current state of both libraries. ```console...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: work on this one. ## Which test is failing? Tarsier 2 has a malformed `config.json` in its checkpoint and vLLM already has some workarounds to account for this (the `Tarsier2Config` that gets registered in vLLM). This a...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: l config does not have `num_attention_heads` attribute. This indicates a mismatch between the model config and vLLM's expectations. Please ensure that the model config is compatible with vLLM. [type=value_error, input_v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: config does not have `num_attention_heads` attribute. This indicates a mismatch between the model config and vLLM's expectations. Please ensure that the model config is compatible with vLLM. [type=value_error, input_val...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: escription of this issue before beginning to work on this one. ## Which test is failing? Tarsier 2 has a malformed `config.json` in its checkpoint and vLLM already has some workarounds to account for this (the `Tarsier2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
