# vllm-project/vllm#9774: [Bug]: [help wanted] MoE + TP + custom allreduce bug

| 字段 | 值 |
| --- | --- |
| Issue | [#9774](https://github.com/vllm-project/vllm/issues/9774) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;moe |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;moe |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [help wanted] MoE + TP + custom allreduce bug

### Issue 正文摘录

### Your current environment main branch, H100 ### Model Input Dumps _No response_ ### 🐛 Describe the bug when I try this simple command `vllm serve allenai/OLMoE-1B-7B-0924 -tp 2` on the main branch, it hits an error: `Failed: Cuda error /workspace/csrc/custom_all_reduce.cuh:336 'invalid argument'` removing `-tp` works, and disabling custom allreduce also works. not sure what's happening. if anyone is familiar with the moe code, please help. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: TP + custom allreduce bug bug ### Your current environment main branch, H100 ### Model Input Dumps _No response_ ### 🐛 Describe the bug when I try this simple command `vllm serve allenai/OLMoE-1B-7B-0924 -tp 2` on the m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: m allreduce bug bug ### Your current environment main branch, H100 ### Model Input Dumps _No response_ ### 🐛 Describe the bug when I try this simple command `vllm serve allenai/OLMoE-1B-7B-0924 -tp 2` on the main branch...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: [help wanted] MoE + TP + custom allreduce bug bug ### Your current environment main branch, H100 ### Model Input Dumps _No response_ ### 🐛 Describe the bug when I try this simple command `vllm serve allenai/OLMoE...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development distributed_parallel;model_support;moe cuda;moe Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
