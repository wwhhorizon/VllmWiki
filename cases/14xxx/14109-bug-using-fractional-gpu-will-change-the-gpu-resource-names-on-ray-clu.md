# vllm-project/vllm#14109: [Bug]: Using fractional GPU will change the GPU resource names on Ray cluster nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#14109](https://github.com/vllm-project/vllm/issues/14109) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using fractional GPU will change the GPU resource names on Ray cluster nodes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are trying to deploy two LLMs on a ray cluster with fractional GPUs as a single one will not use all memories of a gpu. This cluster has 6 nodes and each node has one gpu. We found that, after we deploying the 1st LLM, the 2nd will fail with error raised [here](https://github.com/vllm-project/vllm/blob/main/vllm/executor/ray_utils.py#L347-L352) ```sh ValueError: Current node has no GPU available. current_node_resource={ 'accelerator_type:L4': 1.0, 'node:172.31.22.233': 1.0, 'bundle_group_4_4b47a28355f832a07cdeb7a245f703000000': 999.999, 'GPU_group_4_4b47a28355f832a07cdeb7a245f703000000': 0.4, 'CPU': 3.0, 'memory': 10868666368.0, 'GPU_group_4b47a28355f832a07cdeb7a245f703000000': 0.4, 'bundle_group_4b47a28355f832a07cdeb7a245f703000000': 999.999, 'object_store_memory': 4657999872.0}. vLLM engine cannot start without GPU. Make sure you have at least 1 GPU available in a node current_node_id='9b83e3b843e4c0a8f82a0d77995d37e1610d884e0e64fc17cacdb1fb' current_ip='172.31.22.233'. ``` We dig the code little bit and check in out ray system, we found that after we deploying the 1st LLM, somehow the GPU resource name are changed from `gpu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: is? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. performance ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
