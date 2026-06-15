# vllm-project/vllm#38387: [Transformers v5] HCXVisionForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#38387](https://github.com/vllm-project/vllm/issues/38387) |
| 状态 | closed |
| 标签 | help wanted;good first issue |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Transformers v5] HCXVisionForCausalLM

### Issue 正文摘录

This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, please read the description of this issue before beginning to work on this one. ## Which test is failing? This one we either drop from vLLM or upstream to Transformers ```console $ pytest tests/models/test_initialization.py::test_can_initialize_large_subset[HCXVisionForCausalLM] ... AttributeError: 'HCXVisionConfig' object has no attribute 'text_config' ``` ## How to configure my environment? It's very important that you install both vLLM and Transformers from source so that your test results reflect the current state of both libraries. ```console # Or your fork git clone https://github.com/huggingface/transformers.git git clone https://github.com/vllm-project/vllm.git cd vllm VLLM_USE_PRECOMPILED=1 uv pip install -e . uv pip install -e ../transformers ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ribute 'text_config' ``` ## How to configure my environment? It's very important that you install both vLLM and Transformers from source so that your test results reflect the current state of both libraries. ```console...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: er drop from vLLM or upstream to Transformers ```console $ pytest tests/models/test_initialization.py::test_can_initialize_large_subset[HCXVisionForCausalLM] ... AttributeError: 'HCXVisionConfig' object has no attribute...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: escription of this issue before beginning to work on this one. ## Which test is failing? This one we either drop from vLLM or upstream to Transformers ```console $ pytest tests/models/test_initialization.py::test_can_in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
