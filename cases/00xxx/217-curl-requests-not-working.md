# vllm-project/vllm#217: Curl requests not working 

| 字段 | 值 |
| --- | --- |
| Issue | [#217](https://github.com/vllm-project/vllm/issues/217) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;sampling_logits |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Curl requests not working 

### Issue 正文摘录

Hi there, I had a question regarding working with the API Server from the [instructions](https://vllm.readthedocs.io/en/latest/getting_started/quickstart.html) here. I am running this after running the docker command # Pull the Docker image with CUDA 11.8. `docker run --gpus all -it --rm --shm-size=8g nvcr.io/nvidia/pytorch:22.12-py3 ` and running these commands within the workspace ``` pip uninstall torch pip install vllm ``` When running the default command `python -m vllm.entrypoints.api_server`, the server doesn't connect, returning INFO: Started server process [3820] INFO: Waiting for application startup. INFO: Application startup complete. ERROR: [Errno 99] error while attempting to bind on address ('::1', 8000, 0, 0): cannot assign requested address INFO: Waiting for application shutdown. INFO: Application shutdown complete. I try different ports and it still doesn't work. However, when I try a different host like 127.0.0.1 for instance through the --host parameter, it connects to the server and runs on Uvicorn but I am unable to curl requests to this server. I try to do this by opening a 2nd terminal, running the docker image and the rest of the commands above again and th...

## 现有链接修复摘要

#39925 [Bugfix] DeepEP LL: pass use_fabric for MNNVL cross-node NVLink

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ing_started/quickstart.html) here. I am running this after running the docker command # Pull the Docker image with CUDA 11.8. `docker run --gpus all -it --rm --shm-size=8g nvcr.io/nvidia/pytorch:22.12-py3 ` and running...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ning this after running the docker command # Pull the Docker image with CUDA 11.8. `docker run --gpus all -it --rm --shm-size=8g nvcr.io/nvidia/pytorch:22.12-py3 ` and running these commands within the workspace ``` pip...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Curl requests not working Hi there, I had a question regarding working with the API Server from the [instructions](https://vllm.readthedocs.io/en/latest/getting_started/quickstart.html) here. I am running this after run...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: the API Server from the [instructions](https://vllm.readthedocs.io/en/latest/getting_started/quickstart.html) here. I am running this after running the docker command # Pull the Docker image with CUDA 11.8. `docker run...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39925](https://github.com/vllm-project/vllm/pull/39925) | mentioned | 0.6 | [Bugfix] DeepEP LL: pass use_fabric for MNNVL cross-node NVLink | nMemHandle` - Bump `DEEPEP_COMMIT_HASH` from `73b6ea4` to `9249c25` ([deepseek-ai/DeepEP#217](https://github.com/deepseek-ai/DeepEP/pull/217)) which adds the `use_fabric` paramete… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
