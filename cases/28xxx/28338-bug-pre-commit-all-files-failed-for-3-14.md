# vllm-project/vllm#28338: [Bug]:  pre-commit all files failed for 3.14

| 字段 | 值 |
| --- | --- |
| Issue | [#28338](https://github.com/vllm-project/vllm/issues/28338) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  pre-commit all files failed for 3.14

### Issue 正文摘录

### Your current environment ➜ vllm git:(main) pre-commit run --all-files Installed 1 package in 5ms ruff check..........................................................................................Passed ruff format.........................................................................................Passed typos...............................................................................................Passed clang-format........................................................................................^[[116;10uPassed Lint GitHub Actions workflow files..................................................................Passed pip-compile.........................................................................................^R Failed - hook id: pip-compile - exit code: 1 Updated https://github.com/IBM/terratorch.git (07184fcf91a1324f831ff521dd238d97f × No solution found when resolving dependencies: ╰─▶ Because only the following versions of ray[cgraph] are available: ray[cgraph] =2.48.0 has no wheels with a matching Python ABI tag (e.g., `cp314`), we can conclude that ray[cgraph]>=2.48.0 cannot be used. And because you require ray[cgraph]>=2.48.0, we can conclude that...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Your current environment ➜ vllm git:(main) pre-commit run --all-files Installed 1 package in 5ms ruff check..........................................................................................Passed ruff format.......
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .14 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .............................................................Passed ruff format.........................................................................................Passed typos..........................................
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
