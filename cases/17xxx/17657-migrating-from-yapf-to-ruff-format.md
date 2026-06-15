# vllm-project/vllm#17657: Migrating from `yapf` to `ruff format`

| 字段 | 值 |
| --- | --- |
| Issue | [#17657](https://github.com/vllm-project/vllm/issues/17657) |
| 状态 | closed |
| 标签 | RFC;keep-open |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Migrating from `yapf` to `ruff format`

### Issue 正文摘录

### Motivation. We would like to transition vLLM from `yapf` to `ruff format`. This will give us: - Increased line length - Better formatting style which is more effectively enforced by tooling rather than by maintainers - Fewer formatting tools fighting eachother ### Proposed Change. We plan to make this change gradually using the following process. If we are converting directory `x`: - In `x`, we add a local `pyproject.toml` which: - overrides `ruff`'s line length to 88 (it's own default) - removes the deprecated type ignores - enables `isort` in ruff - enables formatting of code in docstrings (good for the API docs) - We add `x` to the list of files to run `ruff-format` on in `.pre-commit-config.yaml` - We add `x` to the list of ignores in the `yapf` and `isort` config in the root `pyproject.toml` Here is the list of PRs used to make the transition: - [x] https://github.com/vllm-project/vllm/pull/17656 - [x] https://github.com/vllm-project/vllm/pull/18068 - [x] https://github.com/vllm-project/vllm/pull/18400 - [ ] https://github.com/vllm-project/vllm/pull/21129 - [ ] #26247

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Migrating from `yapf` to `ruff format` RFC;keep-open ### Motivation. We would like to transition vLLM from `yapf` to `ruff format`. This will give us: - Increased line length - Better formatting style which is more effe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
