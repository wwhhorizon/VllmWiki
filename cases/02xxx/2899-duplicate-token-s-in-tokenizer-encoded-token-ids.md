# vllm-project/vllm#2899: Duplicate Token `<s>` in Tokenizer Encoded Token ids

| 字段 | 值 |
| --- | --- |
| Issue | [#2899](https://github.com/vllm-project/vllm/issues/2899) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Duplicate Token `<s>` in Tokenizer Encoded Token ids

### Issue 正文摘录

When working on tokenizer result for `llama-2-7b-chat-hf` model, I noticed that the `prompt_token_ids` generated in [this place](https://github.com/vllm-project/vllm/blob/5f08050d8d0bfcdaced0fe706cdfc9e311e0f263/vllm/engine/llm_engine.py#L385C13-L385C29) would generate an extra token ` ` in the beginning of the sentence. For example for the follow prompt ` [INST] what is the color of the snow? [/INST]` , hf tokenizer can directly tokenize it to ``` [' ', '▁[', 'INST', ']', '▁what', '▁is', '▁the', '▁color', '▁of', '▁the', '▁snow', '?', '▁[', '/', 'INST', ']'] [1, 518, 25580, 29962, 825, 338, 278, 2927, 310, 278, 15007, 29973, 518, 29914, 25580, 29962] ``` but for the very same prompt vllm would generate tokenized prompt ids as follows ``` [1, 1, 518, 25580, 29962, 825, 338, 278, 2927, 310, 278, 15007, 29973, 518, 29914, 25580, 29962] ``` which has an extra token `1`, aka ` ` in the beginning. Looking forward to have someone help me confirm if this is designated behaviour or caused by some of the model options.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Tokenizer Encoded Token ids usage When working on tokenizer result for `llama-2-7b-chat-hf` model, I noticed that the `prompt_token_ids` generated in [this place](https://github.com/vllm-project/vllm/blob/5f08050d8d0bfc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
