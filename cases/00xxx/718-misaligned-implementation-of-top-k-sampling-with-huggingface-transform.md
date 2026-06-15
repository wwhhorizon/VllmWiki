# vllm-project/vllm#718: Misaligned implementation of top_k sampling with huggingface/transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#718](https://github.com/vllm-project/vllm/issues/718) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Misaligned implementation of top_k sampling with huggingface/transformers

### Issue 正文摘录

If we want to do a top_k sampling in vllm by setting top_k>0: 1. vllm computes softmax of logits firstly 2. then does top_k truncation afterwards to obtain the final probability distribution ( which is NOT normalized ). 3. then does sample by torch.multinomial operation. If we want to do a top_k sampling in huggingface/transformers by setting top_k>0 and do_sampling=True. 1. transformers computes topk truncation with logits firstly. 2. then computes the softmax of the truncated logits ( which is normalized ). 3. then does sample by torch.multinomial operation. This difference will result in different top_k sampling generated tokens even the same random seed was set in vllm and transformers. I wonder whether it is a bug of vllm or different styles of top_k sampling implementations. vllm: vllm/model_executor/layers/sampler.py ``` # We use float32 for probabilities and log probabilities. # Compute the probabilities. probs = torch.softmax(logits, dim=-1, dtype=torch.float) # Compute the log probabilities (before applying top-p and top-k). logprobs = torch.log(probs) # Apply top-p and top-k truncation. top_ps, top_ks = _get_top_p_top_k(input_metadata, self.vocab_size) assert len(top_ps...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ations. vllm: vllm/model_executor/layers/sampler.py ``` # We use float32 for probabilities and log probabilities. # Compute the probabilities. probs = torch.softmax(logits, dim=-1, dtype=torch.float) # Compute the log p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Misaligned implementation of top_k sampling with huggingface/transformers If we want to do a top_k sampling in vllm by setting top_k>0: 1. vllm computes softmax of logits firstly 2. then does top_k truncation afterwards...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: rmers by setting top_k>0 and do_sampling=True. 1. transformers computes topk truncation with logits firstly. 2. then computes the softmax of the truncated logits ( which is normalized ). 3. then does sample by torch.mul...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: -p and top-k truncation. top_ps, top_ks = _get_top_p_top_k(input_metadata, self.vocab_size) assert len(top_ps) == len(top_ks) == probs.shape[0] do_top_p = any(p torch.FloatTensor: top_k = min(self.top_k, scores.size(-1)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
