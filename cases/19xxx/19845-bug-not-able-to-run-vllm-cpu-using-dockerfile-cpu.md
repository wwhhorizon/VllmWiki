# vllm-project/vllm#19845: [Bug]: Not able to run vllm cpu using Dockerfile.cpu

| 字段 | 值 |
| --- | --- |
| Issue | [#19845](https://github.com/vllm-project/vllm/issues/19845) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Not able to run vllm cpu using Dockerfile.cpu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I installed VLLM from git git clone https://github.com/vllm-project/vllm.git vllm_source cd vllm_source then i build the cpu Docker using docker build -f docker/Dockerfile.cpu --tag vllm-cpu-env --target vllm-openai . When i try to run using given command it is giving error Command sudo docker run --rm --privileged=true --shm-size=4g -p 8888:8000 -e VLLM_CPU_KVCACHE_SPACE=4096 -e VLLM_CPU_OMP_THREADS_BIND=6 vllm-cpu-env --model=Qwen/Qwen3-0.6B --dtype=auto --no-enable-chunked-prefill --trust-remote-code Error INFO 06-19 07:42:56 [importing.py:43] Triton is installed but 0 active driver(s) found (expected 1). Disabling Triton to prevent runtime errors. INFO 06-19 07:42:56 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available. WARNING 06-19 07:42:56 [importing.py:75] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation. [W619 07:43:03.239704585 OperatorEntry.cpp:154] Warning: Warning only once for all operators, other operators may also be overridden. Overriding a previously registered kernel for the same operator an...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Not able to run vllm cpu using Dockerfile.cpu bug;stale ### Your current environment ### 🐛 Describe the bug I installed VLLM from git git clone https://github.com/vllm-project/vllm.git vllm_source cd vllm_source...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Not able to run vllm cpu using Dockerfile.cpu bug;stale ### Your current environment ### 🐛 Describe the bug I installed VLLM from git git clone https://github.com/vllm-project/vllm.git vllm_source cd vllm_source...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ill --trust-remote-code Error INFO 06-19 07:42:56 [importing.py:43] Triton is installed but 0 active driver(s) found (expected 1). Disabling Triton to prevent runtime errors. INFO 06-19 07:42:56 [importing.py:63] Triton...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: VLLM_CPU_OMP_THREADS_BIND=6 vllm-cpu-env --model=Qwen/Qwen3-0.6B --dtype=auto --no-enable-chunked-prefill --trust-remote-code Error INFO 06-19 07:42:56 [importing.py:43] Triton is installed but 0 active driver(s) found...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: U_KVCACHE_SPACE=4096 -e VLLM_CPU_OMP_THREADS_BIND=6 vllm-cpu-env --model=Qwen/Qwen3-0.6B --dtype=auto --no-enable-chunked-prefill --trust-remote-code Error INFO 06-19 07:42:56 [importing.py:43] Triton is installed but 0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
