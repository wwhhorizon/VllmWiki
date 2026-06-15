# vllm-project/vllm#1357: Pre-PR Feedback: Token Filtering API

| 字段 | 值 |
| --- | --- |
| Issue | [#1357](https://github.com/vllm-project/vllm/issues/1357) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Pre-PR Feedback: Token Filtering API

### Issue 正文摘录

Hello. I'm looking to contribute a prefix token filtering mechanism to vLLM, to allow functionality similar to huggingface's ``` prefix_allowed_tokens_fn: Callable[[int, torch.Tensor], List[int]] ``` parameter when calling generate(). Is this something that the team will be willing to consider accepting if I submit a PR? I thought about adding an optional function field to SamplingParams and using it in the Sampler module if it was provided, but prefer feedback from the team before I dive inside. For some context - I developed a library - [LM Format Enforcer](https://pypi.org/project/lm-format-enforcer) that uses this API (and nothing else, contrary to similar libraries) to allow forcing JSON / regular expression output from the LLM, and opening this API will allow easy integration of it into vLLM.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: fix token filtering mechanism to vLLM, to allow functionality similar to huggingface's ``` prefix_allowed_tokens_fn: Callable[[int, torch.Tensor], List[int]] ``` parameter when calling generate(). Is this something that...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s this API (and nothing else, contrary to similar libraries) to allow forcing JSON / regular expression output from the LLM, and opening this API will allow easy integration of it into vLLM.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ing API Hello. I'm looking to contribute a prefix token filtering mechanism to vLLM, to allow functionality similar to huggingface's ``` prefix_allowed_tokens_fn: Callable[[int, torch.Tensor], List[int]] ``` parameter w...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ://pypi.org/project/lm-format-enforcer) that uses this API (and nothing else, contrary to similar libraries) to allow forcing JSON / regular expression output from the LLM, and opening this API will allow easy integrati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
