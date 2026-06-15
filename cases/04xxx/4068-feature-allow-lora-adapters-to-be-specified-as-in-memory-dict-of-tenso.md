# vllm-project/vllm#4068: [Feature]: Allow LoRA adapters to be specified as in-memory dict of tensors

| 字段 | 值 |
| --- | --- |
| Issue | [#4068](https://github.com/vllm-project/vllm/issues/4068) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow LoRA adapters to be specified as in-memory dict of tensors

### Issue 正文摘录

### 🚀 The feature, motivation and pitch PPO and a number of other LLM fine-tuning techniques require autoregressive generation as part of the training process. When using vLLM to speed up the autoregressive generation part of the training loop, is there an efficient way to update the weights of the LLM? Specifically, in the case of LoRA fine-tuning, is there a way to efficiently swap out the adapters without having to save them to the filesystem? ### Alternatives ## Efficient LoRA adapter update Possible workaround without any code change: save adapters to an in-memory file-system (e.g., `/dev/shm`) and point to that directory in each LoRARequest. This workaround: - Avoids disk read/write bottleneck and SSD wear. - Still incurs the overhead of safetensors serialization and deserialization. Proposed change: modify LoRARequest to allow adapters to be specified as a dictionary of tensors. - Modify class definition of LoRARequest - mark `lora_local_path: str` as optional - add new optional `lora_tensors: dict[str, torch.Tensor]` attribute. - Modify WorkerLoRAManager `_load_lora` implementation ([vllm/lora/worker_manager.py](https://github.com/vllm-project/vllm/blob/2cd6b4f3625466eb584...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: oint`. ## Alternative approach: non-LoRA parameter update - [OpenRLHF](https://github.com/OpenLLMAI/OpenRLHF) replaces vLLM model parameters with in-memory tensors by overriding `hf_model_weights_iterator` and invoking...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Allow LoRA adapters to be specified as in-memory dict of tensors feature request;stale ### 🚀 The feature, motivation and pitch PPO and a number of other LLM fine-tuning techniques require autoregressive generation as pa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Allow LoRA adapters to be specified as in-memory dict of tensors feature request;stale ### 🚀 The feature, motivation and pitch PPO and a number of other LLM fine-tuning techniques require autoregressive gener...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
