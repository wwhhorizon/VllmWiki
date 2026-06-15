# vllm-project/vllm#25536: [Bug]: Inconsistent P90 TTFT Results with Identical Benchmark Parameters

| 字段 | 值 |
| --- | --- |
| Issue | [#25536](https://github.com/vllm-project/vllm/issues/25536) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Inconsistent P90 TTFT Results with Identical Benchmark Parameters

### Issue 正文摘录

### Your current environment ### Environment - **vLLM Version**: [v0.8.0] - **Model**: DeepSeek-R1 - **Backend**: OpenAI Chat API - **Hardware**: [H20] - **OS**: Linux ### 🐛 Describe the bug ### Description I'm experiencing significant variance in P90 TTFT (Time to First Token) latency when running the same benchmark multiple times with identical parameters. The difference can be as large as 25% between runs, which makes performance evaluation unreliable. ### Reproduction Steps **Command used:** ```bash python3 benchmarks/benchmark_serving.py \ --backend openai-chat \ --model DeepSeek-R1 \ --tokenizer deepseek-r1 \ --dataset-name sonnet \ --num-prompts 8 \ --trust-remote-code \ --max-concurrency 4 \ --warmup-num-prompts 4 \ --base-url http://10.12.118.153:8002 \ --endpoint /v1/chat/completions \ --dataset-path sonnet.txt \ --sonnet-input-len 1024 \ --sonnet-output-len 1024 \ --sonnet-prefix-len 200 \ --percentile-metrics ttft,tpot \ --metric-percentiles 50,90,99,100 ``` **Steps:** 1. Run the benchmark command above 2. Wait for completion and record P90 TTFT result 3. Immediately run the exact same command again 4. Compare P90 TTFT results ### Observed Results | Run | P90 TTFT (ms)...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: Inconsistent P90 TTFT Results with Identical Benchmark Parameters bug;stale ### Your current environment ### Environment - **vLLM Version**: [v0.8.0] - **Model**: DeepSeek-R1 - **Backend**: OpenAI Chat API - **Ha...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ameters bug;stale ### Your current environment ### Environment - **vLLM Version**: [v0.8.0] - **Model**: DeepSeek-R1 - **Backend**: OpenAI Chat API - **Hardware**: [H20] - **OS**: Linux ### 🐛 Describe the bug ### Descri...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: (-20.4%) | ### Expected Behavior With identical parameters, warmup, and small dataset size (8 prompts), the P90 TTFT should be consistent between runs, with variance ideally under 5%. ### Additional Context - The server...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ur current environment ### Environment - **vLLM Version**: [v0.8.0] - **Model**: DeepSeek-R1 - **Backend**: OpenAI Chat API - **Hardware**: [H20] - **OS**: Linux ### 🐛 Describe the bug ### Description I'm experiencing s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ## Environment - **vLLM Version**: [v0.8.0] - **Model**: DeepSeek-R1 - **Backend**: OpenAI Chat API - **Hardware**: [H20] - **OS**: Linux ### 🐛 Describe the bug ### Description I'm experiencing significant variance in P...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
