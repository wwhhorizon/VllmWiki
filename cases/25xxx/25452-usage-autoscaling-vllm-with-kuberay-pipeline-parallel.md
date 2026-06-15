# vllm-project/vllm#25452: [Usage]:  Autoscaling vLLM with kuberay (pipeline parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#25452](https://github.com/vllm-project/vllm/issues/25452) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  Autoscaling vLLM with kuberay (pipeline parallel

### Issue 正文摘录

### Your current environment Hello Team, a newbie here in K8, Kuberay, vLLM. Apologies if this question already asked or if this too simple. I am using attached tutorial for "Pipeline parallelism with Kuberay" and it works successfully. https://docs.vllm.ai/projects/production-stack/en/latest/use_cases/pipeline-parallelism-kuberay.html I am moving to the next stage of autoscaling (HPA) and found awesome tutorial https://github.com/vllm-project/production-stack/blob/main/tutorials/10-horizontal-autoscaling.md ### How would you like to use vllm I want to autoscale and could not find any tutorials. Before implementing, I have a couple of questions. 1. Assuming if I set maxReplicas as 2, then will autoscale create one more ray cluster by requesting resources from k8? or will it try to edit existing ray cluster. 2. Also, if it creates a new cluster, do I need the same for nodes (same pipeline parallel and tensor parallel) what I used to deploy the model? 3. What if I have deploy multiple models in the same cluster (all running) than will I have multiple vllm-router-service individual services. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: if this too simple. I am using attached tutorial for "Pipeline parallelism with Kuberay" and it works successfully. https://docs.vllm.ai/projects/production-stack/en/latest/use_cases/pipeline-parallelism-kuberay.html I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Autoscaling vLLM with kuberay (pipeline parallel usage;stale ### Your current environment Hello Team, a newbie here in K8, Kuberay, vLLM. Apologies if this question already asked or if this too simple. I am usi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: zontal-autoscaling.md ### How would you like to use vllm I want to autoscale and could not find any tutorials. Before implementing, I have a couple of questions. 1. Assuming if I set maxReplicas as 2, then will autoscal...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: (same pipeline parallel and tensor parallel) what I used to deploy the model? 3. What if I have deploy multiple models in the same cluster (all running) than will I have multiple vllm-router-service individual services....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: models in the same cluster (all running) than will I have multiple vllm-router-service individual services. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the ch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
