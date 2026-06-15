# vllm-project/vllm#37666: [Bug]: vllm bench:   "Peak output token throughput"  is "less than Output token throughput"

| 字段 | 值 |
| --- | --- |
| Issue | [#37666](https://github.com/vllm-project/vllm/issues/37666) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm bench:   "Peak output token throughput"  is "less than Output token throughput"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm bench serve \ --dataset-name random \ --num-prompts "${NUM_PROMPTS}" \ --max-concurrency 10 \ --random-input 1024 \ --random-output 1024 \ --host "${HOST}" \ --port "${PORT}" \ --backend "openai-chat" \ --percentile-metrics ttft,tpot,itl,e2el \ --model "${MODEL_NAME}" \ --tokenizer "${TOKENIZER_PATH}" \ --ignore-eos ============ Serving Benchmark Result ============ Successful requests: 20 Failed requests: 0 Maximum request concurrency: 10 Benchmark duration (s): 56.71 Total input tokens: 20460 Total generated tokens: 20480 Request throughput (req/s): 0.35 Output token throughput (tok/s): 361.11 Peak output token throughput (tok/s): 180.00 Peak concurrent requests: 13.00 Total token throughput (tok/s): 721.88 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: vllm bench: "Peak output token throughput" is "less than Output token throughput" bug ### Your current environment ### 🐛 Describe the bug vllm bench serve \ --dataset-name random \ --num-prompts "${NUM_PROMPTS}"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;frontend_api;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf;slowdown dtype;env_dependen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: t 1024 \ --host "${HOST}" \ --port "${PORT}" \ --backend "openai-chat" \ --percentile-metrics ttft,tpot,itl,e2el \ --model "${MODEL_NAME}" \ --tokenizer "${TOKENIZER_PATH}" \ --ignore-eos ============ Serving Benchmark...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: mpling_logits cuda;operator;sampling;triton build_error;nan_inf;slowdown dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
