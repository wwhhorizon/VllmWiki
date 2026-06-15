# vllm-project/vllm#1675: How to print each token generation time?

| 字段 | 值 |
| --- | --- |
| Issue | [#1675](https://github.com/vllm-project/vllm/issues/1675) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to print each token generation time?

### Issue 正文摘录

If I give a prompt, I want to print the prefill accurate time and the second token accurate time and third token accurate time and so on. how to achieve that. My thought is below. Change the [OPTForCausalLM forward](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/opt.py#L291-#L295) ``` def forward( self, input_ids: torch.Tensor, positions: torch.Tensor, kv_caches: List[KVCache], input_metadata: InputMetadata, cache_events: Optional[List[torch.cuda.Event]], ) -> SamplerOutput: start = time.time() hidden_states = self.model(input_ids, positions, kv_caches, input_metadata, cache_events) next_tokens = self.sampler(self.lm_head_weight, hidden_states, input_metadata) duation = time.time() - start print(f"duration:{duration}") return next_tokens ```

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: input_metadata: InputMetadata, cache_events: Optional[List[torch.cuda.Event]], ) -> SamplerOutput: start = time.time() hidden_states = self.model(input_ids, positions, kv_caches, input_metadata, cache_events) next_token...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: positions: torch.Tensor, kv_caches: List[KVCache], input_metadata: InputMetadata, cache_events: Optional[List[torch.cuda.Event]], ) -> SamplerOutput: start = time.time() hidden_states = self.model(input_ids, positions,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ForCausalLM forward](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/opt.py#L291-#L295) ``` def forward( self, input_ids: torch.Tensor, positions: torch.Tensor, kv_caches: List[KVCache], input_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rint each token generation time? If I give a prompt, I want to print the prefill accurate time and the second token accurate time and third token accurate time and so on. how to achieve that. My thought is below. Change...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
