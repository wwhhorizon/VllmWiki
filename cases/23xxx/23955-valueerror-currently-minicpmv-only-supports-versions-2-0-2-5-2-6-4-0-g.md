# vllm-project/vllm#23955: ValueError: Currently, MiniCPMV only supports versions 2.0, 2.5, 2.6, 4.0. Got version: (4, 5)

| 字段 | 值 |
| --- | --- |
| Issue | [#23955](https://github.com/vllm-project/vllm/issues/23955) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: Currently, MiniCPMV only supports versions 2.0, 2.5, 2.6, 4.0. Got version: (4, 5)

### Issue 正文摘录

I still get the error: pip install -U vllm --pre --extra-index-url https://wheels.vllm.ai/nightly --force-reinstall vllm serve "openbmb/MiniCPM-V-4_5" --tensor-parallel-size=2 --trust-remote-code ... ERROR 08-29 13:40:25 [multiproc_executor.py:559] ValueError: Currently, MiniCPMV only supports versions 2.0, 2.5, 2.6, 4.0. Got version: (4, 5) Running on Debian 12 with Python 3.11. _Originally posted by @ep5000 in https://github.com/vllm-project/vllm/issues/23586#issuecomment-3237765819_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ValueError: Currently, MiniCPMV only supports versions 2.0, 2.5, 2.6, 4.0. Got version: (4, 5) stale I still get the error: pip install -U vllm --pre --extra-index-url https://wheels.vllm.ai/nightly --force-reinstall vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: MiniCPMV only supports versions 2.0, 2.5, 2.6, 4.0. Got version: (4, 5) stale I still get the error: pip install -U vllm --pre --extra-index-url https://wheels.vllm.ai/nightly --force-reinstall vllm serve "openbmb/MiniC...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
