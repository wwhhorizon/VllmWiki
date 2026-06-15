# vllm-project/vllm#7893: [Bug]: After VLLM successfully starts the service, a prompt will appear during the first inference and the inference cannot proceed normally

| 字段 | 值 |
| --- | --- |
| Issue | [#7893](https://github.com/vllm-project/vllm/issues/7893) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: After VLLM successfully starts the service, a prompt will appear during the first inference and the inference cannot proceed normally

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug No code. Just starting the service nvidia-smi result is NVIDIA-SMI 535.161.07 Driver Version: 535.161.07 CUDA Version: 12.2 uname -a result is Linux VM-0-16-centos 5.4.119-19.0009.28 #1 SMP Thu May 18 10:37:10 CST 2023 x86_64 x86_64 x86_64 GNU/Linux linux version is H20 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t ### 🐛 Describe the bug No code. Just starting the service nvidia-smi result is NVIDIA-SMI 535.161.07 Driver Version: 535.161.07 CUDA Version: 12.2 uname -a result is Linux VM-0-16-centos 5.4.119-19.0009.28 #1 SMP Thu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: service nvidia-smi result is NVIDIA-SMI 535.161.07 Driver Version: 535.161.07 CUDA Version: 12.2 uname -a result is Linux VM-0-16-centos 5.4.119-19.0009.28 #1 SMP Thu May 18 10:37:10 CST 2023 x86_64 x86_64 x86_64 GNU/Li...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
