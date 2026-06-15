# vllm-project/vllm#38384: [Transformers v5] Distributed shutdown test timetout

| 字段 | 值 |
| --- | --- |
| Issue | [#38384](https://github.com/vllm-project/vllm/issues/38384) |
| 状态 | closed |
| 标签 | help wanted;good first issue |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Transformers v5] Distributed shutdown test timetout

### Issue 正文摘录

This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, please read the description of this issue before beginning to work on this one. ## Which test is failing? This test seems to be reliably failing in CI when v5 is installed, but I have not been able to reproduce it locally. ```console $ pytest tests/v1/shutdown/test_delete.py::test_llm_delete[False-True-2-hmellor/tiny-random-LlamaForCausalLM] ... Failed: Timeout >120.0s ``` ## How to configure my environment? It's very important that you install both vLLM and Transformers from source so that your test results reflect the current state of both libraries. ```console # Or your fork git clone https://github.com/huggingface/transformers.git git clone https://github.com/vllm-project/vllm.git cd vllm VLLM_USE_PRECOMPILED=1 uv pip install -e . uv pip install -e ../transformers ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e. ## Which test is failing? This test seems to be reliably failing in CI when v5 is installed, but I have not been able to reproduce it locally. ```console $ pytest tests/v1/shutdown/test_delete.py::test_llm_delete[Fal...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: hutdown/test_delete.py::test_llm_delete[False-True-2-hmellor/tiny-random-LlamaForCausalLM] ... Failed: Timeout >120.0s ``` ## How to configure my environment? It's very important that you install both vLLM and Transform...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: reliably failing in CI when v5 is installed, but I have not been able to reproduce it locally. ```console $ pytest tests/v1/shutdown/test_delete.py::test_llm_delete[False-True-2-hmellor/tiny-random-LlamaForCausalLM] ......
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ```console $ pytest tests/v1/shutdown/test_delete.py::test_llm_delete[False-True-2-hmellor/tiny-random-LlamaForCausalLM] ... Failed: Timeout >120.0s ``` ## How to configure my environment? It's very important that you i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Transformers v5] Distributed shutdown test timetout help wanted;good first issue This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, please read the description of this is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
