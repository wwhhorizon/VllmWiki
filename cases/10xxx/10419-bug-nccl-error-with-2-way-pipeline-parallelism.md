# vllm-project/vllm#10419: [Bug]: NCCL error with 2-way pipeline parallelism.

| 字段 | 值 |
| --- | --- |
| Issue | [#10419](https://github.com/vllm-project/vllm/issues/10419) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NCCL error with 2-way pipeline parallelism.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to serve an LLM (I have tried both `facebook/opt-125m` and `llama/Meta-Llama-3-8B`) in a distributed environment with 2 nodes and 8 A10G GPUs per node (`g5.48xlarge` AWS instances). I am using the provided helper script (https://github.com/vllm-project/vllm/blob/main/examples/run_cluster.sh) to launch the ray cluster as follows: On node 0 (N0) ``` bash run_cluster.sh vllm/vllm-openai 172.31.41.232 --head $HF_MODEL_REPO ``` On node 1 (N1) ``` bash run_cluster.sh vllm/vllm-openai 172.31.41.232 --worker $HF_MODEL_REPO ``` The `ray status` from within the container command successfully reports the 2 nodes: ``` (base) pl4tinum@awsA10G:~$ docker exec -ti node bash root@awsA10GN0:/vllm-workspace# ray status ======== Autoscaler status: 2024-11-18 02:59:20.884053 ======== Node status --------------------------------------------------------------- Active: 1 node_ae301c60fd664cb2726b719c713f237b85745ad547328dc75535dec0 1 node_5201b98fefd78033c9580c794d5e4c12c666af31e50905174fc8ded8 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: command successfully reports the 2 nodes: ``` (base) pl4tinum@awsA10G:~$ docker exec -ti node bash root@awsA10GN0:/vllm-workspace# ray status ======== Autoscaler status: 2024-11-18 02:59:20.884053 ======== Node status -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: NCCL error with 2-way pipeline parallelism. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to serve an LLM (I have tried both `facebook/opt-125m` and `llam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 2-way pipeline parallelism. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to serve an LLM (I have tried both `facebook/opt-125m` and `llama/Meta-Llama-3-8B`) in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ec -ti node bash root@awsA10GN0:/vllm-workspace# ray status ======== Autoscaler status: 2024-11-18 02:59:20.884053 ======== Node status --------------------------------------------------------------- Active: 1 node_ae30...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
