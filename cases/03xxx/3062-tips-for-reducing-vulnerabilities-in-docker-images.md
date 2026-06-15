# vllm-project/vllm#3062: Tips for reducing vulnerabilities in docker images

| 字段 | 值 |
| --- | --- |
| Issue | [#3062](https://github.com/vllm-project/vllm/issues/3062) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Tips for reducing vulnerabilities in docker images

### Issue 正文摘录

The Docker images produced by vLLM project have > 100 vulnerabilities ![image](https://github.com/vllm-project/vllm/assets/1972276/0c261765-fde2-4deb-8ca9-97ce3f346217) These mostly come from the dependency on a full ubuntu base image. This base image is great because it allows for installation of CUDA and other GPU dependencies. It's difficult to find distroless cuda-ready images. This issue is a request to find/create an image like that (preferably) or to reduce the vulnerabilities some other way, such as uninstalling unused ubuntu utils.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Tips for reducing vulnerabilities in docker images The Docker images produced by vLLM project have > 100 vulnerabilities ![image](https://github.com/vllm-project/vllm/assets/1972276/0c261765-fde2-4deb-8ca9-97ce3f346217)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e image. This base image is great because it allows for installation of CUDA and other GPU dependencies. It's difficult to find distroless cuda-ready images. This issue is a request to find/create an image like that (pr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: . It's difficult to find distroless cuda-ready images. This issue is a request to find/create an image like that (preferably) or to reduce the vulnerabilities some other way, such as uninstalling unused ubuntu utils.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
