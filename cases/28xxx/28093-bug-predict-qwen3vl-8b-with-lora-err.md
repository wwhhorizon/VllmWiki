# vllm-project/vllm#28093: [Bug]: predict qwen3vl-8b with lora err

| 字段 | 值 |
| --- | --- |
| Issue | [#28093](https://github.com/vllm-project/vllm/issues/28093) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: predict qwen3vl-8b with lora err

### Issue 正文摘录

### Your current environment vllm0.11.0+torch2.8+cu12.6 ### 🐛 Describe the bug During inference using Qwen3VL-8B with the trained LoRA, an error occurred. Updating to the nightly version still failed to resolve the issue. ```text (EngineCore_DP0 pid=19569) File "/algoqc_nas/shixu/mamba/envs/vlm/lib/python3.12/site-packages/vllm/lora/ops/triton_ops/lora_shrink_op.py", line 149, in _lora_shrink (EngineCore_DP0 pid=19569) assert token_lora_mapping.size(0) == M (EngineCore_DP0 pid=19569) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=19569) AssertionError [rank0]:[W1105 03:46:33.417694485 ProcessGroupNCCL.cpp:1538] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator()) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: predict qwen3vl-8b with lora err bug;stale ### Your current environment vllm0.11.0+torch2.8+cu12.6 ### 🐛 Describe the bug During inference using Qwen3VL-8B with the trained LoRA, an error occurred. Updating to th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: goqc_nas/shixu/mamba/envs/vlm/lib/python3.12/site-packages/vllm/lora/ops/triton_ops/lora_shrink_op.py", line 149, in _lora_shrink (EngineCore_DP0 pid=19569) assert token_lora_mapping.size(0) == M (EngineCore_DP0 pid=195...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 3VL-8B with the trained LoRA, an error occurred. Updating to the nightly version still failed to resolve the issue. ```text (EngineCore_DP0 pid=19569) File "/algoqc_nas/shixu/mamba/envs/vlm/lib/python3.12/site-packages/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ne 149, in _lora_shrink (EngineCore_DP0 pid=19569) assert token_lora_mapping.size(0) == M (EngineCore_DP0 pid=19569) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=19569) AssertionError [rank0]:[W1105 03:46:33.4176...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
