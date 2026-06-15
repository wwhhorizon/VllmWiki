# vllm-project/vllm#6283: [Misc]: About Phi3 Rotary Embedding Implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#6283](https://github.com/vllm-project/vllm/issues/6283) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: About Phi3 Rotary Embedding Implementation

### Issue 正文摘录

### Anything you want to discuss about vllm. https://github.com/vllm-project/vllm/blob/d3a245138acb358c7e1e5c5dcf4dcb3c2b48c8ff/vllm/model_executor/layers/rotary_embedding.py#L594-L595 When we're in decode stage and position ids are given ```python positions = torch.LongTensor([0, 5000, 1, 10000]) long_prompt_offset = (torch.any(positions > k).float() * torch.full_like(positions, k)).long() long_prompt_offset >>> [4096, 4096, 4096, 4096] ``` should it be like [0, 4096, 0, 4096]? However, inspecting original phi3 code (https://huggingface.co/microsoft/Phi-3-vision-128k-instruct/blob/f998a184b56bf0399b3af85c50b20ec0d5688f5f/modeling_phi3_v.py#L140-L171) ```python @torch.no_grad() def forward(self, x, position_ids, seq_len=None): seq_len = torch.max(position_ids) + 1 if seq_len > self.original_max_position_embeddings: ext_factors = torch.tensor(self.long_factor, dtype=torch.float32, device=x.device) else: ext_factors = torch.tensor(self.short_factor, dtype=torch.float32, device=x.device) ``` it applies same "long_factor" if there's at least one long input in a batch. I think it's bit strange. Same input will produce different embedding result if they're in different batch. is it a in...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ax_position_embeddings: ext_factors = torch.tensor(self.long_factor, dtype=torch.float32, device=x.device) else: ext_factors = torch.tensor(self.short_factor, dtype=torch.float32, device=x.device) ``` it applies same "l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: com/vllm-project/vllm/blob/d3a245138acb358c7e1e5c5dcf4dcb3c2b48c8ff/vllm/model_executor/layers/rotary_embedding.py#L594-L595 When we're in decode stage and position ids are given ```python positions = torch.LongTensor([...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: torch.tensor(self.long_factor, dtype=torch.float32, device=x.device) else: ext_factors = torch.tensor(self.short_factor, dtype=torch.float32, device=x.device) ``` it applies same "long_factor" if there's at least one lo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: /vllm/model_executor/layers/rotary_embedding.py#L594-L595 When we're in decode stage and position ids are given ```python positions = torch.LongTensor([0, 5000, 1, 10000]) long_prompt_offset = (torch.any(positions > k)....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
