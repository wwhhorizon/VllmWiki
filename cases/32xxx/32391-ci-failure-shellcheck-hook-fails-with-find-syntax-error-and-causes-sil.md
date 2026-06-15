# vllm-project/vllm#32391: [CI Failure]: shellcheck hook fails with find syntax error and causes silent failures

| 字段 | 值 |
| --- | --- |
| Issue | [#32391](https://github.com/vllm-project/vllm/issues/32391) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: shellcheck hook fails with find syntax error and causes silent failures

### Issue 正文摘录

### Your current environment This is not environment-specific bug. ### 🐛 Describe the bug The `shellcheck` script fails initially due to inappropriate usage of `.git` in the `find` command syntax. ```bash ❯ pre-commit run --all-files # ... (omitted initialization logs) ... Run mypy locally for lowest supported Python version................................................Passed Lint shell scripts..................................................................................Failed - hook id: shellcheck - exit code: 2 shellcheck-stable/LICENSE.txt shellcheck-stable/README.txt shellcheck-stable/shellcheck find: paths must precede expression: `.git' find: possible unquoted pattern after predicate `-name'? shellcheck-stable/LICENSE.txt shellcheck-stable/README.txt shellcheck-stable/shellcheck find: paths must precede expression: `.git' find: possible unquoted pattern after predicate `-name'? # ... (repeated errors) shellcheck-stable/LICENSE.txt tar: shellcheck-stable/LICENSE.txt: Cannot open: File exists shellcheck-stable/README.txt shellcheck-stable/shellcheck tar: Exiting with failure status due to previous errors ``` Crucially, subsequent runs result in a silent failure. After th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [CI Failure]: shellcheck hook fails with find syntax error and causes silent failures bug ### Your current environment This is not environment-specific bug. ### 🐛 Describe the bug The `shellcheck` script fails initiall
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .............................................................Passed ruff format.........................................................................................Passed typos..........................................
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ............................................Passed Forbid direct 'import triton'.......................................................................Passed Prevent new pickle/cloudpickle imports..........................
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ay. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ...........................................Passed reformat nightly_torch_test.txt to be in sync with test.in..........................................Passed Run mypy locally for lowest supported Python version.............

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
