# vllm-project/vllm#15376: [Bug]: VLLM Build Using Docker Error Deploy

| 字段 | 值 |
| --- | --- |
| Issue | [#15376](https://github.com/vllm-project/vllm/issues/15376) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM Build Using Docker Error Deploy

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have a Dockerfile like this ```dockerfile FROM pytorch/pytorch:2.6.0-cuda12.6-cudnn9-devel AS build RUN apt update && apt install gcc g++ git -y && apt clean && rm -rf /var/lib/apt/lists/* ENV PATH=/workspace-lib:/workspace-lib/bin:$PATH ENV PYTHONUSERBASE=/workspace-lib RUN pip install git+https://github.com/fahadh4ilyas/vllm.git@stable-oarfish bitsandbytes --no-cache-dir --user FROM pytorch/pytorch:2.6.0-cuda12.6-cudnn9-runtime AS vllm-openai RUN apt update && apt install gcc g++ -y && apt clean && rm -rf /var/lib/apt/lists/* WORKDIR /vllm-workspace COPY --from=build /workspace-lib /workspace-lib ENV PATH=/workspace-lib:/workspace-lib/bin:$PATH ENV PYTHONUSERBASE=/workspace-lib ENV PYTHONPATH=/workspace-lib:/vllm-workspace ENTRYPOINT ["python3", "-m", "vllm.entrypoints.openai.api_server"] ``` The branch is based on tag v0.8.1. After build the docker using this command: ```bash docker build -t vllm-test:1.8.1 --no-cache --progress=plain . ``` The build is successfully done! But, if I tried to run the docker image ```bash docker run -d -t --name test-vllm vllm-test:1.8.1 ``` The docker container wont be run and I got this error...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: VLLM Build Using Docker Error Deploy bug;stale ### Your current environment ### 🐛 Describe the bug I have a Dockerfile like this ```dockerfile FROM pytorch/pytorch:2.6.0-cuda12.6-cudnn9-devel AS build RUN apt upd...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: I have a Dockerfile like this ```dockerfile FROM pytorch/pytorch:2.6.0-cuda12.6-cudnn9-devel AS build RUN apt update && apt install gcc g++ git -y && apt clean && rm -rf /var/lib/apt/lists/* ENV PATH=/workspace-lib:/wor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: VLLM Build Using Docker Error Deploy bug;stale ### Your current environment ### 🐛 Describe the bug I have a Dockerfile like this ```dockerfile FROM pytorch/pytorch:2.6.0-cuda12.6-cudnn9-devel AS build RUN apt upd...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: te-packages/vllm/executor/executor_base.py", line 16, in from vllm.model_executor.layers.sampler import SamplerOutput File "/workspace-lib/lib/python3.11/site-packages/vllm/model_executor/layers/sampler.py", line 23, in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: After build the docker using this command: ```bash docker build -t vllm-test:1.8.1 --no-cache --progress=plain . ``` The build is successfully done! But, if I tried to run the docker image ```bash docker run -d -t --nam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
