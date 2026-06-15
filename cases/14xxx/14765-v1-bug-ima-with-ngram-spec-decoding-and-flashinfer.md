# vllm-project/vllm#14765: [V1][Bug] IMA with ngram spec decoding and flashinfer

| 字段 | 值 |
| --- | --- |
| Issue | [#14765](https://github.com/vllm-project/vllm/issues/14765) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [V1][Bug] IMA with ngram spec decoding and flashinfer

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With current main branch, I'm seeing the following: ``` $ VLLM_LOGGING_LEVEL=DEBUG VLLM_USE_V1=1 VLLM_ENABLE_V1_MULTIPROCESSING=1 vllm serve meta-llama/Llama-3.1-8B-Instruct --speculative-model "[ngram]" --num-speculative-tokens 5 --ngram-prompt-lookup-max 4 .... ERROR 03-13 11:26:04 [core.py:337] EngineCore hit an exception: Traceback (most recent call last): ERROR 03-13 11:26:04 [core.py:337] File "/home/markmc/vllm-project/vllm/vllm/v1/engine/core.py", line 330, in run_engine_core ERROR 03-13 11:26:04 [core.py:337] engine_core.run_busy_loop() ERROR 03-13 11:26:04 [core.py:337] File "/home/markmc/vllm-project/vllm/vllm/v1/engine/core.py", line 364, in run_busy_loop ERROR 03-13 11:26:04 [core.py:337] outputs = step_fn() ERROR 03-13 11:26:04 [core.py:337] ^^^^^^^^^ ERROR 03-13 11:26:04 [core.py:337] File "/home/markmc/vllm-project/vllm/vllm/v1/engine/core.py", line 192, in step ERROR 03-13 11:26:04 [core.py:337] output = self.model_executor.execute_model(scheduler_output) ERROR 03-13 11:26:04 [core.py:337] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-13 11:26:04 [core.py:337] File "/home/markmc/vllm-project/vllm/v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: NABLE_V1_MULTIPROCESSING=1 vllm serve meta-llama/Llama-3.1-8B-Instruct --speculative-model "[ngram]" --num-speculative-tokens 5 --ngram-prompt-lookup-max 4 .... ERROR 03-13 11:26:04 [core.py:337] EngineCore hit an excep...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [V1][Bug] IMA with ngram spec decoding and flashinfer bug ### Your current environment ### 🐛 Describe the bug With current main branch, I'm seeing the following: ``` $ VLLM_LOGGING_LEVEL=DEBUG VLLM_USE_V1=1 VLLM_ENABLE_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-13 11:26:04 [core.py:337] RuntimeError: CUDA error: an illegal memory access was encountered ``` Workload is: ``` $ python ./benchmarks/benchmark_serving.py --model meta-llama/Llama-3.1-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: VEL=DEBUG VLLM_USE_V1=1 VLLM_ENABLE_V1_MULTIPROCESSING=1 vllm serve meta-llama/Llama-3.1-8B-Instruct --speculative-model "[ngram]" --num-speculative-tokens 5 --ngram-prompt-lookup-max 4 .... ERROR 03-13 11:26:04 [core.p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
