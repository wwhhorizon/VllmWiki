# vllm-project/vllm#12144: [Bug]: Benchmark script - TypeError: argument 'text': 'list' object cannot be converted to 'PyString'

| 字段 | 值 |
| --- | --- |
| Issue | [#12144](https://github.com/vllm-project/vllm/issues/12144) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Benchmark script - TypeError: argument 'text': 'list' object cannot be converted to 'PyString'

### Issue 正文摘录

### Your current environment ### Model Input Dumps vllm version `0.6.6` Running below command - ``` python3 benchmarks/benchmark_serving.py --backend openai-chat --model msnemo24072h100gv --base-url --dataset-name sonnet --dataset-path benchmarks/sonnet.txt --request-rate 16 --num-prompts 256 --endpoint /api/v1/chat/completions --sonnet-input-len=3864 --sonnet-output-len=200 --sonnet-prefix-len=3764 --tokenizer mistralai/Mistral-Nemo-Instruct-2407 --tokenizer-mode mistral ``` Getting below error ``` Traceback (most recent call last): File "/home/vijay/vllm/benchmarks/benchmark_serving.py", line 1226, in main(args) File "/home/vijay/vllm/benchmarks/benchmark_serving.py", line 821, in main input_requests = sample_sonnet_requests( ^^^^^^^^^^^^^^^^^^^^^^^ File "/home/vijay/vllm/benchmarks/benchmark_serving.py", line 149, in sample_sonnet_requests poem_token_ids = tokenizer(poem_lines).input_ids ^^^^^^^^^^^^^^^^^^^^^ File "/home/vijay/miniconda3/envs/nai/lib/python3.11/site-packages/vllm/transformers_utils/tokenizers/mistral.py", line 232, in __call__ input_ids = self.encode(prompt) ^^^^^^^^^^^^^^^^^^^ File "/home/vijay/miniconda3/envs/nai/lib/python3.11/site-packages/vllm/transformers...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: String' bug ### Your current environment ### Model Input Dumps vllm version `0.6.6` Running below command - ``` python3 benchmarks/benchmark_serving.py --backend openai-chat --model msnemo24072h100gv --base-url --datase...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: benchmarks/benchmark_serving.py --backend openai-chat --model msnemo24072h100gv --base-url --dataset-name sonnet --dataset-path benchmarks/sonnet.txt --request-rate 16 --num-prompts 256 --endpoint /api/v1/chat/completio...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ` Running below command - ``` python3 benchmarks/benchmark_serving.py --backend openai-chat --model msnemo24072h100gv --base-url --dataset-name sonnet --dataset-path benchmarks/sonnet.txt --request-rate 16 --num-prompts...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: -base-url --dataset-name sonnet --dataset-path benchmarks/sonnet.txt --request-rate 16 --num-prompts 256 --endpoint /api/v1/chat/completions --sonnet-input-len=3864 --sonnet-output-len=200 --sonnet-prefix-len=3764 --tok...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Benchmark script - TypeError: argument 'text': 'list' object cannot be converted to 'PyString' bug ### Your current environment ### Model Input Dumps vllm version `0.6.6` Running below command - ``` python3 bench...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
