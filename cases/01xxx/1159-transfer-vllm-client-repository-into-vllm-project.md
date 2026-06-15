# vllm-project/vllm#1159: Transfer vllm-client repository into vllm-project

| 字段 | 值 |
| --- | --- |
| Issue | [#1159](https://github.com/vllm-project/vllm/issues/1159) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Transfer vllm-client repository into vllm-project

### Issue 正文摘录

Hi @WoosukKwon , I've developed a standalone Python client for the vLLM API: - https://github.com/viktor-ferenczi/vllm-client - https://pypi.org/project/vllm-client/ It has tests and example and documented. I already started to use this package in my projects. The reason for a separate Python API client is to allow vLLM user to have minimal dependencies in their Python projects. I am aware that it is possible by just using `requests` directly, but that's more verbose and less convenient, especially for newbies. Delivering a separate HTTP library would also allow for seamless upgrade to a newer vLLM API version should we need one without the clients to do anything than updating the Python package. I think this repository should belong into the `vllm-project` GitHub organization instead of my private GitHub. Could you please consider transferring the above repository or allowing me to do that? Thank you. I've attempted to request a transfer, but it does not work like that: ![image](https://github.com/vllm-project/vllm/assets/1848514/112d31e0-4be7-4006-8887-9aef2f1abf02)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: separate Python API client is to allow vLLM user to have minimal dependencies in their Python projects. I am aware that it is possible by just using `requests` directly, but that's more verbose and less convenient, espe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: in their Python projects. I am aware that it is possible by just using `requests` directly, but that's more verbose and less convenient, especially for newbies. Delivering a separate HTTP library would also allow for se...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tor-ferenczi/vllm-client - https://pypi.org/project/vllm-client/ It has tests and example and documented. I already started to use this package in my projects. The reason for a separate Python API client is to allow vLL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
