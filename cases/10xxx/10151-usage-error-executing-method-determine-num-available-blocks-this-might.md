# vllm-project/vllm#10151: [Usage]: Error executing method determine_num_available_blocks. This might cause deadlock in distributed execution.

| 字段 | 值 |
| --- | --- |
| Issue | [#10151](https://github.com/vllm-project/vllm/issues/10151) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;quantization |
| 子分类 |  |
| Operator 关键词 | fp8;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Error executing method determine_num_available_blocks. This might cause deadlock in distributed execution.

### Issue 正文摘录

### Your current environment I want to deply neuralmagic/DeepSeek-Coder-V2-Instruct-FP8 with 8 x NVIDIA L20， use -tensor-parallel-size=8 --enforce-eager --trust-remote-code --quantization=fp8 --kv-cache-dtype=fp8 but i get logs： ![20241108-181536](https://github.com/user-attachments/assets/b1ad9d16-0c6c-49d6-bfbc-510273342010) ### How would you like to use vllm I want to deply neuralmagic/DeepSeek-Coder-V2-Instruct-FP8 with 8 x NVIDIA L20， use -tensor-parallel-size=8 --enforce-eager --trust-remote-code --quantization=fp8 --kv-cache-dtype=fp8 but i get logs： ![20241108-181536](https://github.com/user-attachments/assets/537a5320-e512-41d0-9d78-64dd4479a3ae) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rent environment I want to deply neuralmagic/DeepSeek-Coder-V2-Instruct-FP8 with 8 x NVIDIA L20， use -tensor-parallel-size=8 --enforce-eager --trust-remote-code --quantization=fp8 --kv-cache-dtype=fp8 but i get logs： ![...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Error executing method determine_num_available_blocks. This might cause deadlock in distributed execution. usage;stale ### Your current environment I want to deply neuralmagic/DeepSeek-Coder-V2-Instruct-FP8 with 8 x NVI...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ae) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: parallel-size=8 --enforce-eager --trust-remote-code --quantization=fp8 --kv-cache-dtype=fp8 but i get logs： ![20241108-181536](https://github.com/user-attachments/assets/b1ad9d16-0c6c-49d6-bfbc-510273342010) ### How wou...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Usage]: Error executing method determine_num_available_blocks. This might cause deadlock in distributed execution. usage;stale ### Your current environment I want to deply neuralmagic/DeepSeek-Coder-V2-Instruct-FP8 wit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
