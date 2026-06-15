# vllm-project/vllm#14495: [Feature]: num of LoRAs requested by the batch is larger than num lora slots

| 字段 | 值 |
| --- | --- |
| Issue | [#14495](https://github.com/vllm-project/vllm/issues/14495) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: num of LoRAs requested by the batch is larger than num lora slots

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In the below code: def activate_adapter( self, lora_id: int, ) -> bool: """Move LoRA into a GPU buffer to be used in the forward pass.""" if lora_id in self._active_adapters: return False first_free_slot = next( ((i, lora_id) for i, lora_id in enumerate(self.lora_index_to_id) if lora_id is None), None) if first_free_slot is None: raise ValueError("No free lora slots") If a batch contains 3 requests, and LoRa1, LoRa2 and LoRa3 are required respectively. But there are only 2 lora slots, this will raise an error. I wonder if vllm team has a plan to fix this? By taking measures such as denying the request to be added to the current batch. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Feature]: num of LoRAs requested by the batch is larger than num lora slots feature request ### 🚀 The feature, motivation and pitch In the below code: def activate_adapter( self, lora_id: int, ) -> bool: """Move LoRA i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: num of LoRAs requested by the batch is larger than num lora slots feature request ### 🚀 The feature, motivation and pitch In the below code: def activate_adapter( self, lora_id: int, ) -> bool:
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
