# vllm-project/vllm#38386: [Transformers v5] Base model and LoRA used in test has incorrect `tokenizer_config.json`

| 字段 | 值 |
| --- | --- |
| Issue | [#38386](https://github.com/vllm-project/vllm/issues/38386) |
| 状态 | open |
| 标签 | help wanted;good first issue |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Transformers v5] Base model and LoRA used in test has incorrect `tokenizer_config.json`

### Issue 正文摘录

This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, please read the description of this issue before beginning to work on this one. ## Which test is failing? The `tokenizer_config.json` is incorrect for both the base model and the adapter. If we duplicated these checkpoints and stored them inside https://huggingface.co/vllm-project, then we could own them and update the tokenizer class to be `PreTrainedTokenizerFast` which will almost always work. ```console $ pytest tests/lora/test_quant_model.py::test_quant_model_lora[model0] ... AssertionError: assert ['#f07733: A ...#f08800: A v'] == ['#f07700: A ...#f00000: A v'] [2026-03-27T01:15:06Z] [2026-03-27T01:15:06Z] At index 0 diff: '#f07733: A v' != '#f07700: A v' [2026-03-27T01:15:06Z] [2026-03-27T01:15:06Z] Full diff: [2026-03-27T01:15:06Z] [ [2026-03-27T01:15:06Z] - '#f07700: A v', [2026-03-27T01:15:06Z] ? ^^ [2026-03-27T01:15:06Z] + '#f07733: A v', [2026-03-27T01:15:06Z] ? ^^ [2026-03-27T01:15:06Z] - '#f00000: A v', [2026-03-27T01:15:06Z] ? ^^ [2026-03-27T01:15:06Z] + '#f08800: A v', [2026-03-27T01:15:06Z] ? ^^ [2026-03-27T01:15:06Z] ] ``` ## How to configure my environment? It's ve...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: -27T01:15:06Z] ] ``` ## How to configure my environment? It's very important that you install both vLLM and Transformers from source so that your test results reflect the current state of both libraries. ```console # Or...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Transformers v5] Base model and LoRA used in test has incorrect `tokenizer_config.json` help wanted;good first issue This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, pl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ast` which will almost always work. ```console $ pytest tests/lora/test_quant_model.py::test_quant_model_lora[model0] ... AssertionError: assert ['#f07733: A ...#f08800: A v'] == ['#f07700: A ...#f00000: A v'] [2026-03-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Transformers v5] Base model and LoRA used in test has incorrect `tokenizer_config.json` help wanted;good first issue This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, pl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
