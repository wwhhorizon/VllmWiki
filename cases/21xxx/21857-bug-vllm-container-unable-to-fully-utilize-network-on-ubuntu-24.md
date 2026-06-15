# vllm-project/vllm#21857: [Bug]: vllm Container Unable To Fully Utilize Network On Ubuntu 24

| 字段 | 值 |
| --- | --- |
| Issue | [#21857](https://github.com/vllm-project/vllm/issues/21857) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: vllm Container Unable To Fully Utilize Network On Ubuntu 24

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **This requires a bit of context:** I am running a Kubernetes cluster with multiple nodes and GPUs respectively. While testing multi-node models through vllm on the cluster, I decided to inspect the pods running it to test their network performance. Most of the cluster is capable of supporting 400 Gbps of data transfer through their network cards and a test with the mlabbe/iperf3 image from docker confirmed it can with the current setup. When testing iperf3 within the vllm image, I had noticed that the speed drops to around 40 Gbps at most, a tenth of the normal capacity I've seen from other pods within the cluster. I have a suspicion on what it could be, as the nodes of the cluster are running with Ubuntu 24, and I've noticed older Ubuntu images of 22 suffer from this exact problem when running iperf3 through them. **The bug:** From what I've stated above, I believe the massive decrease in Gbps from a container created from the vllm image, is potentially a bug as it should be fairly close to the expected 400 Gbps I should be seeing instead of 40 Gbps. ### Before submitting a new issue... - [x] Make sure you already searched for...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tively. While testing multi-node models through vllm on the cluster, I decided to inspect the pods running it to test their network performance. Most of the cluster is capable of supporting 400 Gbps of data transfer thr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ps. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm Container Unable To Fully Utilize Network On Ubuntu 24 bug;stale ### Your current environment ### 🐛 Describe the bug **This requires a bit of context:** I am running a Kubernetes cluster with multiple nodes...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ster with multiple nodes and GPUs respectively. While testing multi-node models through vllm on the cluster, I decided to inspect the pods running it to test their network performance. Most of the cluster is capable of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
