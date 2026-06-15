# vllm-project/vllm#507: How to get seq_len in Atten

| 字段 | 值 |
| --- | --- |
| Issue | [#507](https://github.com/vllm-project/vllm/issues/507) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to get seq_len in Atten

### Issue 正文摘录

``` def forward( self, positions: torch.Tensor, hidden_states: torch.Tensor, kv_cache: KVCache, input_metadata: InputMetadata, cache_event: Optional[torch.cuda.Event], ) -> torch.Tensor: qkv, _ = self.W_pack(hidden_states) q, k, v = qkv.chunk(chunks=3, dim=-1) k_cache, v_cache = kv_cache # How to get seq_len here? attn_output = self.attn( positions, q, k, v, k_cache, v_cache, input_metadata, cache_event, seq_len=512 ) output, _ = self.o_proj(attn_output) return output ``` How to get seq_len at Atten layer. (I printed shapes of each tensor but can't really know how to according them to torch side), Can anyone help?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: input_metadata: InputMetadata, cache_event: Optional[torch.cuda.Event], ) -> torch.Tensor: qkv, _ = self.W_pack(hidden_states) q, k, v = qkv.chunk(chunks=3, dim=-1) k_cache, v_cache = kv_cache # How to get seq_len here?...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: hidden_states: torch.Tensor, kv_cache: KVCache, input_metadata: InputMetadata, cache_event: Optional[torch.cuda.Event], ) -> torch.Tensor: qkv, _ = self.W_pack(hidden_states) q, k, v = qkv.chunk(chunks=3, dim=-1) k_cach...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
