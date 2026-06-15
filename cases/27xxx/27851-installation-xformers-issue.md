# vllm-project/vllm#27851: [Installation]: xformers issue

| 字段 | 值 |
| --- | --- |
| Issue | [#27851](https://github.com/vllm-project/vllm/issues/27851) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: xformers issue

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm × No solution found when resolving dependencies: ╰─▶ Because there is no version of xformers{platform_machine == 'x86_64' and sys_platform == 'linux'}==0.0.33+5d4b92a5.d20251029 and vllm==0.11.1rc6.dev12+gb2e65cb4a.precompiled depends on xformers{platform_machine == 'x86_64' and sys_platform == 'linux'}==0.0.33+5d4b92a5.d20251029, we can conclude that vllm==0.11.1rc6.dev12+gb2e65cb4a.precompiled cannot be used. And because only vllm==0.11.1rc6.dev12+gb2e65cb4a.precompiled is available and you require vllm, we can conclude that your requirements are unsatisfiable. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: xformers issue installation ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm × No solution found when resolving dependencies: ╰─▶ Because
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: le. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
