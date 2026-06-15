# vllm-project/vllm#3271: High CPU Usage in Kubernetes with Double T4 Running Zephyr 7b Model

| 字段 | 值 |
| --- | --- |
| Issue | [#3271](https://github.com/vllm-project/vllm/issues/3271) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> High CPU Usage in Kubernetes with Double T4 Running Zephyr 7b Model

### Issue 正文摘录

Thanks for your wonderful work. I am using below docker file to build image > FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04 > RUN apt-get update \ > && apt-get -yqq upgrade \ > && apt-get -yqq install python3-pip python-is-python3 \ > && apt-get -qqy autoremove --purge \ > && apt-get clean \ > && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \ > && rm -rf /usr/share/man > > COPY requirements.txt requirements.txt > RUN pip3 install -r requirements.txt \ > && pip3 cache purge > > ENTRYPOINT ["python","-m", "vllm.entrypoints.openai.api_server"] Utilizing the above image, we create a pod with ample resources, including 2 T4 GPUs, 8 vCPUs, and 32GB RAM. However, after receiving several requests (sometimes even at starting of pod itself and at no request), the CPU usage spikes significantly to around 1400-1500%. Surprisingly, it does not decrease during idle periods. Could you please help me to resolve the issue.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Zephyr 7b Model stale Thanks for your wonderful work. I am using below docker file to build image > FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04 > RUN apt-get update \ > && apt-get -yqq upgrade \ > && apt-get -yqq instal...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: High CPU Usage in Kubernetes with Double T4 Running Zephyr 7b Model stale Thanks for your wonderful work. I am using below docker file to build image > FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04 > RUN apt-get update \...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: erful work. I am using below docker file to build image > FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04 > RUN apt-get update \ > && apt-get -yqq upgrade \ > && apt-get -yqq install python3-pip python-is-python3 \ > && apt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: High CPU Usage in Kubernetes with Double T4 Running Zephyr 7b Model stale Thanks for your wonderful work. I am using below docker file to build image > FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04 > RUN apt-get update \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
