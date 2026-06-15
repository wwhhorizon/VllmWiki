# vllm-project/vllm#5456: [Bug]: Outdated binaries when re-building vLLM from source

| 字段 | 值 |
| --- | --- |
| Issue | [#5456](https://github.com/vllm-project/vllm/issues/5456) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Outdated binaries when re-building vLLM from source

### Issue 正文摘录

### 🐛 Describe the bug After upgrading vLLM (e.g. syncing a fork with latest `main` branch), re-building from source fails to clear/overwrite the existing compiled binaries, resulting in errors such as ``` AttributeError: '_OpNamespace' '_C' object has no attribute ... ``` ### Workaround Installing from a fresh clone of vLLM fixes this error. Nevertheless, it would be ideal to automatically remove/update outdated binaries when re-building vLLM. ### Related issues - #5448 - #5454 - #5461

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Outdated binaries when re-building vLLM from source bug ### 🐛 Describe the bug After upgrading vLLM (e.g. syncing a fork with latest `main` branch), re-building from source fails to clear/overwrite the existing c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ### 🐛 Describe the bug After upgrading vLLM (e.g. syncing a fork with latest `main` branch), re-building from source fails to clear/overwrite the existing compiled binaries, resulting in errors such as ``` AttributeErro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
