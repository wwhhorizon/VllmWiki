# vllm-project/vllm#8846: [Bug]: We tested Qwen2.5_3b on opencompass and vllm, and the results  are very different

| 字段 | 值 |
| --- | --- |
| Issue | [#8846](https://github.com/vllm-project/vllm/issues/8846) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: We tested Qwen2.5_3b on opencompass and vllm, and the results  are very different

### Issue 正文摘录

### Your current environment vllm0.5.0 post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug EXAMPLE question: Problem:\nThe superfactorial $n\\$$ is defined as $n\\$ = \\underbrace{ n!^{{n!}^{{\\cdot}^{{\\cdot}^{{\\cdot}^{n!}}}}}}_{n!}$. What is the units digit of $4\\$$?\nSolution:" gold: 6 vllm: We can start by finding the units digit of $4!$, which is $24$. Then, we can find the units digit of $24!$, which is $0$. Since $24!$ is divisible by $10$, the units digit of $24!^{{24!}^{{\\cdot}^{{\\cdot}^{{\\cdot}^{24!}}}}}$ is $0$. Therefore, the units digit of $4\\$ = \\underbrace{ 4!^{{4!}^{{\\cdot}^{{\\cdot}^{{\\cdot}^{4!}}}}}}_{4!}$ is $\\boxed{{0}}$.\nFinal Answer: The final answer is $0$. I hope it is correct.\n\n opencompass: To find the units digit of $4\\$$, we need to find the units digit of $4!^{{4!}^{{\\cdot}^{{\\cdot}^{{\\cdot}^{4!}}}}}$.\nFirst, we find the units digit of $4!$, which is $24$.\nNext, we find the units digit of $4!^2$, which is $24^2 = 576$.\nContinuing this pattern, we find that the units digit of $4!^{{4!}^{{\\cdot}^{{\\cdot}^{{\\cdot}^{4!}}}}}$ is $6$.\nTherefore, the units digit of $4\\$$ is $\\boxed{6}$.\nFinal Answer: The final answer is...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: We tested Qwen2.5_3b on opencompass and vllm, and the results are very different bug;stale ### Your current environment vllm0.5.0 post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug EXAMPLE question:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n2.5_3b on opencompass and vllm, and the results are very different bug;stale ### Your current environment vllm0.5.0 post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug EXAMPLE question: Problem:\nThe super...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: We tested Qwen2.5_3b on opencompass and vllm, and the results are very different bug;stale ### Your current environment vllm0.5.0 post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug EXAMPLE question:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
