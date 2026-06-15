# vllm-project/vllm#24760: [Bug]: CUDA illegal memory access when benchmarking gemma-3-4b-it

| 字段 | 值 |
| --- | --- |
| Issue | [#24760](https://github.com/vllm-project/vllm/issues/24760) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA illegal memory access when benchmarking gemma-3-4b-it

### Issue 正文摘录

### Your current environment #### Environment - Docker image: [vllm/vllm-openai (latest)](https://hub.docker.com/r/vllm/vllm-openai/tags) -Single GPU: **NVIDIA B200** #### Reproduction Steps 1. Pull latest image: ```bash docker pull vllm/vllm-openai:latest ``` 2. Run server: ```bash vllm serve google/gemma-3-4b-it --tensor-parallel-size 1 --port 8000 ``` 3. Run client benchmark: ```bash vllm bench serve \ --backend vllm \ --model google/gemma-3-4b-it \ --random-input-len 1024 \ --random-output-len 2048 \ --port 8000 \ --percentile-metrics "ttft,tpot,itl,e2el" \ --request-rate 10 ``` ### 🐛 Describe the bug #### Observed Error During benchmarking, the following error occurs: ``` (EngineCore_0 pid=168) ERROR 09-12 09:18:59 [core.py:702] RuntimeError: CUDA error: an illegal memory access was encountered (EngineCore_0 pid=168) ERROR 09-12 09:18:59 [core.py:702] CUDA kernel errors might be asynchronously reported at some other API call (EngineCore_0 pid=168) ERROR 09-12 09:18:59 [core.py:702] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 (EngineCore_0 pid=168) ERROR 09-12 09:18:59 [core.py:702] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` #### Attachme...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: mma-3-4b-it bug;stale ### Your current environment #### Environment - Docker image: [vllm/vllm-openai (latest)](https://hub.docker.com/r/vllm/vllm-openai/tags) -Single GPU: **NVIDIA B200** #### Reproduction Steps 1. Pul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA illegal memory access when benchmarking gemma-3-4b-it bug;stale ### Your current environment #### Environment - Docker image: [vllm/vllm-openai (latest)](https://hub.docker.com/r/vllm/vllm-openai/tags) -Sing...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: CUDA illegal memory access when benchmarking gemma-3-4b-it bug;stale ### Your current environment #### Environment - Docker image: [vllm/vllm-openai (latest)](https://hub.docker.com/r/vllm/vllm-openai/tags) -Sing...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: CUDA illegal memory access when benchmarking gemma-3-4b-it bug;stale ### Your current environment #### Environment - Docker image: [vllm/vllm-openai (latest)](https://hub.docker.com/r/vllm/vllm-openai/tags) -Sing...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: CUDA illegal memory access when benchmarking gemma-3-4b-it bug;stale ### Your current environment #### Environment - Docker image: [vllm/vllm-openai (latest)](https://hub.docker.com/r/vllm/vllm-openai/tags) -Sing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
