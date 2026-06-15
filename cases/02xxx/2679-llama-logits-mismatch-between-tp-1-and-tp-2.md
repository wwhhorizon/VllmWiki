# vllm-project/vllm#2679: llama logits mismatch between TP=1 and TP=2

| 字段 | 值 |
| --- | --- |
| Issue | [#2679](https://github.com/vllm-project/vllm/issues/2679) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> llama logits mismatch between TP=1 and TP=2

### Issue 正文摘录

## Context Env: H800 * 2 GPU, NGC container, Latest Master branch Model: **Llama 7b** with vocab_size = 80k Just infer one token. ## Changes I Change this file, and simply add a print in function: `execute_model`: ``` vllm/worker/model_runner.py print(f"hidden_states = {hidden_states}") ``` ``` @torch.inference_mode() def execute_model( self, seq_group_metadata_list: Optional[List[SequenceGroupMetadata]], kv_caches: List[Tuple[torch.Tensor, torch.Tensor]], ) -> Optional[SamplerOutput]: input_tokens, input_positions, input_metadata, sampling_metadata, lora_requests, lora_mapping = ( self.prepare_input_tensors(seq_group_metadata_list)) if self.lora_config: self.set_active_loras(lora_requests, lora_mapping) # Execute the model. if input_metadata.use_cuda_graph: graph_batch_size = input_tokens.shape[0] model_executable = self.graph_runners[graph_batch_size] else: model_executable = self.model hidden_states = model_executable( input_ids=input_tokens, positions=input_positions, kv_caches=kv_caches, input_metadata=input_metadata, ) print(f"hidden_states = {hidden_states}") # Sample the next token. output = self.model.sample( hidden_states=hidden_states, sampling_metadata=sampling_metadat...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: .inference_mode() def execute_model( self, seq_group_metadata_list: Optional[List[SequenceGroupMetadata]], kv_caches: List[Tuple[torch.Tensor, torch.Tensor]], ) -> Optional[SamplerOutput]: input_tokens, input_positions,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: llama logits mismatch between TP=1 and TP=2 ## Context Env: H800 * 2 GPU, NGC container, Latest Master branch Model: **Llama 7b** with vocab_size = 80k Just infer one token. ## Changes I Change this file, and simply ad
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: llama logits mismatch between TP=1 and TP=2 ## Context Env: H800 * 2 GPU, NGC container, Latest Master branch Model: **Llama 7b** with vocab_size = 80k Just infer one token. ## Changes I Change this file, and simply add...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: llama logits mismatch between TP=1 and TP=2 ## Context Env: H800 * 2 GPU, NGC container, Latest Master branch Model: **Llama 7b** with vocab_size = 80k Just infer one token. ## Changes I Change this file, and simply add...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: input_tokens, input_positions, input_metadata, sampling_metadata, lora_requests, lora_mapping = ( self.prepare_input_tensors(seq_group_metadata_list)) if self.lora_config: self.set_active_loras(lora_requests, lora_mappi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
