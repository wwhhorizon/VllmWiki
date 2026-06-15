# vllm-project/vllm#20354: [Bug]: vLLM 0.9.1 takes a long time to start up when using --enable-lora and CUDA Graph

| 字段 | 值 |
| --- | --- |
| Issue | [#20354](https://github.com/vllm-project/vllm/issues/20354) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.9.1 takes a long time to start up when using --enable-lora and CUDA Graph

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When starting with the following command using vLLM 0.9.1, it gets stuck, but adding `--enforce-eager` allows it to run normally. ```shell vllm serve Qwen/Qwen2.5-14B \ --port 8080 \ --served-model-name model \ --gpu-memory-utilization 0.9 \ --max-num-seqs 64 \ --enable-prefix-caching \ --enable-lora ``` ``` 2025-07-02T14:32:50.786405823+08:00 [HAMI-core Msg(1:140105358836736:libvgpu.c:840)]: Initializing..... 2025-07-02T14:32:50.786709725+08:00 [HAMI-core Warn(1:140105358836736:multiprocess_memory_limit.c:591)]: Kick dead proc 150 2025-07-02T14:32:57.707472105+08:00 DEBUG 07-02 14:32:57 [__init__.py:31] No plugins for group vllm.platform_plugins found. 2025-07-02T14:32:57.707497525+08:00 DEBUG 07-02 14:32:57 [__init__.py:35] Checking if TPU platform is available. 2025-07-02T14:32:57.707616412+08:00 DEBUG 07-02 14:32:57 [__init__.py:45] TPU platform is not available because: No module named 'libtpu' ... Loading safetensors checkpoint shards: 0% Completed | 0/8 [00:00 2025-07-02T14:34:36.496076119+08:00 DEBUG 07-02 14:34:36 [utils.py:485] Waiting for 1 local, 0 remote core engine proc(s) to start. 2025-07-02T14:34:46.506054858+08:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error env_dependency;shape Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ]: vLLM 0.9.1 takes a long time to start up when using --enable-lora and CUDA Graph bug;stale ### Your current environment ### 🐛 Describe the bug When starting with the following command using vLLM 0.9.1, it gets stuck,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: adding `--enforce-eager` allows it to run normally. ```shell vllm serve Qwen/Qwen2.5-14B \ --port 8080 \ --served-model-name model \ --gpu-memory-utilization 0.9 \ --max-num-seqs 64 \ --enable-prefix-caching \ --enable-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: akes a long time to start up when using --enable-lora and CUDA Graph bug;stale ### Your current environment ### 🐛 Describe the bug When starting with the following command using vLLM 0.9.1, it gets stuck, but adding `--...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
