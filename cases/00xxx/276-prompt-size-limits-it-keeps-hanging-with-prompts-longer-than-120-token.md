# vllm-project/vllm#276: Prompt size limits? It keeps hanging with prompts longer than 120 tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#276](https://github.com/vllm-project/vllm/issues/276) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Prompt size limits? It keeps hanging with prompts longer than 120 tokens

### Issue 正文摘录

Are there any prompt size limits? It seems that using more than 120 words make the model unresponsive. Check the following case. In the first try I used 112 words in prompt and worked just fine. ![Screenshot 2023-06-27 103239](https://github.com/vllm-project/vllm/assets/26122127/7b404d7f-55ce-4094-9d9a-6fd4e9c224d3) Then I tried increasing the prompt's size to 140 words and it just came unresponsive. and had to kill it. ![Screenshot 2023-06-27 105213](https://github.com/vllm-project/vllm/assets/26122127/dbbbc89d-870a-4101-8203-9118be2a3d5c) The same behavior is reproduced every time I try to give a prompt larger than 120 - 130 words. Probably this is why it doen't work with more complex chains (RetrievalQA) and LlamaIndex #233 Is there any idea?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: any prompt size limits? It seems that using more than 120 words make the model unresponsive. Check the following case. In the first try I used 112 words in prompt and worked just fine. ![Screenshot 2023-06-27 103239](ht...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ets/26122127/dbbbc89d-870a-4101-8203-9118be2a3d5c) The same behavior is reproduced every time I try to give a prompt larger than 120 - 130 words. Probably this is why it doen't work with more complex chains (RetrievalQA...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rds. Probably this is why it doen't work with more complex chains (RetrievalQA) and LlamaIndex #233 Is there any idea?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
