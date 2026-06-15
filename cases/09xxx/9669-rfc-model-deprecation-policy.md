# vllm-project/vllm#9669: [RFC]: Model Deprecation Policy

| 字段 | 值 |
| --- | --- |
| Issue | [#9669](https://github.com/vllm-project/vllm/issues/9669) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Model Deprecation Policy

### Issue 正文摘录

### Motivation. Usually, we accept model contribution from model vendors, as long as they can verify the model output is correct. When a new model is added into vLLM, vLLM maintainers will need to maintain the code, update it when necessary. However, we find that sometimes the model vendor might not be responsive, and the model can get obsolete and even be broken for new `transformers` versions. As stated in https://docs.vllm.ai/en/latest/models/supported_models.html#model-support-policy , some models are community-driven, and vLLM maintainers do not actively keep them up-to-date. Here, I want to go one step further: if a model is broken (cannot run directly with the latest `transformers` version), and we cannot hear from the model vendor for a period of time, then we will remove the model from vLLM. An example: the `xverse` model added by https://github.com/vllm-project/vllm/pull/3610 . the huggingface repo https://huggingface.co/xverse/XVERSE-7B-Chat/tree/main does not have any update in one year, and the tokenizer is broken in recent `transformers`, leading to an error similar to https://github.com/huggingface/transformers/issues/31789 . In fact, when I add `torch.compile` supp...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: Model Deprecation Policy RFC ### Motivation. Usually, we accept model contribution from model vendors, as long as they can verify the model output is correct. When a new model is added into vLLM, vLLM maintainers...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: and the model can get obsolete and even be broken for new `transformers` versions. As stated in https://docs.vllm.ai/en/latest/models/supported_models.html#model-support-policy , some models are community-driven, and vL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: for new `transformers` versions. As stated in https://docs.vllm.ai/en/latest/models/supported_models.html#model-support-policy , some models are community-driven, and vLLM maintainers do not actively keep them up-to-dat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
