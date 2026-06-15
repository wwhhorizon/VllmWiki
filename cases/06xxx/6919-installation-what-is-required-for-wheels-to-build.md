# vllm-project/vllm#6919: [Installation]: What is required for wheels to build?

| 字段 | 值 |
| --- | --- |
| Issue | [#6919](https://github.com/vllm-project/vllm/issues/6919) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: What is required for wheels to build?

### Issue 正文摘录

### Your current environment Not applicable -- Dockerfile ### How you are installing vllm Wheel building fails with `Unknown runtime environment` inside the call to `get_vllm_version`. Your documentation says: > Requirements >OS: Linux >Python: 3.8 – 3.11 >GPU: compute capability 7.0 or higher (e.g., V100, T4, RTX20xx, A100, L4, H100, etc.) Does the last point mean a GPU has to be present at *build* time? This is problematic when building Docker images, and shouldn't be required. But if it's required, it should at least be documented better. Steps to reproduce. 1. Create a 2-line Dockerfile: ```Dockerfile FROM python:3.11 RUN pip install -vvv vllm ``` 2. Building this Dockerfile results in: ``` [+] Building 27.0s (5/5) FINISHED docker:desktop-linux => [internal] load .dockerignore 0.0s => => transferring context: 2B 0.0s => [internal] load build definition from simple.Dockerfile 0.0s => => transferring dockerfile: 87B 0.0s => [internal] load metadata for docker.io/library/python:3.11 0.5s => CACHED [1/2] FROM docker.io/library/python:3.11@sha256:a46ef4ef9f9d4fee62ad368f9526552a0a99e90882d246cdefe50d356e3a74dd 0.0s => ERROR [2/2] RUN pip install -vvv vllm 26.4s ------ > [2/2] RUN p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: What is required for wheels to build? installation;stale ### Your current environment Not applicable -- Dockerfile ### How you are installing vllm Wheel building fails with `Unknown runtime environment`
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ation says: > Requirements >OS: Linux >Python: 3.8 – 3.11 >GPU: compute capability 7.0 or higher (e.g., V100, T4, RTX20xx, A100, L4, H100, etc.) Does the last point mean a GPU has to be present at *build* time? This is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: stay within GitHub character limit... 2.821 Obtaining dependency information for MarkupSafe>=2.0 from https://files.pythonhosted.org/packages/1c/cf/35fe557e53709e93feb65575c93927942087e9b97213eabc3fe9d5b25a55/MarkupSafe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Installation]: What is required for wheels to build? installation;stale ### Your current environment Not applicable -- Dockerfile ### How you are installing vllm Wheel building fails with `Unknown runtime environment`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tions/sdist.py", line 101, in _get_build_requires_wheel 25.71 return backend.get_requires_for_build_wheel() 25.71 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 25.71 File "/usr/local/lib/python3.11/site-packages/pip/_internal/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
