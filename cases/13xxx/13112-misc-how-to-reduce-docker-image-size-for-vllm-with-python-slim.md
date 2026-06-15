# vllm-project/vllm#13112: [Misc]: How to reduce docker image size for vllm with python-slim?

| 字段 | 值 |
| --- | --- |
| Issue | [#13112](https://github.com/vllm-project/vllm/issues/13112) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: How to reduce docker image size for vllm with python-slim?

### Issue 正文摘录

I am building a custom docker image using python-slim as the base, for spinning up an openAI compatible server using vllm and our custom LLM. This is the Dockerfile so far: ``` FROM python:3.12-slim RUN pip install --no-cache-dir vllm ENTRYPOINT ["sh", "-c", "python3 -m vllm.entrypoints.openai.api_server --model] ``` Everything works. But the docker image is 7.07 GB in size. I used 'no-cache-dir' to bring the size down from 10.6GB to 7.07GB. The bulk of the size seems to be coming from all the dependencies of vllm. Is there any way I can reduce the image size further? Is there a way to be more selective about what parts of vllm my project will need/use, and only download those with some sort of flag? ``` Permission UID:GID Size Filetree drwxr-xr-x 0:0 7.1 GB ├── usr drwxr-xr-x 0:0 7.0 GB │ ├── local drwxr-xr-x 0:0 7.0 GB │ │ ├── lib drwxr-xr-x 0:0 7.0 GB │ │ │ ├── python3.12 drwxr-xr-x 0:0 6.9 GB │ │ │ │ ├── site-packages drwxr-xr-x 0:0 2.9 GB │ │ │ │ │ ├─⊕ nvidia drwxr-xr-x 0:0 1.8 GB │ │ │ │ │ ├─⊕ torch drwxr-xr-x 0:0 811 MB │ │ │ │ │ ├─⊕ vllm drwxr-xr-x 0:0 581 MB │ │ │ │ │ ├─⊕ triton drwxr-xr-x 0:0 184 MB │ │ │ │ │ ├─⊕ ray ``` ### Before submitting a new issue... - [x] Make su...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Misc]: How to reduce docker image size for vllm with python-slim? I am building a custom docker image using python-slim as the base, for spinning up an openAI compatible server using vllm and our custom LLM. This is th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: drwxr-xr-x 0:0 581 MB │ │ │ │ │ ├─⊕ triton drwxr-xr-x 0:0 184 MB │ │ │ │ │ ├─⊕ ray ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ENTRYPOINT ["sh", "-c", "python3 -m vllm.entrypoints.openai.api_server --model] ``` Everything works. But the docker image is 7.07 GB in size. I used 'no-cache-dir' to bring the size down from 10.6GB to 7.07GB. The bulk...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;model_support triton env_depen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
