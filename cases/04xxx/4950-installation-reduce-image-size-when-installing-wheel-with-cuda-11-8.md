# vllm-project/vllm#4950: [Installation]: Reduce Image size when installing wheel with cuda 11.8

| 字段 | 值 |
| --- | --- |
| Issue | [#4950](https://github.com/vllm-project/vllm/issues/4950) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Reduce Image size when installing wheel with cuda 11.8

### Issue 正文摘录

### Your current environment Hello, when the Python Wheel is installed according to your documentation: https://docs.vllm.ai/en/latest/getting_started/installation.html#install-with-pip The image size of a Docker Container adds up to 10GB, which is a lot for some Container Registries. Is there any alternative to reduce the image size of the Container Image to less then 5 GB? Because the Image what you are proving at the Docker Registry, is much smaller. ``` REPOSITORY TAG IMAGE ID CREATED SIZE vllmtest5 latest d86273b9420d 2 minutes ago 7.9GB ``` ### How you are installing vllm _Dockerfile_ ``` FROM nvidia/cuda:11.8.0-base-ubuntu22.04 AS vllm-base ARG VLLM_VERSION=0.4.2 ARG VLLM_PYTHON_VERSION=310 WORKDIR /vllm-workspace RUN apt-get update -y \ && apt-get install -y python3-pip \ && apt-get clean && apt-get autoremove --yes \ && rm -rf /tmp/* && rm -rf /var/lib/{apt,dpkg,cache,log} # Workaround for https://github.com/openai/triton/issues/2507 and # https://github.com/pytorch/pytorch/issues/107960 -- hopefully # this won't be needed for future versions of this docker image # or future versions of triton. RUN ldconfig /usr/local/cuda-11.8/compat/ # install vllm wheel first, so that...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: Reduce Image size when installing wheel with cuda 11.8 installation;stale ### Your current environment Hello, when the Python Wheel is installed according to your documentation: https://docs.vllm.ai/en/la
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: Reduce Image size when installing wheel with cuda 11.8 installation;stale ### Your current environment Hello, when the Python Wheel is installed according to your documentation: https://docs.vllm.ai/en/l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: var/lib/{apt,dpkg,cache,log} # Workaround for https://github.com/openai/triton/issues/2507 and # https://github.com/pytorch/pytorch/issues/107960 -- hopefully # this won't be needed for future versions of this docker im...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ture versions of this docker image # or future versions of triton. RUN ldconfig /usr/local/cuda-11.8/compat/ # install vllm wheel first, so that torch etc will be installed RUN python3 -m pip install --upgrade pip RUN p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: on]: Reduce Image size when installing wheel with cuda 11.8 installation;stale ### Your current environment Hello, when the Python Wheel is installed according to your documentation: https://docs.vllm.ai/en/latest/getti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
