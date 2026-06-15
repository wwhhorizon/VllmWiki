# vllm-project/vllm#24005: [Doc]: why vllm bench tset Successful requests very low

| 字段 | 值 |
| --- | --- |
| Issue | [#24005](https://github.com/vllm-project/vllm/issues/24005) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: why vllm bench tset Successful requests very low

### Issue 正文摘录

### 📚 The doc issue I launched the qwen3-8B model on an L20 and tested it with vllm bench, but the results were disappointing. In particular, the number of successful requests was very low. star serve：`export CUDA_VISIBLE_DEVICES=0 vllm serve "/data0/data/Qwen3-8B/" --gpu-memory-utilization 0.7` test: ``` BASE_URL="http://localhost:8000" MODEL="/data0/data/Qwen3-8B/" vllm bench serve \ --backend openai \ --base-url "$BASE_URL" \ --endpoint "/v1/completions" \ --model "$MODEL" \ --dataset-name random \ --tokenizer "$MODEL" \ --random-input-len 128 \ --random-output-len 128 \ --num-prompts 500 \ --max-concurrency 2 \ GPU usage: 32980MiB / 46068MiB ``` result is follow as ``` Initial test run completed. Starting main benchmark run... Traffic request rate: inf Burstiness factor: 1.0 (Poisson process) Maximum request concurrency: 2 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:02<00:00, 34.85it/s] ============ Serving Benchmark Result ============ Successful requests: 1 Maximum request concurrency: 2 Benchmark duration (s): 2.87 Tot...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: n;stale ### 📚 The doc issue I launched the qwen3-8B model on an L20 and tested it with vllm bench, but the results were disappointing. In particular, the number of successful requests was very low. star serve：`export CU...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: equests very low documentation;stale ### 📚 The doc issue I launched the qwen3-8B model on an L20 and tested it with vllm bench, but the results were disappointing. In particular, the number of successful requests was ve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Doc]: why vllm bench tset Successful requests very low documentation;stale ### 📚 The doc issue I launched the qwen3-8B model on an L20 and tested it with vllm bench, but the results were disappointing. In particular, t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ocalhost:8000" MODEL="/data0/data/Qwen3-8B/" vllm bench serve \ --backend openai \ --base-url "$BASE_URL" \ --endpoint "/v1/completions" \ --model "$MODEL" \ --dataset-name random \ --tokenizer "$MODEL" \ --random-input...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ===================================== ``` only one request success! vllm version == v0.10.1.1 ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] #24166

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
