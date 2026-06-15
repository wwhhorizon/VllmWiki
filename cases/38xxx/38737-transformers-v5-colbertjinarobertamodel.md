# vllm-project/vllm#38737: [Transformers v5] ColBERTJinaRobertaModel

| 字段 | 值 |
| --- | --- |
| Issue | [#38737](https://github.com/vllm-project/vllm/issues/38737) |
| 状态 | closed |
| 标签 | help wanted;good first issue |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Transformers v5] ColBERTJinaRobertaModel

### Issue 正文摘录

This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, please read the description of this issue before beginning to work on this one. ## Which test is failing? ```console $ pytest tests/models/language/pooling/test_colbert.py::test_colbert_hf_comparison[jina] ... AssertionError: Embedding mismatch for text 0 ``` ## How to configure my environment? It's very important that you install both vLLM and Transformers from source so that your test results reflect the current state of both libraries. ```console # Or your fork git clone https://github.com/huggingface/transformers.git git clone https://github.com/vllm-project/vllm.git cd vllm VLLM_USE_PRECOMPILED=1 uv pip install -e . uv pip install -e ../transformers ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Transformers v5] ColBERTJinaRobertaModel help wanted;good first issue This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, please read the description of this issue before...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: mismatch for text 0 ``` ## How to configure my environment? It's very important that you install both vLLM and Transformers from source so that your test results reflect the current state of both libraries. ```console #...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: lbert.py::test_colbert_hf_comparison[jina] ... AssertionError: Embedding mismatch for text 0 ``` ## How to configure my environment? It's very important that you install both vLLM and Transformers from source so that yo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ert.py::test_colbert_hf_comparison[jina] ... AssertionError: Embedding mismatch for text 0 ``` ## How to configure my environment? It's very important that you install both vLLM and Transformers from source so that your...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: escription of this issue before beginning to work on this one. ## Which test is failing? ```console $ pytest tests/models/language/pooling/test_colbert.py::test_colbert_hf_comparison[jina] ... AssertionError: Embedding...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
