# vllm-project/vllm#1218: Support Python 3.12

| 字段 | 值 |
| --- | --- |
| Issue | [#1218](https://github.com/vllm-project/vllm/issues/1218) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support Python 3.12

### Issue 正文摘录

[Python 3.12](https://docs.python.org/3.12/whatsnew/3.12.html) releases next week, [Monday 2023-10-02](https://peps.python.org/pep-0693/). It would be great if vLLM could support Python 3.12 fully, including testing in CI and wheels uploaded [to PyPI](https://pypi.org/project/vllm/#files).

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d be great if vLLM could support Python 3.12 fully, including testing in CI and wheels uploaded [to PyPI](https://pypi.org/project/vllm/#files).
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Support Python 3.12 feature request [Python 3.12](https://docs.python.org/3.12/whatsnew/3.12.html) releases next week, [Monday 2023-10-02](https://peps.python.org/pep-0693/). It would be great if vLLM could support Pyth...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: /). It would be great if vLLM could support Python 3.12 fully, including testing in CI and wheels uploaded [to PyPI](https://pypi.org/project/vllm/#files).

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
