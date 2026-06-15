# vllm-project/vllm#3923: [Feature]: Add CPU support for openai entrypoint

| 字段 | 值 |
| --- | --- |
| Issue | [#3923](https://github.com/vllm-project/vllm/issues/3923) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add CPU support for openai entrypoint

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am working on using VLLM to enable model inferencing on CPU skus. The latest release allowed for offline batched inferencing on CPUs however, the entrypoints (i.e vllm.entrypoints.openai.api_server.py and vllm.entrypoints.api_server.py) only work on GPUs. I would like to add support for CPUs to use those entrypoints ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: motivation and pitch I am working on using VLLM to enable model inferencing on CPU skus. The latest release allowed for offline batched inferencing on CPUs however, the entrypoints (i.e vllm.entrypoints.openai.api_serve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: The feature, motivation and pitch I am working on using VLLM to enable model inferencing on CPU skus. The latest release allowed for offline batched inferencing on CPUs however, the entrypoints (i.e vllm.entrypoints.ope...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add CPU support for openai entrypoint feature request ### 🚀 The feature, motivation and pitch I am working on using VLLM to enable model inferencing on CPU skus. The latest release allowed for offline batched...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: am working on using VLLM to enable model inferencing on CPU skus. The latest release allowed for offline batched inferencing on CPUs however, the entrypoints (i.e vllm.entrypoints.openai.api_server.py and vllm.entrypoin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
