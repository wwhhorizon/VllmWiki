# vllm-project/vllm#7131: [RFC]: vLLM plugin system

| 字段 | 值 |
| --- | --- |
| Issue | [#7131](https://github.com/vllm-project/vllm/issues/7131) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: vLLM plugin system

### Issue 正文摘录

### Motivation. There is an increasing need to customize vLLM, including: - out-of-tree model registration, where users want to register their model outside of vLLM repo. This is partially fulfilled by https://github.com/vllm-project/vllm/pull/3871 . But later users find that it does not work in distributed setting with `ray`: https://github.com/vllm-project/vllm/issues/5657 - custom executor class, already added in https://github.com/vllm-project/vllm/pull/6557 - custom scheduler, requested in https://github.com/vllm-project/vllm/issues/7123 - custom tensor parallel implementation, requested in https://github.com/vllm-project/vllm/issues/7124 Usually, the request is to swap out some functions / classes in vLLM, or call some functions before vLLM runs the model. While implementing them in vLLM is not difficult, the maintenaince burden grows. In order to satisfy the growing need of customization, I propose to introduce vLLM plugin system. It is inspired by the pytest [community](https://github.com/pytest-dev/pytest), where a plugin is a standalone pypi package, e.g. https://pypi.org/project/pytest-forked/ . https://github.com/vllm-project/vllm/pull/7130 is a draft implementation, w...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: already added in https://github.com/vllm-project/vllm/pull/6557 - custom scheduler, requested in https://github.com/vllm-project/vllm/issues/7123 - custom tensor parallel implementation, requested in https://github.com/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ges/man8/ld.so.8.html), with a colon-separated list of python modules to import. One of the most important concern, is to fight against [arbitrary code execution](https://en.wikipedia.org/wiki/Arbitrary_code_execution)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: There is an increasing need to customize vLLM, including: - out-of-tree model registration, where users want to register their model outside of vLLM repo. This is partially fulfilled by https://github.com/vllm-project/v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ion, I propose to introduce vLLM plugin system. It is inspired by the pytest [community](https://github.com/pytest-dev/pytest), where a plugin is a standalone pypi package, e.g. https://pypi.org/project/pytest-forked/ ....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
