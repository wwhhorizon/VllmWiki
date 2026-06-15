# vllm-project/vllm#19960: [Bug]: the worker node joins successfully for a few seconds and exits without a reason

| 字段 | 值 |
| --- | --- |
| Issue | [#19960](https://github.com/vllm-project/vllm/issues/19960) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: the worker node joins successfully for a few seconds and exits without a reason

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug the ray command is executed by the `vllm/vllm-openai:v0.8.5` image. the command is simplified from the `run_cluster.sh` for debugging. ``` ctr -n k8s.io run --rm --net-host --privileged --runc-binary /usr/local/nvidia/toolkit/nvidia-container-runtime --env NVIDIA_VISIBLE_DEVICES=all --env VLLM_HOST_IP=156.176.0.154 --mount type=bind,src=/datadisk0/hobin,dst=/root/.cache/huggingface,options=rbind:rw docker.io/vllm/vllm-openai:v0.8.5 hobin bash -c "ray start --block --verbose --address=156.176.0.153:6379" ``` the worker node joins join successfully for a few secs and exit without a reason. On the master node, the console prints like this. ```shell root@paas-controller-1:/vllm-workspace# ray status ======== Autoscaler status: 2025-06-22 18:45:44.434933 ======== Node status --------------------------------------------------------------- Active: 1 node_43ceaa6cfd5d34f5d52f7baa5edfe7cb57b2c9afc8c09116acfe6882 1 node_484ca76fc03f637b1e986210cb0b69ac31d12f33457145930ba98f64 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/112.0 CPU 0.0/2.0 GPU...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ind,src=/datadisk0/hobin,dst=/root/.cache/huggingface,options=rbind:rw docker.io/vllm/vllm-openai:v0.8.5 hobin bash -c "ray start --block --verbose --address=156.176.0.153:6379" ``` the worker node joins join successful...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: =156.176.0.154 --mount type=bind,src=/datadisk0/hobin,dst=/root/.cache/huggingface,options=rbind:rw docker.io/vllm/vllm-openai:v0.8.5 hobin bash -c "ray start --block --verbose --address=156.176.0.153:6379" ``` the work...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: bind:rw docker.io/vllm/vllm-openai:v0.8.5 hobin bash -c "ray start --block --verbose --address=156.176.0.153:6379" ``` the worker node joins join successfully for a few secs and exit without a reason. On the master node...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: d_parallel;hardware_porting;model_support;scheduler_memory cuda;operator;triton build_error;crash;nan_inf;oom;slowdown env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
