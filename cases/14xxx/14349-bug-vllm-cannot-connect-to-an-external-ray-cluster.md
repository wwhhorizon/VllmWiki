# vllm-project/vllm#14349: [Bug]: vllm cannot connect to an external ray cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#14349](https://github.com/vllm-project/vllm/issues/14349) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm cannot connect to an external ray cluster

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I started a ray cluster on the GPU machine using the following command: ```` head node: ray start --head --port=6888 --block worker node: ray start --address=192.168.1.67:6888 --block ray status: # ray status Node status --------------------------------------------------------------- Active: 1 node_b913fef1fe5d495c327117aaf64a74c3435fc708c2a1091c47aea7c9 1 node_eef046d01ec2a7b4e22456feedaf9e31647d1d258d2652413416ca5b ```` Next, I start an llm through vllm serve and want to use this cluster to start it. My startup command is as follows: ```` # echo $RAY_ADDRESS ray://192.168.1.67:10001 # echo $VLLM_HOST_IP 192.168.1.69 root@d94e8f69d9c0:/vllm-workspace# vllm serve /data/llm_models/DeepSeek-R1-Distill-Qwen-14B --tensor-parallel-size 1 --pipeline-parallel-size 2 ```` However, vllm cannot start the service normally, and the error log is as follows: He prompted me with this error: `Ray has not been started yet. You can start Ray with 'ray.init()'` But my ray cluster is normal, and I can submit jobs in the following way: ```` >>> import ray >>> >>> # This will connect to the cluster via the open SSH session. >>> ray.init("ray://192.168...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: cluster is normal, and I can submit jobs in the following way: ```` >>> import ray >>> >>> # This will connect to the cluster via the open SSH session. >>> ray.init("ray://192.168.1.67:10001") 2025-03-06 17:48:34,162 IN...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _IP 192.168.1.69 root@d94e8f69d9c0:/vllm-workspace# vllm serve /data/llm_models/DeepSeek-R1-Distill-Qwen-14B --tensor-parallel-size 1 --pipeline-parallel-size 2 ```` However, vllm cannot start the service normally, and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ng the following command: ```` head node: ray start --head --port=6888 --block worker node: ray start --address=192.168.1.67:6888 --block ray status: # ray status Node status --------------------------------------------...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm cannot connect to an external ray cluster bug;ray;stale ### Your current environment ### 🐛 Describe the bug I started a ray cluster on the GPU machine using the following command: ```` head node: ray start -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
