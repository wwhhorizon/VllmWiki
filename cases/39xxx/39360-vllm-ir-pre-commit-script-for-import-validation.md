# vllm-project/vllm#39360: [vLLM IR] pre-commit script for import validation

| 字段 | 值 |
| --- | --- |
| Issue | [#39360](https://github.com/vllm-project/vllm/issues/39360) |
| 状态 | open |
| 标签 | vllm-ir |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [vLLM IR] pre-commit script for import validation

### Issue 正文摘录

As mentioned in the design doc (#32358), vLLM IR base infra and ops should be fully independent from the rest of vLLM: any ops that must be dependent on vLLM can live outside the `vllm/ir` directory. We should enforce this via a pre-commit script; apart from `vllm.logging` (and obviously `vllm.ir`), no other imports from `vllm` should be allowed. This should include relative and local imports.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [vLLM IR] pre-commit script for import validation vllm-ir As mentioned in the design doc (#32358), vLLM IR base infra and ops should be fully independent from the rest of vLLM: any ops that must be dependent on vLLM can...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
