# vllm-project/vllm#15529: [Usage]: Qwen2.5-VL-32B-Instruct 4卡4090启动报错

| 字段 | 值 |
| --- | --- |
| Issue | [#15529](https://github.com/vllm-project/vllm/issues/15529) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | gemm |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Qwen2.5-VL-32B-Instruct 4卡4090启动报错

### Issue 正文摘录

### Your current environment ```text vllm serve /data/models/Qwen2.5-VL-32B-Instruct --limit-mm-per-prompt image=2 --tensor-parallel-size 4 --served-model-name Qwen2.5-VL-32B-Instruct --max-model-len 8192 --gpu-memory-utilization 0.99 ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Qwen2.5-VL-32B-Instruct 4卡4090启动报错 usage;stale ### Your current environment ```text vllm serve /data/models/Qwen2.5-VL-32B-Instruct --limit-mm-per-prompt image=2 --tensor-parallel-size 4 --served-model-name Qwe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: equently asked questions. performance distributed_parallel;model_support gemm #43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Qwen2.5-VL-32B-Instruct 4卡4090启动报错 usage;stale ### Your current environment ```text vllm serve /data/models/Qwen2.5-VL-32B-Instruct --limit-mm-per-prompt image=2 --tensor-parallel-size 4 --served-model-name Qwe...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 145 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15529">#15529</a> by <a href="https://github.com/tiangolo"><code>@​tiangolo</code></a>.</li> <li>🌐 Update translatio… |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 147 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15529">#15529</a> by <a href="https://github.com/tiangolo"><code>@​tiangolo</code></a>.</li> <li>🌐 Update translatio… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
