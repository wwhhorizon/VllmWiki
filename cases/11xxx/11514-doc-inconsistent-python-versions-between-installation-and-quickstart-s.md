# vllm-project/vllm#11514: [Doc]:  Inconsistent Python versions between Installation and Quickstart sections in the documentation

| 字段 | 值 |
| --- | --- |
| Issue | [#11514](https://github.com/vllm-project/vllm/issues/11514) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]:  Inconsistent Python versions between Installation and Quickstart sections in the documentation

### Issue 正文摘录

### 📚 The doc issue There is an inconsistency in the Python versions specified for creating a conda virtual environment in the official documentation: - In the `Installation` section, the recommended Python version is `python==3.12`. - In the `Quickstart` section, the recommended Python version is `python==3.10`. This inconsistency may confuse users and could potentially cause compatibility issues when following the instructions. Thank you for the contributions to the open-source community! ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Doc]: Inconsistent Python versions between Installation and Quickstart sections in the documentation documentation ### 📚 The doc issue There is an inconsistency in the Python versions specified for creating a conda vir...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
