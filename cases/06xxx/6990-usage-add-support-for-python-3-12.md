# vllm-project/vllm#6990: [Usage]: Add support for Python 3.12

| 字段 | 值 |
| --- | --- |
| Issue | [#6990](https://github.com/vllm-project/vllm/issues/6990) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Add support for Python 3.12

### Issue 正文摘录

### Your current environment ## Request for Python 3.12 Support ### Background I am currently using the vllm engine for my project, and I noticed that it does not support Python 3.12. Given that Python 3.12 includes several new features and performance improvements, it would be beneficial for this repository to support it. ### Additional Information If there are any blockers or specific reasons why Python 3.12 is not currently supported, please let me know. I am willing to help with testing or any other tasks necessary to add support for this version. Thank you for your consideration. ### How would you like to use vllm _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: des several new features and performance improvements, it would be beneficial for this repository to support it. ### Additional Information If there are any blockers or specific reasons why Python 3.12 is not currently...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: repository to support it. ### Additional Information If there are any blockers or specific reasons why Python 3.12 is not currently supported, please let me know. I am willing to help with testing or any other tasks nec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: would be beneficial for this repository to support it. ### Additional Information If there are any blockers or specific reasons why Python 3.12 is not currently supported, please let me know. I am willing to help with t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: age]: Add support for Python 3.12 usage ### Your current environment ## Request for Python 3.12 Support ### Background I am currently using the vllm engine for my project, and I noticed that it does not support Python 3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: s not currently supported, please let me know. I am willing to help with testing or any other tasks necessary to add support for this version. Thank you for your consideration. ### How would you like to use vllm _No res...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
