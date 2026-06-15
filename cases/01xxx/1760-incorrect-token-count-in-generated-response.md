# vllm-project/vllm#1760: Incorrect Token Count in Generated Response

| 字段 | 值 |
| --- | --- |
| Issue | [#1760](https://github.com/vllm-project/vllm/issues/1760) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Incorrect Token Count in Generated Response

### Issue 正文摘录

**Description:** I have identified a discrepancy in the token count when generating responses using the VLLM withh llama 2 model. When providing a question with a specific max_tokens value, the returned response includes a completion token equal to the specified max_tokens initially set. However, when attempting to count tokens in the text provided in the response using the Hugging Face tokenizer (len(tokenizer.encode(response))), the result exceeds the specified max_tokens (Sometimes, we observe an addition of more than 80 tokens.). This behavior is consistent across both LLama 2 and Zephyr models. **Steps to Reproduce:** 1. Provide a question to the model with a specific max_tokens value. 2. Retrieve the generated response. 3. Use the Hugging Face tokenizer to count tokens in the response (len(tokenizer.encode(response))). 4. Observe that the token count exceeds the initially set max_tokens. **Expected Behavior:** The token count in the response should match the specified max_tokens value. **Environment:** - Model: LLama 2 / Zephyr - Hugging Face Tokenizer

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: epancy in the token count when generating responses using the VLLM withh llama 2 model. When providing a question with a specific max_tokens value, the returned response includes a completion token equal to the specifie...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ehavior is consistent across both LLama 2 and Zephyr models. **Steps to Reproduce:** 1. Provide a question to the model with a specific max_tokens value. 2. Retrieve the generated response. 3. Use the Hugging Face token...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: using the VLLM withh llama 2 model. When providing a question with a specific max_tokens value, the returned response includes a completion token equal to the specified max_tokens initially set. However, when attempting...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
