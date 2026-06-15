# vllm-project/vllm#9226: [Bug]: Could not `pip install vllm` inside dockerfile after certain commit in `main` branch

| 字段 | 值 |
| --- | --- |
| Issue | [#9226](https://github.com/vllm-project/vllm/issues/9226) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Could not `pip install vllm` inside dockerfile after certain commit in `main` branch

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This is actually a follow up from #9152. After I tested every commit to build docker image using this Dockerfile ```dockerfile FROM pytorch/pytorch:2.4.0-cuda12.1-cudnn9-devel AS build ARG GITHASH RUN apt update && apt install gcc g++ git -y && apt clean && rm -rf /var/lib/apt/lists/* ENV PATH=/workspace-lib:/workspace-lib/bin:$PATH ENV PYTHONUSERBASE=/workspace-lib RUN pip install git+https://github.com/vllm-project/vllm.git@${GITHASH} --no-cache-dir --user FROM pytorch/pytorch:2.4.0-cuda12.1-cudnn9-runtime AS vllm-openai WORKDIR /vllm-workspace COPY --from=build /workspace-lib /workspace-lib ENV PATH=/workspace-lib:/workspace-lib/bin:$PATH ENV PYTHONUSERBASE=/workspace-lib ENV PYTHONPATH=/workspace-lib:/vllm-workspace ENTRYPOINT ["python3", "-m", "vllm.entrypoints.openai.api_server"] ``` I found that this particular commit aeb37c2a725554791ff6f258b1e18830867a3ab9 is the culprit. Is there any way to solve this? I already update my Nvidia Driver to the latest but the problem persisted. CC: @LucasWilkinson (author of the mentioned commit) ### Before submitting a new issue... - [X] Make sure you...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Could not `pip install vllm` inside dockerfile after certain commit in `main` branch bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This is actually a follow up from #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er image using this Dockerfile ```dockerfile FROM pytorch/pytorch:2.4.0-cuda12.1-cudnn9-devel AS build ARG GITHASH RUN apt update && apt install gcc g++ git -y && apt clean && rm -rf /var/lib/apt/lists/* ENV PATH=/works...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _build;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: certain commit in `main` branch bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This is actually a follow up from #9152. After I tested every commit to build docker image usin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tly asked questions. development ci_build;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
