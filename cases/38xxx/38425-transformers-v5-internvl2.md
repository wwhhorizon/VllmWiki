# vllm-project/vllm#38425: [Transformers v5] InternVL2

| 字段 | 值 |
| --- | --- |
| Issue | [#38425](https://github.com/vllm-project/vllm/issues/38425) |
| 状态 | open |
| 标签 | help wanted;good first issue |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Transformers v5] InternVL2

### Issue 正文摘录

This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, please read the description of this issue before beginning to work on this one. ## Which test is failing? Transformers v5 creates the model on the meta device first, then loads the weights, similarly to what vLLM does. The issue here is that the custom model code in the checkpoint tries to use real tensors as part of model structure construction. Since the issue here is with the HF reference generation, this cannot be fixed in vLLM (other than skipping the tests until the model works with Transformers v5). The proper solution to this issue is to upstream this architecture, which shouldn't be too hard using Modular Transformers as the text backbone is Qwen2 so that can be reused. ```console $ pytest tests/models/multimodal/generation/test_common.py::test_single_image_models[intern_vl-test_case25] ... RuntimeError: Tensor.item() cannot be called on meta tensors ``` ## How to configure my environment? It's very important that you install both vLLM and Transformers from source so that your test results reflect the current state of both libraries. ```console # Or your fork git clone https...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Transformers v5] InternVL2 help wanted;good first issue This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, please read the description of this issue before beginning to w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: lled on meta tensors ``` ## How to configure my environment? It's very important that you install both vLLM and Transformers from source so that your test results reflect the current state of both libraries. ```console...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Transformers v5). The proper solution to this issue is to upstream this architecture, which shouldn't be too hard using Modular Transformers as the text backbone is Qwen2 so that can be reused. ```console $ pytest tests...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: escription of this issue before beginning to work on this one. ## Which test is failing? Transformers v5 creates the model on the meta device first, then loads the weights, similarly to what vLLM does. The issue here is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
