# vllm-project/vllm#13778: [Bug]: vllm server hang when running DeepSeek R1

| 字段 | 值 |
| --- | --- |
| Issue | [#13778](https://github.com/vllm-project/vllm/issues/13778) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm server hang when running DeepSeek R1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I started vllm v0.7.3 server using the following command: ``` python3 -m vllm.entrypoints.openai.api_server --disable-log-requests --gpu-memory-utilization 0.8 --max-model-len 131072 --max-num-batched-tokens 4000 --seed 0 --tensor-parallel-size 16 --model /path-to/DeepSeek-R1 --trust-remote-code ``` And ran benchmark_serving as follow: ``` python3 /root/vllm-v0.7.3/benchmarks/benchmark_serving.py --backend vllm \ --model /path-to/DeepSeek-R1 \ --base-url http://127.0.0.1:8000 \ --endpoint /v1/completions \ --num-prompts 32 \ --request-rate 8 \ --metric_percentiles '50,90,95,99' \ --goodput ttft:5000 tpot:250 \ --max-concurrency 8 \ --random-input-len 2500 \ --random-output-len 1500 \ --dataset-name random \ --ignore-eos --trust-remote-code \ --save-result > log ``` After handling some requests normally, the service hangs. At this point, the vLLM process does not exit, GPU utilization drops to 0%, and CPU usage isn't high. Do you have any insights into the potential causes or solutions for this issue? FYI: the last benchmark ran successfully is request-rate 4 + max-concurrency 4 + input 3500 + output 1500 vLLM server hang but not...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;operator build_error env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ents/assets/9e99abbf-193b-4a91-b703-9a8400476578) the output of `nvidia-smi:` the output of `top`: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot liv...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: lel-size 16 --model /path-to/DeepSeek-R1 --trust-remote-code ``` And ran benchmark_serving as follow: ``` python3 /root/vllm-v0.7.3/benchmarks/benchmark_serving.py --backend vllm \ --model /path-to/DeepSeek-R1 \ --base-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm server hang when running DeepSeek R1 bug;stale ### Your current environment ### 🐛 Describe the bug I started vllm v0.7.3 server using the following command: ``` python3 -m vllm.entrypoints.openai.api_server...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: follow: ``` python3 /root/vllm-v0.7.3/benchmarks/benchmark_serving.py --backend vllm \ --model /path-to/DeepSeek-R1 \ --base-url http://127.0.0.1:8000 \ --endpoint /v1/completions \ --num-prompts 32 \ --request-rate 8 \

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
