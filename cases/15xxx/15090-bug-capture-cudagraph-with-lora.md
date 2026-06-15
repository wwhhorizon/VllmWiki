# vllm-project/vllm#15090: [Bug]: Capture CudaGraph with LoRA

| 字段 | 值 |
| --- | --- |
| Issue | [#15090](https://github.com/vllm-project/vllm/issues/15090) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Capture CudaGraph with LoRA

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when I use LoRA with enabel_eager=False(which means it should capture cudaGraph), I find the below code could cause problem(in vllm/vllm/worker/model_runner.py): if self.lora_config: lora_mapping = LoRAMapping( **dict(index_mapping=[0] * batch_size, prompt_mapping=[0] * batch_size, is_prefill=False)) self.set_active_loras(set(), lora_mapping) then I print `token_lora_indices` by `self.lora_manager._adapter_manager.punica_wrapper._token_lora_indices`, but only get `tensor([-1, -1, -1, ..., 0, 0, 0], device='cuda:0')`. A token with LoRA_indices=-1 seems not right. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Capture CudaGraph with LoRA bug;stale ### Your current environment ### 🐛 Describe the bug when I use LoRA with enabel_eager=False(which means it should capture cudaGraph), I find the below code could cause proble...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ironment ### 🐛 Describe the bug when I use LoRA with enabel_eager=False(which means it should capture cudaGraph), I find the below code could cause problem(in vllm/vllm/worker/model_runner.py): if self.lora_config: lora...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: udaGraph), I find the below code could cause problem(in vllm/vllm/worker/model_runner.py): if self.lora_config: lora_mapping = LoRAMapping( **dict(index_mapping=[0] * batch_size, prompt_mapping=[0] * batch_size, is_pref...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Capture CudaGraph with LoRA bug;stale ### Your current environment ### 🐛 Describe the bug when I use LoRA with enabel_eager=False(which means it should capture cudaGraph), I find the below code could cause proble...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
