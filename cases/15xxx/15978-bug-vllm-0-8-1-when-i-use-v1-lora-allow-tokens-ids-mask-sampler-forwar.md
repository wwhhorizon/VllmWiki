# vllm-project/vllm#15978: [Bug]: vllm==0.8.1, when I use : v1 + lora + allow_tokens_ids_mask,  Sampler.forward.apply_allowed_token_ids. func,  sampling_metadata.allowed_token_ids_mask.shape not match logits.shape

| 字段 | 值 |
| --- | --- |
| Issue | [#15978](https://github.com/vllm-project/vllm/issues/15978) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm==0.8.1, when I use : v1 + lora + allow_tokens_ids_mask,  Sampler.forward.apply_allowed_token_ids. func,  sampling_metadata.allowed_token_ids_mask.shape not match logits.shape

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` ## vllm/v1/sample/sampler.py def apply_allowed_token_ids( self, logits: torch.Tensor, sampling_metadata: SamplingMetadata, ) -> torch.Tensor: if sampling_metadata.allowed_token_ids_mask is not None: logits.masked_fill_(sampling_metadata.allowed_token_ids_mask, float("-inf")) return logits ------------- logits.shape = [num_req, vocab_size+lora_config.lora_extra_vocab_size], then allowed_token_ids_mask.shape = [num_req, vocab_size] ``` ``` ## vllm/model_executor/models/llama.py class LlamaFotCausalLM: def __init__(): if lora_config: self.unpadded_vocab_size += lora_config.lora_extra_vocab_size ......... logits.shape==self.unpadded_vocab_size but, ## vllm/v1/worker/gpu_input_batch.py class InputBatch: def add_request(): if sampling_params.allowed_token_ids: self.has_allowed_token_ids.add(req_id) if self.allowed_token_ids_mask_cpu_tensor is None: # Lazy allocation for this tensor, which can be large. # False means we don't fill with -inf. self.allowed_token_ids_mask = torch.zeros(self.max_num_reqs, self.vocab_size, dtype=torch.bool, device=self.device) self.allowed_token_ids_mask_cpu_tensor = torch.zeros( self.max_num_reqs, self....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ts ------------- logits.shape = [num_req, vocab_size+lora_config.lora_extra_vocab_size], then allowed_token_ids_mask.shape = [num_req, vocab_size] ``` ``` ## vllm/model_executor/models/llama.py class LlamaFotCausalLM: d...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: kens_ids_mask, Sampler.forward.apply_allowed_token_ids. func, sampling_metadata.allowed_token_ids_mask.shape not match logits.shape bug;stale ### Your current environment ### 🐛 Describe the bug ``` ## vllm/v1/sample/sam...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ampling_metadata.allowed_token_ids_mask.shape not match logits.shape bug;stale ### Your current environment ### 🐛 Describe the bug ``` ## vllm/v1/sample/sampler.py def apply_allowed_token_ids( self, logits: torch.Tensor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: lf.vocab_size, dtype=torch.bool, device=self.device) self.allowed_token_ids_mask_cpu_tensor = torch.zeros( self.max_num_reqs,
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
