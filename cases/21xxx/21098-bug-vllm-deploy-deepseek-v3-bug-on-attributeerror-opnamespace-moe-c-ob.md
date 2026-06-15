# vllm-project/vllm#21098: [Bug]: vllm deploy deepseek-v3 bug on attributeerror: '_OpNameSpace' '_moe_C' object has no attribute 'moe_align_block_size'

| 字段 | 值 |
| --- | --- |
| Issue | [#21098](https://github.com/vllm-project/vllm/issues/21098) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm deploy deepseek-v3 bug on attributeerror: '_OpNameSpace' '_moe_C' object has no attribute 'moe_align_block_size'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug the launch command is ' vllm serve xxx --served-model-name deepseek-v3 -tp 8 --gpu-memory-utilization 0.85 --max-model-len 65536 --enable-auto-tool-choice --tool-call-parser deepseek_v3 ' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 3 ' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tributeerror: '_OpNameSpace' '_moe_C' object has no attribute 'moe_align_block_size' bug;stale ### Your current environment ### 🐛 Describe the bug the launch command is ' vllm serve xxx --served-model-name deepseek-v3 -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ### 🐛 Describe the bug the launch command is ' vllm serve xxx --served-model-name deepseek-v3 -tp 8 --gpu-memory-utilization 0.85 --max-model-len 65536 --enable-auto-tool-choice --tool-call-parser deepseek_v3 ' ### Befo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: vllm deploy deepseek-v3 bug on attributeerror: '_OpNameSpace' '_moe_C' object has no attribute 'moe_align_block_size' bug;stale ### Your current environment ### 🐛 Describe the bug the launch command is ' vllm ser...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: OpNameSpace' '_moe_C' object has no attribute 'moe_align_block_size' bug;stale ### Your current environment ### 🐛 Describe the bug the launch command is ' vllm serve xxx --served-model-name deepseek-v3 -tp 8 --gpu-memor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
