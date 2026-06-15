# vllm-project/vllm#17766: [Bug]: Logits processing with Lora is incorrect

| 字段 | 值 |
| --- | --- |
| Issue | [#17766](https://github.com/vllm-project/vllm/issues/17766) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Logits processing with Lora is incorrect

### Issue 正文摘录

### Your current environment V1. Logic error. ### 🐛 Describe the bug When we have mixed prompt and sampling in a batch (possible in V1), we can no longer use indices_padded = self.punica_wrapper.sampler_indices_padded to select from lora_logits of size [(lora_max+1*B, d_model] https://github.com/vllm-project/vllm/blob/8d84d836d17bdabe4c640021bc6f8bd11a546a44/vllm/lora/layers.py#L1142 But indices_padded is of size samples which is <= B. Hence the result would be incorrect or error out later in https://github.com/vllm-project/vllm/blob/8d84d836d17bdabe4c640021bc6f8bd11a546a44/vllm/lora/layers.py#L1152 due to broadcast mismatch. To fix, we probably need to add lora mapping for each token in the batch, say, batch_indices like https://github.com/vllm-project/vllm/blob/ba7703e659e21ea376c25b872c4a80a7c82804fe/vllm/lora/punica_wrapper/utils.py#L130 And the 2D flat indexing like https://github.com/iterationlab/monorepo/blob/7345300cc615de19fb54df261447c1356c8dd028/third_party/vllm/vllm/lora/punica_wrapper/utils.py#L133 And use that instead of `sampler_indices_padded` to indice the lora_logits. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, a...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: abe4c640021bc6f8bd11a546a44/vllm/lora/layers.py#L1152 due to broadcast mismatch. To fix, we probably need to add lora mapping for each token in the batch, say, batch_indices like https://github.com/vllm-project/vllm/blo...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: bdabe4c640021bc6f8bd11a546a44/vllm/lora/layers.py#L1152 due to broadcast mismatch. To fix, we probably need to add lora mapping for each token in the batch, say, batch_indices like https://github.com/vllm-project/vllm/b...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: y#L1152 due to broadcast mismatch. To fix, we probably need to add lora mapping for each token in the batch, say, batch_indices like https://github.com/vllm-project/vllm/blob/ba7703e659e21ea376c25b872c4a80a7c82804fe/vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: pler_indices_padded to select from lora_logits of size [(lora_max+1*B, d_model] https://github.com/vllm-project/vllm/blob/8d84d836d17bdabe4c640021bc6f8bd11a546a44/vllm/lora/layers.py#L1142 But indices_padded is of size...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Logits processing with Lora is incorrect bug;stale ### Your current environment V1. Logic error. ### 🐛 Describe the bug When we have mixed prompt and sampling in a batch (possible in V1), we can no longer use ind...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
