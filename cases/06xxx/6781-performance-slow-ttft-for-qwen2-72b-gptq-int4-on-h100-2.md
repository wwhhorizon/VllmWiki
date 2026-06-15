# vllm-project/vllm#6781: [Performance]: Slow TTFT(?) for Qwen2-72B-GPTQ-Int4 on H100 *2

| 字段 | 值 |
| --- | --- |
| Issue | [#6781](https://github.com/vllm-project/vllm/issues/6781) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Slow TTFT(?) for Qwen2-72B-GPTQ-Int4 on H100 *2

### Issue 正文摘录

I did some tests in order to find better parameter to speed up, and it appears that there hasn't been a significant change in TTFT (Time To First Token). Is my TTFT correct? I feel it might be a bit too slow... Here's the test environment: `H100 *2, vllm = 0.5.3post1` #### Test script: `python benchmark_serving.py --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json --dataset-name sharegpt --backend vllm --model Qwen2-72B-Int4 --request-rate 12 --num_prompts=1000` #### 1st test set: `python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2-72B-Instruct-GPTQ-Int4 --disable-log-requests --dtype auto --quantization marlin --max-model-len 8000` ``` ============ Serving Benchmark Result ============ Successful requests: 1000 Benchmark duration (s): 172.44 Total input tokens: 217393 Total generated tokens: 193576 Request throughput (req/s): 5.80 Input token throughput (tok/s): 1260.72 Output token throughput (tok/s): 1122.60 ---------------Time to First Token---------------- Mean TTFT (ms): 18799.19 Median TTFT (ms): 12578.35 P99 TTFT (ms): 54378.33 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 202.99 Median TPOT (ms): 206.15 P99 TPOT (ms): 351.08 ------...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: TTFT(?) for Qwen2-72B-GPTQ-Int4 on H100 *2 performance;stale I did some tests in order to find better parameter to speed up, and it appears that there hasn't been a significant change in TTFT (Time To First Token). Is m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Performance]: Slow TTFT(?) for Qwen2-72B-GPTQ-Int4 on H100 *2 performance;stale I did some tests in order to find better parameter to speed up, and it appears that there hasn't been a significant change in TTFT (Time T...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Slow TTFT(?) for Qwen2-72B-GPTQ-Int4 on H100 *2 performance;stale I did some tests in order to find better parameter to speed up, and it appears that there hasn't been a significant change in TTFT (Time T...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: erformance]: Slow TTFT(?) for Qwen2-72B-GPTQ-Int4 on H100 *2 performance;stale I did some tests in order to find better parameter to speed up, and it appears that there hasn't been a significant change in TTFT (Time To...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: path ShareGPT_V3_unfiltered_cleaned_split.json --dataset-name sharegpt --backend vllm --model Qwen2-72B-Int4 --request-rate 12 --num_prompts=1000` #### 1st test set: `python3 -m vllm.entrypoints.openai.api_server --mode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
