# vllm-project/vllm#29085: [Bug]: RuntimeError "cancelled" when using pipeline parallelism with Qwen3-14B

| 字段 | 值 |
| --- | --- |
| Issue | [#29085](https://github.com/vllm-project/vllm/issues/29085) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError "cancelled" when using pipeline parallelism with Qwen3-14B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Reproduction Steps ### 1. Start vLLM serve with pipeline parallelism: ``` CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve /data/hfhub/Qwen3/Qwen3-14B/ --port 8011 --gpu-memory-utilization 0.9 --tensor-parallel-size 1 --pipeline-parallel-size 4 --max-num-batched-tokens 2048 --max-num-seqs 2048 ``` ### 2. Run benchmark test: ``` vllm bench serve --base-url http://localhost:8011 --model /data/hfhub/Qwen3/Qwen3-14B/ --dataset-name random --random-input-len 128 --random-output-len 100 --request-rate 40 --num-prompts 20000 --save-result --save-detailed --append-result --result-dir /data/slwang/vllm_bench_results/Qwen3-14B-A100-t1-p4/ --result-filename 40qps-batch2048-burstiness0.1.json --seed 100 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 90,95,99 --ignore-eos --burstiness 0.1 ``` ## Error Log ``` (EngineCore_DP0 pid=69817) Process EngineCore_DP0: (EngineCore_DP0 pid=69817) Traceback (most recent call last): (EngineCore_DP0 pid=69817) File "/home/slwang/.local/share/uv/python/cpython-3.12.11-linux-x86_64-gnu/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=69817) self.run() (EngineCor...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: timeError "cancelled" when using pipeline parallelism with Qwen3-14B bug;stale ### Your current environment ### 🐛 Describe the bug ## Reproduction Steps ### 1. Start vLLM serve with pipeline parallelism: ``` CUDA_VISIBL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ory broadcast communication layer during inter-process communication. Specifically, the read operation from the worker response message queue is being cancelled, which suggests a timeout or communication failure between...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: RuntimeError "cancelled" when using pipeline parallelism with Qwen3-14B bug;stale ### Your current environment ### 🐛 Describe the bug ## Reproduction Steps ### 1. Start vLLM serve with pipeline parallelism: ``` C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: RuntimeError "cancelled" when using pipeline parallelism with Qwen3-14B bug;stale ### Your current environment ### 🐛 Describe the bug ## Reproduction Steps ### 1. Start vLLM serve with pipeline parallelism: ``` C...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: -size 4 --max-num-batched-tokens 2048 --max-num-seqs 2048 ``` ### 2. Run benchmark test: ``` vllm bench serve --base-url http://localhost:8011 --model /data/hfhub/Qwen3/Qwen3-14B/ --dataset-name random --random-input-le...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
