# vllm-project/vllm#8074: [Feature]: Support multi-node serving on Kubernetes

| 字段 | 值 |
| --- | --- |
| Issue | [#8074](https://github.com/vllm-project/vllm/issues/8074) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support multi-node serving on Kubernetes

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, I'm currently working on **deploying vLLM distributed on multi-node in k8s cluster**. I saw that the official documentation provided a link by using [LWS](https://github.com/kubernetes-sigs/lws/tree/main) to deploy vllm for distributed model serving. The [KubeRay](https://github.com/ray-project/kuberay) team also provided a solution for multi-node deployment by using Ray Serve. But **neither of these** solutions has been integrated into the vllm codebase. I was wondering if there are any development plans in it for vllm offcial team? If so, I am willing to provide relevant support in terms of code. ### Alternatives I have tried [ray service example](https://docs.ray.io/en/latest/serve/tutorials/vllm-example.html) to deploy a 2-node serving. And it supposes to work. But there are some parts of the code need to be modified to be compatible with the latest version of vLLM. The **related works** are listed below: > - #3522 > - The [Guide](https://github.com/kubernetes-sigs/lws/tree/main/docs/examples/vllm) for deploying distributed inference service with vLLM by using LWS > - The [example](https://docs.ray.io/en/latest/serve/tutorials/vllm-e...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ying vLLM distributed on multi-node in k8s cluster**. I saw that the official documentation provided a link by using [LWS](https://github.com/kubernetes-sigs/lws/tree/main) to deploy vllm for distributed model serving....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support multi-node serving on Kubernetes feature request;stale ### 🚀 The feature, motivation and pitch Hi, I'm currently working on **deploying vLLM distributed on multi-node in k8s cluster**. I saw that the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: github.com/kubernetes-sigs/lws/tree/main) to deploy vllm for distributed model serving. The [KubeRay](https://github.com/ray-project/kuberay) team also provided a solution for multi-node deployment by using Ray Serve. B...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: lternatives I have tried [ray service example](https://docs.ray.io/en/latest/serve/tutorials/vllm-example.html) to deploy a 2-node serving. And it supposes to work. But there are some parts of the code need to be modifi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
