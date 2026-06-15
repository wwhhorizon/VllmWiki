# vllm-project/vllm#5667: [Bug]: Option for preemption_mode uses underscore (_) instead of dash (-)

| 字段 | 值 |
| --- | --- |
| Issue | [#5667](https://github.com/vllm-project/vllm/issues/5667) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Option for preemption_mode uses underscore (_) instead of dash (-)

### Issue 正文摘录

### Your current environment Irrelevant, the error is easily seen in the code. It is seen in version 0.5.0.post1, in the file vllm.engine.arg_utils:576 ### 🐛 Describe the bug In the latest release (V0.5.0.post1), the CLI argument for `preemption_mode` parameter of EngineArgs is `--preemption_mode` which goes against the typical convention of replacing _ with - in command-line parameters. This won't affect any other code if fixed to `--preemption-mode`, because argparse converts any dashes to underscores in the namespace returned by `parser.parse_args()`. However the current situation causes problems when I want to convert an EngineArgs instance to set of command-line flags (say in order to launch a vllm server programmatically via subprocess)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ronment Irrelevant, the error is easily seen in the code. It is seen in version 0.5.0.post1, in the file vllm.engine.arg_utils:576 ### 🐛 Describe the bug In the latest release (V0.5.0.post1), the CLI argument for `preem...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: in the file vllm.engine.arg_utils:576 ### 🐛 Describe the bug In the latest release (V0.5.0.post1), the CLI argument for `preemption_mode` parameter of EngineArgs is `--preemption_mode` which goes against the typical con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
