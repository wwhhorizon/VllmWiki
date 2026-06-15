# vllm-project/vllm#28336: [Build]: Remove upper bound constraint on setuptools (<80) to resolve dependency conflicts

| 字段 | 值 |
| --- | --- |
| Issue | [#28336](https://github.com/vllm-project/vllm/issues/28336) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Build]: Remove upper bound constraint on setuptools (<80) to resolve dependency conflicts

### Issue 正文摘录

### Problem vLLM's build system currently constrains setuptools to ` =77.0.3, =0.9.0 depends on setuptools>=77.0.3, =80.9.0 These requirements are mutually exclusive. ``` ### Context - Setuptools 80.x has been stable since early 2025 (current: 80.9.0) - The ` =77.0.3 ``` This maintains the tested minimum version while allowing compatibility with current and future setuptools releases.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Build]: Remove upper bound constraint on setuptools (<80) to resolve dependency conflicts ### Problem vLLM's build system currently constrains setuptools to ` =77.0.3, =0.9.0 depends on setuptools>=77.0.3, =80.9.0 These
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nce early 2025 (current: 80.9.0) - The ` =77.0.3 ``` This maintains the tested minimum version while allowing compatibility with current and future setuptools releases.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
