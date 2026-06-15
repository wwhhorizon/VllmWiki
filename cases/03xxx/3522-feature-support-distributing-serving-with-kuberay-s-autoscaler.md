# vllm-project/vllm#3522: [Feature]: Support distributing serving with KubeRay's autoscaler

| 字段 | 值 |
| --- | --- |
| Issue | [#3522](https://github.com/vllm-project/vllm/issues/3522) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support distributing serving with KubeRay's autoscaler

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, I'm deploying vLLM distributed serving in a Kubernetes environment. To make it work, I installed [KubeRay](https://github.com/ray-project/kuberay) to help me manage the ray cluster in Kubernetes. vLLM works well when the ray cluster has enough GPU resources. For example, if `ray status` reports that there are 2 GPUs available now, then vLLM launches successfully with the following command: ``` python -m vllm.entrypoints.openai.api_server --trust-remote-code --model /root/vllm-models/ --gpu-memory-utilization 0.95 --tensor-parallel-size 2 ``` I also noticed that KubeRay supports [AutoScaling](https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/configuring-autoscaling.html), so **I would like to leverage the AutoScaling feature to save me more money on GPU instances**. What I expect is that **when there are no more GPUs available in the (kube)ray cluster, launching the vLLM should trigger scaling out some ray worker pods with some available GPU inside it, and wait for ray cluster to schedule its `RayLLMWorker` actors**. I failed with the following message: ``` $ python -m vllm.entrypoints.openai.api_server --trust-remote-code --mo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: vLLM distributed serving in a Kubernetes environment. To make it work, I installed [KubeRay](https://github.com/ray-project/kuberay) to help me manage the ray cluster in Kubernetes. vLLM works well when the ray cluster...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Support distributing serving with KubeRay's autoscaler feature request;stale ### 🚀 The feature, motivation and pitch Hi, I'm deploying vLLM distributed serving in a Kubernetes environment. To make it work, I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ``` python -m vllm.entrypoints.openai.api_server --trust-remote-code --model /root/vllm-models/ --gpu-memory-utilization 0.95 --tensor-parallel-size 2 ``` I also noticed that KubeRay supports [AutoScaling](https://docs....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: server.py:727] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: Support distributing serving with KubeRay's autoscaler feature request;stale ### 🚀 The feature, motivation and pitch Hi, I'm deploying vLLM distributed serving in a Kubernetes environment. To make it work, I i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
