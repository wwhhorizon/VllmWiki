# vllm-project/vllm#34736: [Refactor]: Handle OOV Multimodal Tokens Generically

| 字段 | 值 |
| --- | --- |
| Issue | [#34736](https://github.com/vllm-project/vllm/issues/34736) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Refactor]: Handle OOV Multimodal Tokens Generically

### Issue 正文摘录

Currently we have flags that are set on a per model basis for out of vocabulary tokens that indicate whether or not the tokens should be squeezed out prior to getting the LLM embeddings. I think it would be a good idea to simplify this to be generic, so that: - We remove the `handle_oov_mm_token` flag - When we initialize the model, we directly check if any multimodal tokens are OOV (i.e., register an arch's mm token indices at init time and just check against the vocab size) - Log once if multimodal tokens are OOV - At inference time, if the model has OOV multimodal tokens, mask with zeros to avoid incorrect placeholder offsets where it's expected, e.g., for LoRA This will resolve https://github.com/vllm-project/vllm/issues/29166 and is a cleaner alternative to the fix that I opened [here](https://github.com/vllm-project/vllm/pull/32135), since it will avoid the extra flag + let us remove the current `handle_oov_mm_token` flag, as well as not have to worry about setting it for specific models in the future. If the cost of masking with zeros vs squeezing the IDs out is significant, we can also discuss what can be done there, but IMO it's worth trying to keep the offsets consistent...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Refactor]: Handle OOV Multimodal Tokens Generically documentation Currently we have flags that are set on a per model basis for out of vocabulary tokens that indicate whether or not the tokens should be squeezed out pr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: to keep the offsets consistent where possible to avoid complexity unless benchmarks prove otherwise, since the cost of the one embedding lookup will be low relative to the overall generation @DarkLight1337 @jeejeelee @N...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: oov_mm_token` flag, as well as not have to worry about setting it for specific models in the future. If the cost of masking with zeros vs squeezing the IDs out is significant, we can also discuss what can be done there,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l, we directly check if any multimodal tokens are OOV (i.e., register an arch's mm token indices at init time and just check against the vocab size) - Log once if multimodal tokens are OOV - At inference time, if the mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
