# vllm-project/vllm#32288: [Build]: Relax anthropic version pin from ==0.71.0 to >=0.71.0

| 字段 | 值 |
| --- | --- |
| Issue | [#32288](https://github.com/vllm-project/vllm/issues/32288) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Build]: Relax anthropic version pin from ==0.71.0 to >=0.71.0

### Issue 正文摘录

Hey guys, we need to upgrade vllm on our side but your anthropic requirement blocks that upgrade. ### Problem vLLM currently pins the `anthropic` package to an exact version in `requirements/common.txt`: ``` anthropic == 0.71.0 ``` This creates dependency conflicts with other packages that require newer versions of `anthropic`. For example, `pydantic-ai` requires `anthropic>=0.75.0`, making it impossible to install alongside vLLM: ``` vllm>=0.12.0 depends on anthropic==0.71.0 pydantic-ai depends on anthropic>=0.75.0 These requirements are mutually exclusive. ``` ### Context - The `anthropic` package is now at version 0.76.0 - The exact pin was added in #22627 (merged Oct 2025) when Anthropic API support was introduced - There doesn't appear to be a specific incompatibility with newer versions - it was likely pinned conservatively - As more packages adopt newer anthropic versions as minimums, this constraint will cause increasing compatibility issues ### Proposed Solution Relax the version constraint to allow compatible newer versions: ``` anthropic >= 0.71.0 ``` This maintains the tested minimum version while allowing compatibility with current and future anthropic releases. ### A...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Build]: Relax anthropic version pin from ==0.71.0 to >=0.71.0 Hey guys, we need to upgrade vllm on our side but your anthropic requirement blocks that upgrade. ### Problem vLLM currently pins the `anthropic` package to
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: guys, we need to upgrade vllm on our side but your anthropic requirement blocks that upgrade. ### Problem vLLM currently pins the `anthropic` package to an exact version in `requirements/common.txt`: ``` anthropic == 0....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: patible newer versions: ``` anthropic >= 0.71.0 ``` This maintains the tested minimum version while allowing compatibility with current and future anthropic releases. ### Additional Context This is similar to issue #283...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
