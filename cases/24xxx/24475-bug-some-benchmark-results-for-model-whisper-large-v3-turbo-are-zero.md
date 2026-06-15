# vllm-project/vllm#24475: [Bug]: Some benchmark results for model whisper-large-v3-turbo are zero

| 字段 | 值 |
| --- | --- |
| Issue | [#24475](https://github.com/vllm-project/vllm/issues/24475) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Some benchmark results for model whisper-large-v3-turbo are zero

### Issue 正文摘录

### Your current environment Script ```bash DATASET_NAME=hf DATASET_PATH=edinburghcstr/ami HF_SUBSET=ihm HF_SPLIT=test LOCAL_MODEL=openai/whisper-large-v3-turbo SERVE_MODEL=whisper-large-v3-turbo HOST=localhost PORT=8001 BACKEND=openai-audio ENDPOINT=/v1/audio/transcriptions for request_rate in 4 8 16 32 40 48 64 80 96 128 256 512; do python3 vllm/benchmarks/benchmark_serving.py \ --backend $BACKEND \ --endpoint $ENDPOINT \ --dataset-name $DATASET_NAME \ --dataset-path $DATASET_PATH \ --hf-subset $HF_SUBSET \ --hf-split $HF_SPLIT\ --model $LOCAL_MODEL \ --served-model-name $SERVE_MODEL \ --request-rate $request_rate \ --host $HOST \ --port $PORT \ --num-prompts 1000 \ --trust-remote-code \ --save-result \ --result-filename $(basename $SERVE_MODEL)-request_rate${request_rate}.json \ --seed 12345 | tee -a $(basename $SERVE_MODEL)_log.txt done ``` Result ### 🐛 Describe the bug I benchmarked the performance of the whisper-large-v3-turbo model, I used vLLM version 0.8.3 with the benchmark script below and observed that some metrics have a value of 0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Some benchmark results for model whisper-large-v3-turbo are zero bug;stale ### Your current environment Script ```bash DATASET_NAME=hf DATASET_PATH=edinburghcstr/ami HF_SUBSET=ihm HF_SPLIT=test LOCAL_MODEL=openai...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g]: Some benchmark results for model whisper-large-v3-turbo are zero bug;stale ### Your current environment Script ```bash DATASET_NAME=hf DATASET_PATH=edinburghcstr/ami HF_SUBSET=ihm HF_SPLIT=test LOCAL_MODEL=openai/wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Some benchmark results for model whisper-large-v3-turbo are zero bug;stale ### Your current environment Script ```bash DATASET_NAME=hf DATASET_PATH=edinburghcstr/ami HF_SUBSET=ihm HF_SPLIT=test LOCAL_MODEL=openai...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rge-v3-turbo SERVE_MODEL=whisper-large-v3-turbo HOST=localhost PORT=8001 BACKEND=openai-audio ENDPOINT=/v1/audio/transcriptions for request_rate in 4 8 16 32 40 48 64 80 96 128 256 512; do python3 vllm/benchmarks/benchm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: hmarked the performance of the whisper-large-v3-turbo model, I used vLLM version 0.8.3 with the benchmark script below and observed that some metrics have a value of 0. ### Before submitting a new issue... - [x] Make su...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
