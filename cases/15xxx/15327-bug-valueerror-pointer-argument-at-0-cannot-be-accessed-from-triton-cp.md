# vllm-project/vllm#15327: [Bug]: ValueError: Pointer argument (at 0) cannot be accessed from Triton (cpu tensor?)

| 字段 | 值 |
| --- | --- |
| Issue | [#15327](https://github.com/vllm-project/vllm/issues/15327) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: Pointer argument (at 0) cannot be accessed from Triton (cpu tensor?)

### Issue 正文摘录

### Your current environment linux ### 🐛 Describe the bug I run DeepSeeK-R1-Zero with the command ```text vllm serve DeepSeek-R1-Zero -pp 3 -tp 2 --cpu-offload-gb 400 --trust-remote-code --max-model-len 5000 ``` (I have six 48G 4090 and a 500G RAM, the model was downloaded directly from huggingface) Then I encountered this issue. ```python [rank0]: ValueError: Pointer argument (at 0) cannot be accessed from Triton (cpu tensor?) [rank0]:[W322 06:54:59.203812629 ProcessGroupNCCL.cpp:1250] Warning: WARNING: process group has NOT been destroyed before we destruct ProcessGroupNCCL. On normal program exit, the application should call destroy_process_group to ensure that any pending NCCL operations have finished in this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTorch 2.4 (function operator()) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answe...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: pSeek-R1-Zero -pp 3 -tp 2 --cpu-offload-gb 400 --trust-remote-code --max-model-len 5000 ``` (I have six 48G 4090 and a 500G RAM, the model was downloaded directly from huggingface) Then I encountered this issue. ```pyth...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: ValueError: Pointer argument (at 0) cannot be accessed from Triton (cpu tensor?) bug;stale ### Your current environment linux ### 🐛 Describe the bug I run DeepSeeK-R1-Zero with the command ```text vllm serve Deep...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: o with the command ```text vllm serve DeepSeek-R1-Zero -pp 3 -tp 2 --cpu-offload-gb 400 --trust-remote-code --max-model-len 5000 ``` (I have six 48G 4090 and a 500G RAM, the model was downloaded directly from huggingfac...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
