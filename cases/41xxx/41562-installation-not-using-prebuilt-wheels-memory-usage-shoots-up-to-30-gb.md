# vllm-project/vllm#41562: [Installation]: not using prebuilt wheels + memory usage shoots up to 30+GB

| 字段 | 值 |
| --- | --- |
| Issue | [#41562](https://github.com/vllm-project/vllm/issues/41562) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: not using prebuilt wheels + memory usage shoots up to 30+GB

### Issue 正文摘录

### Your current environment This seems to be a two-fold problem: 1. the pre-built wheels are not being used from pypi and I do not understand why; 2. as it decides to build, it goes greedily out of memory. Can't run `collect_env` since I can't get the library installed (just `wget` and running python does not work since that script contains `regex` and `vllm` dependencies) but: - AlmaLinux 9.7 - CUDA 13.0 - Make 4.3 - 32GB of memory; nvidia L40S I cleared the cache completely (pip, torch, triton, vllm) and created a fresh uv environment. I execute the command as recommended in the documentation: ```sh uv pip install vllm --torch-backend=auto ``` Initially everything goes fine but then as soon as the CUDA building kicks in (cudafe++), something along the lines of ```sh cudafe++ --c++17 ==static-host-stub --device-hidden-visibility --gnu_version=110500 ... ``` This fills the memory, going into swap and ultimately hard-freezing the system. I am puzzled why it is not using pre-built wheels. ### How you are installing vllm ```sh uv pip install vllm --torch-backend=auto uv pip install vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: not using prebuilt wheels + memory usage shoots up to 30+GB installation ### Your current environment This seems to be a two-fold problem: 1. the pre-built wheels are not being used from pypi and I do not
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 2GB of memory; nvidia L40S I cleared the cache completely (pip, torch, triton, vllm) and created a fresh uv environment. I execute the command as recommended in the documentation: ```sh uv pip install vllm --torch-backe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: script contains `regex` and `vllm` dependencies) but: - AlmaLinux 9.7 - CUDA 13.0 - Make 4.3 - 32GB of memory; nvidia L40S I cleared the cache completely (pip, torch, triton, vllm) and created a fresh uv environment. I...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: questions. performance ci_build;scheduler_memory cuda;triton build_error;oom env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hich can answer lots of frequently asked questions. performance ci_build;scheduler_memory cuda;triton build_error;oom env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
