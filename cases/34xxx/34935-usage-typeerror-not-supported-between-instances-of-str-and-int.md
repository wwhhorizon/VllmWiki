# vllm-project/vllm#34935: [Usage]: TypeError: '>' not supported between instances of 'str' and 'int'

| 字段 | 值 |
| --- | --- |
| Issue | [#34935](https://github.com/vllm-project/vllm/issues/34935) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: TypeError: '>' not supported between instances of 'str' and 'int'

### Issue 正文摘录

If you're encountering a `TypeError: '>' not supported between instances of 'str' and 'int'` with the `transformers` tokenizer in `vllm.chat()`, this issue likely stems from `transformers` versions 5.x. I'm not sure this change was applied continually, Transformers tokenizer's `return_dict` argument was changed to `True` by default in [these versions](https://github.com/huggingface/transformers/releases/tag/v5.0.0rc3). - [Tokenizer] Change default value of return_dict to True in doc string for apply_chat_template by @kashif in [#43223](https://github.com/huggingface/transformers/pull/43223) To resolve this, you can add `chat_template_kwargs` to the `chat` function, with `return_dict` to `False` as shown below: ``` vllm.chat( ..., chat_template_kwargs={'return_dict': False}, ) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tokenizer in `vllm.chat()`, this issue likely stems from `transformers` versions 5.x. I'm not sure this change was applied continually, Transformers tokenizer's `return_dict` argument was changed to `True` by default in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: `chat_template_kwargs` to the `chat` function, with `return_dict` to `False` as shown below: ``` vllm.chat( ..., chat_template_kwargs={'return_dict': False}, ) ``` ### Before submitting a new issue... - [x] Make sure yo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: was changed to `True` by default in [these versions](https://github.com/huggingface/transformers/releases/tag/v5.0.0rc3). - [Tokenizer] Change default value of return_dict to True in doc string for apply_chat_template b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
