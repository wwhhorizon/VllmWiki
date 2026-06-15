# vllm-project/vllm#24535: [Bug]: 500 internal server error when BS>8 for ISL/OSL: 1K/1K, 1K/8K.

| 字段 | 值 |
| --- | --- |
| Issue | [#24535](https://github.com/vllm-project/vllm/issues/24535) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 500 internal server error when BS>8 for ISL/OSL: 1K/1K, 1K/8K.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Model: nvidia/DeepSeek-R1-0528-FP4 ISL: 1K, OSL: 1K. TP=4. Server command: export VLLM_FLASHINFER_MOE_BACKEND=latency VLLM_USE_STANDALONE_COMPILE=0 VLLM_WORKER_MULTIPROC_METHOD=fork vllm serve $MODEL \ --tokenizer $MODEL \ --seed 1 --trust-remote-code \ --quantization=modelopt_fp4 \ --enable-chunked-prefill \ --disable-log-requests --no-enable-prefix-caching \ --host 0.0.0.0 --port=8080 \ --gpu-memory-utilization 0.85 \ --tensor-parallel-size $TP \ --cuda-graph-sizes 1 2 4 8 16 32 64 128 256 512 1024 Client command: INPUT_LEN=1024 OUTPUT_LEN=1024 BATCH=8 NUM_PROMPTS=$((2 * BATCH)) FRAMEWORK=vllm python3 vllm/benchmarks/benchmark_serving.py \ --model $MODEL --tokenizer $MODEL \ --trust-remote-code \ --dataset-name random --random-input-len $INPUT_LEN \ --random-output-len $OUTPUT_LEN --random-range-ratio 0.8 \ --num-prompts $NUM_PROMPTS --seed 1 \ --ignore-eos --metadata "framework=$FRAMEWORK" \ --port 8080 --host 0.0.0.0 \ --max-concurrency $BATCH ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https:...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Bug]: 500 internal server error when BS>8 for ISL/OSL: 1K/1K, 1K/8K. bug;stale ### Your current environment ### 🐛 Describe the bug Model: nvidia/DeepSeek-R1-0528-FP4 ISL: 1K, OSL: 1K. TP=4. Server command: export VLLM_F...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 1K, OSL: 1K. TP=4. Server command: export VLLM_FLASHINFER_MOE_BACKEND=latency VLLM_USE_STANDALONE_COMPILE=0 VLLM_WORKER_MULTIPROC_METHOD=fork vllm serve $MODEL \ --tokenizer $MODEL \ --seed 1 --trust-remote-code \ --qua...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pSeek-R1-0528-FP4 ISL: 1K, OSL: 1K. TP=4. Server command: export VLLM_FLASHINFER_MOE_BACKEND=latency VLLM_USE_STANDALONE_COMPILE=0 VLLM_WORKER_MULTIPROC_METHOD=fork vllm serve $MODEL \ --tokenizer $MODEL \ --seed 1 --tr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: t environment ### 🐛 Describe the bug Model: nvidia/DeepSeek-R1-0528-FP4 ISL: 1K, OSL: 1K. TP=4. Server command: export VLLM_FLASHINFER_MOE_BACKEND=latency VLLM_USE_STANDALONE_COMPILE=0 VLLM_WORKER_MULTIPROC_METHOD=fork...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --gpu-memory-utilization 0.85 \ --tensor-parallel-size $TP \ --cuda-graph-sizes 1 2 4 8 16 32 64 128 256 512 1024 Client command: INPUT_LEN=1024 OUTPUT_LEN=1024 BATCH=8 NUM_PROMPTS=$((2 * BATCH)) FRAMEWORK=vllm python3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
