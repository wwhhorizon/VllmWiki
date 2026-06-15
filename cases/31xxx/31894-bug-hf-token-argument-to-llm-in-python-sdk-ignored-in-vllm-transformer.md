# vllm-project/vllm#31894: [Bug] `hf_token` argument to `LLM` in Python SDK ignored in `vllm.transformer_utils.config`

| 字段 | 值 |
| --- | --- |
| Issue | [#31894](https://github.com/vllm-project/vllm/issues/31894) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] `hf_token` argument to `LLM` in Python SDK ignored in `vllm.transformer_utils.config`

### Issue 正文摘录

There is a bug in `vllm.transformer_utils.config` in that it ignores the `hf_token` argument provided to the `LLM` instance. See: https://github.com/vllm-project/vllm/blob/d111bc53ad2fbb5f28671019d21f5f753436e46d/vllm/transformers_utils/config.py#L140 This means that only environment variables are loaded when calling the HuggingFace API to load a models configuration (which for some gated models, for example, can result in the model failing to load since the config itself requires an `hf_token`). It seems like an easy fix as far as I can tell: An additional line on `vllm.v1.engine.llm_engine` when calling `maybe_override_with_speculators` to pass in the `hf_token`. I'd be happy to contribute the PR

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug] `hf_token` argument to `LLM` in Python SDK ignored in `vllm.transformer_utils.config` bug There is a bug in `vllm.transformer_utils.config` in that it ignores the `hf_token` argument provided to the `LLM` instance...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
