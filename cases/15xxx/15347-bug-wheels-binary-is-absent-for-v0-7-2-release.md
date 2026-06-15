# vllm-project/vllm#15347: [Bug]: Wheels binary is absent for v0.7.2 release

| 字段 | 值 |
| --- | --- |
| Issue | [#15347](https://github.com/vllm-project/vllm/issues/15347) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Wheels binary is absent for v0.7.2 release

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Quick verification test:** Wheel binary not found for v0.7.2: ```wget https://wheels.vllm.ai/0408efc6d0c17fba17b2be38d0d0f02e96d2bf9d/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl``` But, it works for : 1. v0.7.3 ```wget https://wheels.vllm.ai/ed6e9075d31e32c8548b480a47d1ffb77da1f54c/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl``` 2. v0.7.1 ```wget https://wheels.vllm.ai/4f4d427ac2cee0f8ff7f79103001f6617fa8989c/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Wheels binary is absent for v0.7.2 release bug ### Your current environment ### 🐛 Describe the bug **Quick verification test:** Wheel binary not found for v0.7.2: ```wget https://wheels.vllm.ai/0408efc6d0c17fba17...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: our current environment ### 🐛 Describe the bug **Quick verification test:** Wheel binary not found for v0.7.2: ```wget https://wheels.vllm.ai/0408efc6d0c17fba17b2be38d0d0f02e96d2bf9d/vllm-1.0.0.dev-cp38-abi3-manylinux1_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
