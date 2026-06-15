# vllm-project/vllm#8323: Do vLLM support `input_embeds` as input while using LLama?

| 字段 | 值 |
| --- | --- |
| Issue | [#8323](https://github.com/vllm-project/vllm/issues/8323) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Do vLLM support `input_embeds` as input while using LLama?

### Issue 正文摘录

Can we directly pass the input_embeds to the generate function? Just like the following used in the pytorch transformers ``` generated_ids = self.model.generate( inputs_embeds=input_token_embedding, do_sample=True, max_length=max_length, pad_token_id=self.pad_token_id, eos_token_id=self.eos_target_id, temperature=temperature, top_k=top_k, top_p=top_p, repetition_penalty=repeat_penalty, min_new_tokens=50, ) ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Do vLLM support `input_embeds` as input while using LLama? bug;unstale Can we directly pass the input_embeds to the generate function? Just like the following used in the pytorch transformers ``` generated_ids = self.mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Do vLLM support `input_embeds` as input while using LLama? bug;unstale Can we directly pass the input_embeds to the generate function? Just like the following used in the pytorch transformers ``` generated_ids = self.mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
