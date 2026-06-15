# vllm-project/vllm#18455: [Bug]: Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.

| 字段 | 值 |
| --- | --- |
| Issue | [#18455](https://github.com/vllm-project/vllm/issues/18455) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CMD: ``` # root of vllm cd benchmarks python benchmark_latency.py --model meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 8 --batch-size 4 --input-len 4096 --output-len 1 --dtype bfloat16 --gpu-memory-utilization 0.9 --num-iters 30 --num-iters-warmup 5 --output-json out/latency_results_meta-llama_Llama-3.1-8B-Instruct_tp_size8_batch_size4_input_len4096_output_len1.json ``` Error message: ``` ERROR 05-21 05:16:15 [core.py:489] EngineCore failed to start. ERROR 05-21 05:16:15 [core.py:489] Traceback (most recent call last): ERROR 05-21 05:16:15 [core.py:489] File "/home/ec2-user/workspace/vllm-benchmark/third_party/vllm/vllm/v1/engine/core.py", line 480, in run_engine_core ERROR 05-21 05:16:15 [core.py:489] engine_core = EngineCoreProc(*args, **kwargs) ERROR 05-21 05:16:15 [core.py:489] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 05-21 05:16:15 [core.py:489] File "/home/ec2-user/workspace/vllm-benchmark/third_party/vllm/vllm/v1/engine/core.py", line 379, in __init__ ERROR 05-21 05:16:15 [core.py:489] super().__init__(vllm_config, executor_class, log_stats, ERROR 05-21 05:16:15 [core.py:489] File "/home/ec2-user/workspace/vllm-ben...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -tensor-parallel-size 8 --batch-size 4 --input-len 4096 --output-len 1 --dtype bfloat16 --gpu-memory-utilization 0.9 --num-iters 30 --num-iters-warmup 5 --output-json out/latency_results_meta-llama_Llama-3.1-8B-Instruct...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: bug CMD: ``` # root of vllm cd benchmarks python benchmark_latency.py --model meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 8 --batch-size 4 --input-len 4096 --output-len 1 --dtype bfloat16 --gpu-memory-utiliz...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: rrent environment ### 🐛 Describe the bug CMD: ``` # root of vllm cd benchmarks python benchmark_latency.py --model meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 8 --batch-size 4 --input-len 4096 --output-len 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
