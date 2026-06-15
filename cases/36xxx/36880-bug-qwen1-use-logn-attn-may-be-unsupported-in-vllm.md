# vllm-project/vllm#36880: [Bug]: Qwen1 use_logn_attn may be unsupported in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#36880](https://github.com/vllm-project/vllm/issues/36880) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen1 use_logn_attn may be unsupported in vLLM

### Issue 正文摘录

### Your current environment None ### 🐛 Describe the bug It looks like Qwen1's `use_logn_attn` behavior may be unsupported in vLLM. Official Qwen1 configs (for example `Qwen-7B`) enable: ```json "use_logn_attn": true ``` and the original Qwen implementation applies an extra long-context query scaling when the attention length exceeds the configured seq_length: ``` key_size = key[0].size(2) if self.use_cache_quantization else key.size(1) if key_size > self.seq_length and self.use_logn_attn and not self.training: logn_tensor = self.logn_tensor[:, seq_start:seq_end, :, :].type_as(query) query = query * logn_tensor.expand_as(query) ``` From computation-graph inspection: - the Transformers graph for official Qwen-7B with a long input (key_size > seq_length) clearly contains: - ...attn_buffers_logn_tensor_ - query = query * logn_tensor.expand_as(query) - the vLLM graph for the same model contains: - positions - rotary cache - torch.ops.vllm.unified_attention_with_output(...) - but I could not find any corresponding logn_attn / logn_tensor path I may be missing something on the vLLM side. It could be that vLLM does not hit the same `key_size > seq_length` path as the original Qwen implem...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen1 use_logn_attn may be unsupported in vLLM bug ### Your current environment None ### 🐛 Describe the bug It looks like Qwen1's `use_logn_attn` behavior may be unsupported in vLLM. Official Qwen1 configs (for e
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: context scaling is already handled implicitly inside the Qwen1 attention backend. If so, a clarification would be very helpful. Otherwise, this seems to suggest that `use_logn_attn` is currently unsupported for Qwen1. #...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: like Qwen1's `use_logn_attn` behavior may be unsupported in vLLM. Official Qwen1 configs (for example `Qwen-7B`) enable: ```json "use_logn_attn": true ``` and the original Qwen implementation applies an extra long-conte...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: configured seq_length: ``` key_size = key[0].size(2) if self.use_cache_quantization else key.size(1) if key_size > self.seq_length and self.use_logn_attn and not self.training: logn_tensor = self.logn_tensor[:, seq_star...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n1. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
