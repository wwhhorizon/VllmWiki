# vllm-project/vllm#10689: [Bug]: CPU Docker build fail.

| 字段 | 值 |
| --- | --- |
| Issue | [#10689](https://github.com/vllm-project/vllm/issues/10689) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CPU Docker build fail.

### Issue 正文摘录

### Your current environment ![image](https://github.com/user-attachments/assets/4c4809e4-7983-4205-a747-05f3e037575c) ### Model Input Dumps _No response_ ### 🐛 Describe the bug docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . ![image](https://github.com/user-attachments/assets/4f3dac9d-1c05-40d8-89a1-1d52f9e78705) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: CPU Docker build fail. bug ### Your current environment ![image](https://github.com/user-attachments/assets/4c4809e4-7983-4205-a747-05f3e037575c) ### Model Input Dumps _No response_ ### 🐛 Describe the bug docker...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 05) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: b.com/user-attachments/assets/4c4809e4-7983-4205-a747-05f3e037575c) ### Model Input Dumps _No response_ ### 🐛 Describe the bug docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . ![image](https://github.com/u...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
