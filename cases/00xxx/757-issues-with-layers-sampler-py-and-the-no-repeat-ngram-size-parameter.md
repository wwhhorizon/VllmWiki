# vllm-project/vllm#757: Issues with layers/sampler.py and the no_repeat_ngram_size parameter

| 字段 | 值 |
| --- | --- |
| Issue | [#757](https://github.com/vllm-project/vllm/issues/757) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Issues with layers/sampler.py and the no_repeat_ngram_size parameter

### Issue 正文摘录

I'm adding no_repeat_ngram_size parameter and I have some problem with sampler.py. in transformers/generation/utils.py , my understanding order is model infer, (no_repeat processing: optional), temperature processing, topk processing, softmax. But in vllm, I found it seems like model infer, temperature processing, softmax, topk processing. Can you tell me why the order is different here or give me some advice to add no_repeat_ngram_size? transformers ``` outputs = self( **model_inputs, return_dict=True, output_attentions=output_attentions, output_hidden_states=output_hidden_states, ) if synced_gpus and this_peer_finished: continue # don't waste resources running the code we don't need next_token_logits = outputs.logits[:, -1, :] # pre-process distribution next_token_scores = logits_processor(input_ids, next_token_logits) next_token_scores = logits_warper(input_ids, next_token_scores) probs = nn.functional.softmax(next_token_scores, dim=-1) next_tokens = torch.multinomial(probs, num_samples=1).squeeze(1) ``` vllm ``` hidden_states = self.model(......) hidden_states = _prune_hidden_states(hidden_states, input_metadata) # Get the logits for the next tokens. logits = torch.matmul(hidd...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: t = torch.tensor(temperatures, dtype=logits.dtype, device=logits.device) # Use in-place division to avoid creating a new tensor. logits.div_(t.unsqueeze(dim=1)) # We use float32 for probabi
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: s model infer, (no_repeat processing: optional), temperature processing, topk processing, softmax. But in vllm, I found it seems like model infer, temperature processing, softmax, topk processing. Can you tell me why th...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .....) hidden_states = _prune_hidden_states(hidden_states, input_metadata) # Get the logits for the next tokens. logits = torch.matmul(hidden_states, embedding.t()) if embedding_bias is not None: logits += embedding_bia...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ler.py. in transformers/generation/utils.py , my understanding order is model infer, (no_repeat processing: optional), temperature processing, topk processing, softmax. But in vllm, I found it seems like model infer, te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
