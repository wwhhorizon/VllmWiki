# vllm-project/vllm#29382: [Doc]: Expert Parallel Deployment says "Tensor parallel size (always 1 for now)" is confusing

| 字段 | 值 |
| --- | --- |
| Issue | [#29382](https://github.com/vllm-project/vllm/issues/29382) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Expert Parallel Deployment says "Tensor parallel size (always 1 for now)" is confusing

### Issue 正文摘录

### 📚 The doc issue On page https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment/#single-node-deployment it says Tensor parallel size can only be 1 but didn't mention the behavior of Attention Layers On page https://docs.vllm.ai/en/latest/serving/data_parallel_deployment/ it says The expert layers will by default form a (DP x TP) sized tensor parallel group. To enable expert parallelism, include the --enable-expert-parallel CLI arg (on all nodes in the multi-node case). which is rather confusing. ### Suggest a potential alternative/fix Point out the correct behavior of MoE models when TP, EP are both set. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: form a (DP x TP) sized tensor parallel group. To enable expert parallelism, include the --enable-expert-parallel CLI arg (on all nodes in the multi-node case). which is rather confusing. ### Suggest a potential alternat...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Doc]: Expert Parallel Deployment says "Tensor parallel size (always 1 for now)" is confusing documentation ### 📚 The doc issue On page https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment/#single-node-depl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ggest a potential alternative/fix Point out the correct behavior of MoE models when TP, EP are both set. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatb...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ing documentation ### 📚 The doc issue On page https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment/#single-node-deployment it says Tensor parallel size can only be 1 but didn't mention the behavior of Atten...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
