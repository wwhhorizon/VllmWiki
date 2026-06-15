# vllm-project/vllm#21231: [Bug]: 100% cpu usage on 3 cores on every node when using ray distributed pipeline parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#21231](https://github.com/vllm-project/vllm/issues/21231) |
| 状态 | open |
| 标签 | bug;ray;unstale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 100% cpu usage on 3 cores on every node when using ray distributed pipeline parallel

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using run_cluster.sh to launch ray instances. After serving one inference, the cluster workers have 3 cores each pegged at 100% cpu. I thought this might be the related to the bug fixed by VLLM_SLEEP_WHEN_IDLE or --enable-sleep-mode but that is not having any effect on the ray workers. I'd expect when the cluster is not inferencing, with those parameters, the CPUs can go idle. Below is the vllm process RayWorker class using 300% CPU in top. ``` 271799 root 35 15 507.0g 3.9g 777520 S 281.8 2.4 344:06.51 ray::RayWorkerW ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ny effect on the ray workers. I'd expect when the cluster is not inferencing, with those parameters, the CPUs can go idle. Below is the vllm process RayWorker class using 300% CPU in top. ``` 271799 root 35 15 507.0g 3....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: res on every node when using ray distributed pipeline parallel bug;ray;unstale ### Your current environment ### 🐛 Describe the bug I am using run_cluster.sh to launch ray instances. After serving one inference, the clus...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
