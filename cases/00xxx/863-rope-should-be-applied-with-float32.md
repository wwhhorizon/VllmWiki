# vllm-project/vllm#863: RoPE should be applied with float32

| 字段 | 值 |
| --- | --- |
| Issue | [#863](https://github.com/vllm-project/vllm/issues/863) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RoPE should be applied with float32

### Issue 正文摘录

It seems that RoPE(sin,cos) should be stored and applied in fp32 and then casted back to fp16/bf16 https://github.com/vllm-project/vllm/blob/791d79de3261402fae1b9d0b1650655071a68095/vllm/model_executor/layers/attention.py#L273 Reference implementation from Llama 2 / Code Llama: ```python def precompute_freqs_cis(dim: int, end: int, theta: float = 10000.0): freqs = 1.0 / (theta ** (torch.arange(0, dim, 2)[: (dim // 2)].float() / dim)) t = torch.arange(end, device=freqs.device, dtype=torch.float32) # type: ignore freqs = torch.outer(t, freqs) # type: ignore freqs_cis = torch.polar(torch.ones_like(freqs), freqs) # complex64 return freqs_cis def apply_rotary_emb( xq: torch.Tensor, xk: torch.Tensor, freqs_cis: torch.Tensor, ) -> Tuple[torch.Tensor, torch.Tensor]: xq_ = torch.view_as_complex(xq.float().reshape(*xq.shape[:-1], -1, 2)) xk_ = torch.view_as_complex(xk.float().reshape(*xk.shape[:-1], -1, 2)) freqs_cis = reshape_for_broadcast(freqs_cis, xq_) xq_out = torch.view_as_real(xq_ * freqs_cis).flatten(3) xk_out = torch.view_as_real(xk_ * freqs_cis).flatten(3) return xq_out.type_as(xq), xk_out.type_as(xk) ```

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: RoPE should be applied with float32 feature request It seems that RoPE(sin,cos) should be stored and applied in fp32 and then casted back to fp16/bf16 https://github.com/vllm-project/vllm/blob/791d79de3261402fae1b9d0b16...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: com/vllm-project/vllm/blob/791d79de3261402fae1b9d0b1650655071a68095/vllm/model_executor/layers/attention.py#L273 Reference implementation from Llama 2 / Code Llama: ```python def precompute_freqs_cis(dim: int, end: int,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: mplementation from Llama 2 / Code Llama: ```python def precompute_freqs_cis(dim: int, end: int, theta: float = 10000.0): freqs = 1.0 / (theta ** (torch.arange(0, dim, 2)[: (dim // 2)].float() / dim)) t = torch.arange(en...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: RoPE should be applied with float32 feature request It seems that RoPE(sin,cos) should be stored and applied in fp32 and then casted back to fp16/bf16 https://github.com/vllm-project/vllm/blob/791d79de3261402fae1b9d0b16...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
