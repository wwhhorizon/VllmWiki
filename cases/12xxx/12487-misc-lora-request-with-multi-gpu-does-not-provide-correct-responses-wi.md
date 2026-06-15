# vllm-project/vllm#12487: [Misc]: LoRA request with Multi GPU does not provide correct responses with num_scheduler_steps config

| 字段 | 值 |
| --- | --- |
| Issue | [#12487](https://github.com/vllm-project/vllm/issues/12487) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: LoRA request with Multi GPU does not provide correct responses with num_scheduler_steps config

### Issue 正文摘录

### Anything you want to discuss about vllm. Hello All, We are encountering a strange issue with our LoRA adapter, when running in multi-GPU setup. Context: Base model: Mistral Nemo 12B (https://huggingface.co/nvidia/Mistral-NeMo-12B-Instruct) Adapter Rank: 8 Vllm Model.json ```json { "model": "/model-store/backbone/Mistral-Nemo-Base", "disable_log_requests": "true", "gpu_memory_utilization": 0.85, "max_model_len": 16000, "tensor_parallel_size": 2, "distributed_executor_backend": "ray", "enable_lora": "true", "max_lora_rank": 8, "max_loras": 4, "trust_remote_code": "true" } ``` Multi-lora.json ```json { "t2f": "/model-store/backbone/loras/Mistral-Nemo-Base-t2f-lora" } ``` Now, when we add the num_scheduler_steps configuration to the model.json, ```json "num_scheduler_steps": 8, ``` Now the adapter responds with correct response when we don't have 'num_scheduler_steps' in the multi-GPU setup, but when we add this configuration, we don't get the correct response from the adapter any longer, even though everything else remains same. We are looking at the response from the LoRA targeted request here not the response from Base model. Has anyone faced similar issue, are there any settin...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: th Multi GPU does not provide correct responses with num_scheduler_steps config ### Anything you want to discuss about vllm. Hello All, We are encountering a strange issue with our LoRA adapter, when running in multi-GP...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: LoRA request with Multi GPU does not provide correct responses with num_scheduler_steps config ### Anything you want to discuss about vllm. Hello All, We are encountering a strange issue with our LoRA adapter, w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: el_len": 16000, "tensor_parallel_size": 2, "distributed_executor_backend": "ray", "enable_lora": "true", "max_lora_rank": 8, "max_loras": 4, "trust_remote_code": "true" } ``` Multi-lora.json ```json { "t2f": "/model-sto...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: hit ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: he correct response from the adapter any longer, even though everything else remains same. We are looking at the response from the LoRA targeted request here not the response from Base model. Has anyone faced similar is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
