# vllm-project/vllm#12572: [Bug]: Ray/vLLM RuntimeError: HIP error: invalid device ordinal

| 字段 | 值 |
| --- | --- |
| Issue | [#12572](https://github.com/vllm-project/vllm/issues/12572) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ray/vLLM RuntimeError: HIP error: invalid device ordinal

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Assume a cluster of MI250X or MI300X, 8 per node, many nodes. I allocate the nodes and start a ray cluster on them. Ray status is ok, all is fine. Then I connect to a compute node and start vllm like so: ``` $ vllm serve \ --distributed-executor-backend="ray" \ --device="cuda" \ --task="generate" \ --tensor-parallel-size 2 \ --pipeline-parallel-size 1 ``` This should request 2 gpus on one node and start serving. For that, Ray will allocate two GPUs and "start" 1 rank, not 2 because we seem to be reusing the original vllm rank for that purpose (that causes problems too but that for a future issue/feature request). Then it gets messy. The original vllm rank, the one we started using the command above, will operate with the following environment variable: ``` CUDA_VISIBLE_DEVICES="0,1" ``` That is, we restrict the visibility of this rank to 2 GPUs (represented by identifier 0 and 1) of a node. Now, the second rank will see the following env variables: ``` ROCR_VISIBLE_DEVICES="1" CUDA_VISIBLE_DEVICES="0,1" ``` This is obviously a cause for concern, as documented on this HPC site's documentation. h...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Ray/vLLM RuntimeError: HIP error: invalid device ordinal bug;ray;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Assume a cluster of MI250X or MI300X, 8 per node, man...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: se for concern, as documented on this HPC site's documentation. https://dci.dci-gitlab.cines.fr/webextranet/software_stack/libraries/index.html#id8, paraphrasing: ``` export ROCR_VISIBLE_DEVICES= Same as ${HIP_VISIBLE_D...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: and start vllm like so: ``` $ vllm serve \ --distributed-executor-backend="ray" \ --device="cuda" \ --task="generate" \ --tensor-parallel-size 2 \ --pipeline-parallel-size 1 ``` This should request 2 gpus on one node an...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Ray/vLLM RuntimeError: HIP error: invalid device ordinal bug;ray;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Assume a cluster of MI250X or MI300X, 8 per node, man...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nvalid device ordinal bug;ray;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Assume a cluster of MI250X or MI300X, 8 per node, many nodes. I allocate the nodes and start a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
