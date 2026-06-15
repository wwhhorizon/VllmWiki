# vllm-project/vllm#2816: VLLM Multi-Lora with embed_tokens and lm_head in adapter weights 

| 字段 | 值 |
| --- | --- |
| Issue | [#2816](https://github.com/vllm-project/vllm/issues/2816) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> VLLM Multi-Lora with embed_tokens and lm_head in adapter weights 

### Issue 正文摘录

Hi there! I've encountered an issue with the `adatpter_model.safetensors` in my project, and I'm seeking guidance on how to handle `lm_head` and `embed_tokens` within the specified modules. Here's the current state: ``` ['base_model.model.lm_head.weight', 'base_model.model.model.embed_tokens.weight', 'base_model.model.model.layers.0.self_attn.k_proj.lora_A.weight', 'base_model.model.model.layers.0.self_attn.k_proj.lora_B.weight', 'base_model.model.model.layers.0.self_attn.o_proj.lora_A.weight', 'base_model.model.model.layers.0.self_attn.o_proj.lora_B.weight', ...] ``` Firstly, in [vllm/lora/utils.py](https://github.com/vllm-project/vllm/blob/0e163fce18594c7e29dc5a143dd6b33d213fcbf3/vllm/lora/utils.py#L33), modifications are needed to work with `lm_head` and `embed_tokens`. My question is, what should be the appropriate name for the new module? For instance, from `base_model.model.model.layers.0.self_attn.k_proj.lora_A.weight`, we extract `model.layers.0.self_attn.k_proj`. What should I use for `base_model.model.lm_head.weight` and `base_model.model.model.embed_tokens.weight`? Are `model.lm_head` and `model.embed_tokens` suitable, or do you have alternative suggestions? Additionall...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ing guidance on how to handle `lm_head` and `embed_tokens` within the specified modules. Here's the current state: ``` ['base_model.model.lm_head.weight', 'base_model.model.model.embed_tokens.weight', 'base_model.model....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: r weights stale Hi there! I've encountered an issue with the `adatpter_model.safetensors` in my project, and I'm seeking guidance on how to handle `lm_head` and `embed_tokens` within the specified modules. Here's the cu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: VLLM Multi-Lora with embed_tokens and lm_head in adapter weights stale Hi there! I've encountered an issue with the `adatpter_model.safetensors` in my project, and I'm seeking guidance on how to handle `lm_head` and `em...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
