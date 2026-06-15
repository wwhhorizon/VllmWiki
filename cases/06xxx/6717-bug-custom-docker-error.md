# vllm-project/vllm#6717: [Bug]: custom docker Error

| 字段 | 值 |
| --- | --- |
| Issue | [#6717](https://github.com/vllm-project/vllm/issues/6717) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: custom docker Error

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Differences between docker and local in docker: ``` CUDA runtime version:Could not collect cuDNN version: 9.0.0 ``` in host: ``` CUDA runtime version: 12.3.52 cuDNN version: 8.5.0 ``` v100 16G * 4 ### 🐛 Describe the bug in host, it's ok. but it's error in docker. base docker: nvidia/cuda:12.3.2-cudnn9-runtime-centos7 code: https://github.com/THUDM/GLM-4/blob/main/basic_demo/openai_api_server.py modify `tensor_parallel_size=1` to `tensor_parallel_size=2` CUDA_VISIBLE_DEVICES=0,1 requirements: torch==2.3.0 fastapi==0.111.0 transformers==4.41.2 vllm==0.4.3 sse-starlette=2.1.0 error in `init_device` I found why is NCCL_CHECK return 2 not 0. How do I fix this bug? In docker_run.sh docker run -- runtime nvidia --gpus all --rm --shm-size=30gb --privileged -e CUDA_VISIBLE_DEVICES=0,1 xxxxx like this

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: custom docker Error bug;unstale ### Your current environment ```text The output of `python collect_env.py` ``` Differences between docker and local in docker: ``` CUDA runtime version:Could not collect cuDNN vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: collect_env.py` ``` Differences between docker and local in docker: ``` CUDA runtime version:Could not collect cuDNN version: 9.0.0 ``` in host: ``` CUDA runtime version: 12.3.52 cuDNN version: 8.5.0 ``` v100 16G * 4 ##...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: custom docker Error bug;unstale ### Your current environment ```text The output of `python collect_env.py` ``` Differences between docker and local in docker: ``` CUDA runtime version:Could not collect cuDNN vers...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
