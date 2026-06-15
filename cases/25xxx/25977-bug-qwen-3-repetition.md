# vllm-project/vllm#25977: [Bug]: Qwen 3 repetition

| 字段 | 值 |
| --- | --- |
| Issue | [#25977](https://github.com/vllm-project/vllm/issues/25977) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen 3 repetition

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have run the vllm on qwen3 8b model and got repetition on output like this 📝 Prompt 1: Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet? ================================================================================ 💬 Generated Output: ================================================================================ Processed prompts: 100%|█████████████| 1/1 [00:30<00:00, 30.91s/it, est. speed input: 1.97 toks/s, output: 66.28 toks/s] Let's break down the information given: 1. The wallet costs $100. 2. Betty has half of the money she needs, so she currently has $50. 3. Her parents give her $15. 4. Her grandparents give her twice as much as her parents, which is $30. First, we'll calculate the total amount of money Betty has after receiving the gifts: - Initial amount: $50 - Parents' gift: $15 - Grandparents' gift: $30 Total amount Betty has = $50 + $15 + $30 = $95 Now, we'll subtract this from the total cost of the wall...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen 3 repetition bug ### Your current environment ### 🐛 Describe the bug I have run the vllm on qwen3 8b model and got repetition on output like this 📝 Prompt 1: Betty is saving money for a new wallet which costs
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ch costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: his ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: odel="Qwen/Qwen3-8B", disable_cascade_attn=True, enable_prefix_caching=False) i use vllm==0.8.5 anyone know how to fix this ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
