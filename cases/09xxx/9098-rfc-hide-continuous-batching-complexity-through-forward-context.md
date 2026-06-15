# vllm-project/vllm#9098: [RFC]: hide continuous batching complexity through forward context

| 字段 | 值 |
| --- | --- |
| Issue | [#9098](https://github.com/vllm-project/vllm/issues/9098) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: hide continuous batching complexity through forward context

### Issue 正文摘录

### Motivation. take a look at the current llama forward computation logic: ```python class LlamaMLP(nn.Module): def forward(self, x): gate_up, _ = self.gate_up_proj(x) x = self.act_fn(gate_up) x, _ = self.down_proj(x) return x class LlamaAttention(nn.Module): def forward( self, positions: torch.Tensor, hidden_states: torch.Tensor, kv_cache: torch.Tensor, attn_metadata: AttentionMetadata, ) -> torch.Tensor: qkv, _ = self.qkv_proj(hidden_states) q, k, v = qkv.split([self.q_size, self.kv_size, self.kv_size], dim=-1) q, k = self.rotary_emb(positions, q, k) attn_output = self.attn(q, k, v, kv_cache, attn_metadata) output, _ = self.o_proj(attn_output) return output class LlamaDecoderLayer(nn.Module): def forward( self, positions: torch.Tensor, hidden_states: torch.Tensor, kv_cache: torch.Tensor, attn_metadata: AttentionMetadata, residual: Optional[torch.Tensor], ) -> Tuple[torch.Tensor, torch.Tensor]: # Self Attention if residual is None: residual = hidden_states hidden_states = self.input_layernorm(hidden_states) else: hidden_states, residual = self.input_layernorm( hidden_states, residual) hidden_states = self.self_attn( positions=positions, hidden_states=hidden_states, kv_cache=kv_c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: gh forward context RFC;stale ### Motivation. take a look at the current llama forward computation logic: ```python class LlamaMLP(nn.Module): def forward(self, x): gate_up, _ = self.gate_up_proj(x) x = self.act_fn(gate_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: idden_states: torch.Tensor, kv_cache: torch.Tensor, attn_metadata: AttentionMetadata, ) -> torch.Tensor: qkv, _ = self.qkv_proj(hidden_states) q, k, v = qkv.split([self.q_size, self.kv_size, self.kv_size], dim=-1) q, k...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: hide continuous batching complexity through forward context RFC;stale ### Motivation. take a look at the current llama forward computation logic: ```python class LlamaMLP(nn.Module): def forward(self, x): gate_up...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ttention metadata for different layers (e.g. Gemma 2) - optimized `torch.compile` logic, where we want to hide the complexity of attention layer from the compiler Therefore, I'm considering to hide the complexity of con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
