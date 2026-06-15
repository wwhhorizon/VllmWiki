# vllm-project/vllm#19210: [Bug]: Strange metrics when running `benchmark_serving` under high concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#19210](https://github.com/vllm-project/vllm/issues/19210) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Strange metrics when running `benchmark_serving` under high concurrency

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running `benchmark_serving.py`, I got some strange metrics: - I got an expected ttft and an abnormally large tpot for the first inference after the vllm serve started. The script I used for server side is: ``` VLLM_TORCH_PROFILER_DIR=./outputs/vllm_profile VLLM_RPC_TIMEOUT=1800000 \ vllm serve ../../data/huggingface.co/Qwen/Qwen3-32B \ --max-model-len=16384 \ --max-num-batch-tokens=2048 \ --max-num-seqs=128 \ -tp 2 \ --disable-log-requests ``` The script I used for client side is: ``` python3 benchmarks/benchmark_serving.py --port 8000 \ --save-result --save-detailed \ --result-dir outputs/benchmark \ --backend vllm \ --model ../data/huggingface.co/Qwen/Qwen3-32B \ --dataset-name custom \ --dataset-path "dataset/custom_all.jsonl" \ --custom-output-len 10 \ --num-prompts 16 \ --max-concurrency 2 \ --temperature 0.6 \ --top-p 0.95 \ --top-k 1 \ --profile ``` And the output I got: ``` =========== Serving Benchmark Result =========== Successful requests: 16 Benchmark duration (s): 19.65 Total input tokens: 109554 Total generated tokens: 160 Request throughput (req/s): 0.81 Output token throughput (tok/s): 8.14 Total Token throug...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Bug]: Strange metrics when running `benchmark_serving` under high concurrency bug;stale ### Your current environment ### 🐛 Describe the bug When running `benchmark_serving.py`, I got some strange metrics: - I got an ex...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory cuda;operator;sampling;triton build_err...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ============================================ ``` - I got an abnormally small ttft and an expected tpot for the following inferences, and I noticed the prefix cache hit rate is always bigger than 50%, while in the first...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: puts/vllm_profile VLLM_RPC_TIMEOUT=1800000 \ vllm serve ../../data/huggingface.co/Qwen/Qwen3-32B \ --max-model-len=16384 \ --max-num-batch-tokens=2048 \ --max-num-seqs=128 \ -tp 2 \ --disable-log-requests ``` The script...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ange metrics when running `benchmark_serving` under high concurrency bug;stale ### Your current environment ### 🐛 Describe the bug When running `benchmark_serving.py`, I got some strange metrics: - I got an expected ttf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
