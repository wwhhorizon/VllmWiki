# vllm-project/vllm#416: [Feature Request] Support input embedding in `LLM.generate()`

| 字段 | 值 |
| --- | --- |
| Issue | [#416](https://github.com/vllm-project/vllm/issues/416) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature Request] Support input embedding in `LLM.generate()`

### Issue 正文摘录

Hi, I am using llm as part of a multimodal model, so the model needs to pass `input embedding tensor` directly to generate, and also need to access the language model's `embed_tokens` member to fist calculate the embedding, and then processed, finnaly send to `generate`, demo in the following code : ``` inputs_embeds = self.language_model.get_input_embeddings()(input_ids) prefix_embeds = inputs_embeds[:, :self.offset, :] postfix_embeds = inputs_embeds[:, self.offset:, :] inputs_embeds = torch.cat([prefix_embeds, language_model_inputs, postfix_embeds], dim=1) ..... attention_mask = torch.cat([prefix_mask, vision_mask, postfix_mask], dim=-1) outputs = self.language_model.generate( inputs_embeds=inputs_embeds, attention_mask=attention_mask, generation_config=generation_config, **generate_kwargs, ) ``` I read the vllm code, and it seems that I need to add two interfaces in vllm, one is `LLM.get_input_embeddings`, another one is ` LLM.generate(inputs_embeds=inputs_embeds, ...) ` Do you think this will work? And would you consider support this feature?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ding in `LLM.generate()` feature request Hi, I am using llm as part of a multimodal model, so the model needs to pass `input embedding tensor` directly to generate, and also need to access the language model's `embed_to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature Request] Support input embedding in `LLM.generate()` feature request Hi, I am using llm as part of a multimodal model, so the model needs to pass `input embedding tensor` directly to generate, and also need to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
