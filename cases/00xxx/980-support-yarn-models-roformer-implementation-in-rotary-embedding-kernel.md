# vllm-project/vllm#980: Support YaRN models (RoFormer implementation in rotary_embedding kernel)

| 字段 | 值 |
| --- | --- |
| Issue | [#980](https://github.com/vllm-project/vllm/issues/980) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support YaRN models (RoFormer implementation in rotary_embedding kernel)

### Issue 正文摘录

The YaRN model with a context size of 64k and 128k was recently released and pre-trained by people from Nous Research and EleutherAI. It uses the RoFormer type of embeddings that seem different from GPT-NeoX and GPT-J. It is based on the LLaMa 2 model, so support is mostly there, just need some small adjustments. The original [YaRN module](https://huggingface.co/conceptofmind/Yarn-Llama-2-13b-128k/blob/main/modeling_llama_together_yarn.py#L116) uses the [flash attention rotary embedding](https://github.com/Dao-AILab/flash-attention/blob/a1576ad1e887c11f4b76f42e9dfaceeb6369cdb8/csrc/rotary/rotary_cuda.cu#L9) implementation and seems similar in functionality. You may also be interested in the original RoFormer implementation from [Huggingface](https://github.com/huggingface/transformers/blob/df04959e5542d41b269f96305d82c62287350cee/src/transformers/models/roformer/modeling_roformer.py#L319). Models catalog: https://huggingface.co/NousResearch/Yarn-Llama-2-7b-64k https://huggingface.co/NousResearch/Yarn-Llama-2-7b-128k https://huggingface.co/NousResearch/Yarn-Llama-2-13b-64k https://huggingface.co/NousResearch/Yarn-Llama-2-13b-128k

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: k and 128k was recently released and pre-trained by people from Nous Research and EleutherAI. It uses the RoFormer type of embeddings that seem different from GPT-NeoX and GPT-J. It is based on the LLaMa 2 model, so sup...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Support YaRN models (RoFormer implementation in rotary_embedding kernel) The YaRN model with a context size of 64k and 128k was recently released and pre-trained by people from Nous Research and EleutherAI. It uses the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ama-2-13b-128k/blob/main/modeling_llama_together_yarn.py#L116) uses the [flash attention rotary embedding](https://github.com/Dao-AILab/flash-attention/blob/a1576ad1e887c11f4b76f42e9dfaceeb6369cdb8/csrc/rotary/rotary_cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
