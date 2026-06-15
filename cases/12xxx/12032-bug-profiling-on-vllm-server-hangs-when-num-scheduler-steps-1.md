# vllm-project/vllm#12032: [Bug]: Profiling on vLLM server hangs when --num-scheduler-steps > 1 

| 字段 | 值 |
| --- | --- |
| Issue | [#12032](https://github.com/vllm-project/vllm/issues/12032) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Profiling on vLLM server hangs when --num-scheduler-steps > 1 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug My vLLM version 0.6.5. The vLLM server works well with any number of `--num-scheduler-steps` when running the script benchmark_serving.py. However, the script seems to hang when I use the `--profile` argument. Testing with Different Values of `--num-scheduler-steps`: - --num-scheduler-steps=1: Works. It seems also work for other models. - --num-scheduler-steps=10: Causes the script to hang indefinitely. - --num-scheduler-steps=16: Works. I am unsure why certain values of --num-scheduler-steps work in Llama-3.1-8B-Instruct model , while others cause the process to hang. How to reproduce: ``` export VLLM_TORCH_PROFILER_DIR=/app vllm serve /Path/to/meta-llama/Llama-3.1-8B-Instruct \ --dtype float16 --swap-space 16 \ --disable-log-requests --tensor-parallel-size 2 --distributed-executor-backend mp \ --num-scheduler-steps 10 --gpu-memory-utilization 0.8 --max-model-len 8192 \ --max-num-batched-tokens 65536 --enable-chunked-prefill=False python3 /vllm/benchmarks/benchmark_serving.py --host localhost --backend openai --port 8000 \ --model /data/huggingface/hub/meta-llama/Llama-3.1-8B-Instruct --datase...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Profiling on vLLM server hangs when --num-scheduler-steps > 1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug My vLLM version 0.6.5. The vLLM server works well wi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Bug]: Profiling on vLLM server hangs when --num-scheduler-steps > 1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug My vLLM version 0.6.5. The vLLM server works well wi
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### Model Input Dumps _No response_ ### 🐛 Describe the bug My vLLM version 0.6.5. The vLLM server works well with any number of `--num-scheduler-steps` when running the script benchmark_serving.py. However, the script s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: -num-scheduler-steps > 1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug My vLLM version 0.6.5. The vLLM server works well with any number of `--num-scheduler-steps` whe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: --percentile-metrics ttft,tpot,itl,e2el --profile WARNING 01-14 09:29:47 rocm.py:34] `fork` method is not supported by ROCm. VLLM_WORKER_MULTIPROC_METHOD is overridden to `spawn` instead. Namespace(backend='openai', bas...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
