# vllm-project/vllm#17592: [Bug]: vLLM pre-commit hook doesn't work with git worktree

| 字段 | 值 |
| --- | --- |
| Issue | [#17592](https://github.com/vllm-project/vllm/issues/17592) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM pre-commit hook doesn't work with git worktree

### Issue 正文摘录

### Your current environment n/a ### 🐛 Describe the bug I'm getting the following: ``` yapf.................................................(no files to check)Skipped ruff.................................................(no files to check)Skipped codespell............................................(no files to check)Skipped isort................................................(no files to check)Skipped clang-format.........................................(no files to check)Skipped PyMarkdown...........................................(no files to check)Skipped Lint GitHub Actions workflow files...................(no files to check)Skipped pip-compile..........................................(no files to check)Skipped Run mypy for local Python installation...............(no files to check)Skipped Lint shell scripts...................................(no files to check)Skipped Lint PNG exports from excalidraw.....................(no files to check)Skipped Check SPDX headers...................................(no files to check)Skipped Check for spaces in all filenames........................................Passed Update Dockerfile dependency graph...................(no files to check)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Actions workflow files...................(no files to check)Skipped pip-compile..........................................(no files to check)Skipped Run mypy for local Python installation...............(no files to check...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: `` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ........................................(no files to check)Skipped clang-format.........................................(no files to check)Skipped PyMarkdown...........................................(no files to check)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
