# vllm-project/vllm#5093: [Bug]: The implementation of  DynamicNTKScalingRotaryEmbedding  may have errors.

| 字段 | 值 |
| --- | --- |
| Issue | [#5093](https://github.com/vllm-project/vllm/issues/5093) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The implementation of  DynamicNTKScalingRotaryEmbedding  may have errors.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` I noticed that the implementation of dynamic ntk recalculates the base parameter for all lengths, which is inconsistent with the implementation of transformers? ### 🐛 Describe the bug def _compute_cos_sin_cache(self) -> torch.Tensor: # NOTE(woosuk): self.max_position_embeddings is the original # maximum length before applying the rope scaling. # Thus, the maximum length after applying the rope scaling is # self.max_position_embeddings * self.scaling_factor. max_len = self.max_position_embeddings * self.scaling_factor base = self.base * ( (self.scaling_factor * max_len / self.max_position_embeddings) - (self.scaling_factor - 1))**(self.rotary_dim / (self.rotary_dim - 2)) inv_freq = self._compute_inv_freq(base) t = torch.arange(max_len, dtype=torch.float) freqs = torch.einsum("i,j -> ij", t, inv_freq) cos = freqs.cos() sin = freqs.sin() cache = torch.cat((cos, sin), dim=-1) return cache

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nv_freq = self._compute_inv_freq(base) t = torch.arange(max_len, dtype=torch.float) freqs = torch.einsum("i,j -> ij", t, inv_freq) cos = freqs.cos() sin = freqs.sin() cache = torch.cat((cos, sin), dim=-1) return cache
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: mplementation of DynamicNTKScalingRotaryEmbedding may have errors. bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` I noticed that the implementation of dynamic ntk recalculates t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
