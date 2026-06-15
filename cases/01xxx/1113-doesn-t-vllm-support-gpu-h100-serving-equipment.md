# vllm-project/vllm#1113: Doesn't vllm support GPU H100 serving equipment?

| 字段 | 值 |
| --- | --- |
| Issue | [#1113](https://github.com/vllm-project/vllm/issues/1113) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Doesn't vllm support GPU H100 serving equipment?

### Issue 正文摘录

Hello developers, I am leaving an issue because I am getting an unresolved error while serving using the H100 device. I checked that the server is up and running and the input queries are communicated, but I am getting a 500 Internal Server Error. The container image I'm using is **thebloke/cuda11.8.0-ubuntu22.04-pytorch** First of all, the machine I am using is "NVIDIA H100" and the error I am facing is **RuntimeError: CUDA error: no kernel image is available for execution on the device Compile with 'TORCH_USE_CUDA_DSA' to enable device-side assertions.** This is where the error occurred: vllm/model_executor/paraller_utils/tensor_parallel/layers.py, line 361, in forward output = output_ + self.bias if self.bias is not None else output_ If you have a workaround for this error, I would really appreciate your advice... plz..

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates | #43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rst of all, the machine I am using is "NVIDIA H100" and the error I am facing is **RuntimeError: CUDA error: no kernel image is available for execution on the device Compile with 'TORCH_USE_CUDA_DSA' to enable device-si...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Doesn't vllm support GPU H100 serving equipment? Hello developers, I am leaving an issue because I am getting an unresolved error while serving using the H100 device. I checked that the server is up and running and the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e 361, in forward output = output_ + self.bias if self.bias is not None else output_ If you have a workaround for this error, I would really appreciate your advice... plz.. development ci_build;distributed_parallel;fron...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: enable device-side assertions.** This is where the error occurred: vllm/model_executor/paraller_utils/tensor_parallel/layers.py, line 361, in forward output = output_ + self.bias if self.bias is not None else output_ If...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 140 updates | href="https://redirect.github.com/prometheus/client_python/pull/1113">prometheus/client_python#1113</a></li> <li><a href="https://github.com/aadityadhruv"><code>@​aadityadhruv</co… |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | href="https://redirect.github.com/prometheus/client_python/pull/1113">prometheus/client_python#1113</a></li> <li><a href="https://github.com/aadityadhruv"><code>@​aadityadhruv</co… |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | href="https://redirect.github.com/prometheus/client_python/pull/1113">prometheus/client_python#1113</a></li> <li><a href="https://github.com/aadityadhruv"><code>@​aadityadhruv</co… |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | href="https://redirect.github.com/prometheus/client_python/pull/1113">prometheus/client_python#1113</a></li> <li><a href="https://github.com/aadityadhruv"><code>@​aadityadhruv</co… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | href="https://redirect.github.com/prometheus/client_python/pull/1113">prometheus/client_python#1113</a></li> <li><a href="https://github.com/aadityadhruv"><code>@​aadityadhruv</co… |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 145 updates | href="https://redirect.github.com/prometheus/client_python/pull/1113">prometheus/client_python#1113</a></li> <li>Improve parser performance by <a href="https://github.com/csmarchb… |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 147 updates | href="https://redirect.github.com/prometheus/client_python/pull/1113">prometheus/client_python#1113</a></li> <li>Improve parser performance by <a href="https://github.com/csmarchb… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
