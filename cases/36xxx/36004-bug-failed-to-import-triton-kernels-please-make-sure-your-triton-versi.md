# vllm-project/vllm#36004: [Bug]: Failed to import Triton kernels. Please make sure your triton version is compatible. Error: cannot import name 'SparseMatrix' from 'triton_kernels.tensor'

| 字段 | 值 |
| --- | --- |
| Issue | [#36004](https://github.com/vllm-project/vllm/issues/36004) |
| 状态 | open |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Failed to import Triton kernels. Please make sure your triton version is compatible. Error: cannot import name 'SparseMatrix' from 'triton_kernels.tensor'

### Issue 正文摘录

### Your current environment vllm==0.16.1rc1.dev214+gd6e04f4c4 ### 🐛 Describe the bug help,哪个triton版本可以，3.4.0\3.6.0都报错了 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Failed to import Triton kernels. Please make sure your triton version is compatible. Error: cannot import name 'SparseMatrix' from 'triton_kernels.tensor' bug ### Your current environment vllm==0.16.1rc1.dev214+g...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Failed to import Triton kernels. Please make sure your triton version is compatible. Error: cannot import name 'SparseMatrix' from 'triton_kernels.tensor' bug ### Your current environment vllm==0.16.1rc1.dev214+g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 报错了 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
