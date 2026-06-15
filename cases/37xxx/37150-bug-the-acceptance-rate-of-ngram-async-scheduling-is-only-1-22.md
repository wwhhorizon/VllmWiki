# vllm-project/vllm#37150: [Bug]: the acceptance rate of ngram+async-scheduling is only 1.22%

| 字段 | 值 |
| --- | --- |
| Issue | [#37150](https://github.com/vllm-project/vllm/issues/37150) |
| 状态 | open |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: the acceptance rate of ngram+async-scheduling is only 1.22%

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Compared to ngram(accptance rate is 70%), the performance of ngram + async-scheduling has significantly decreased, and the acceptance rate is only 1.2%. The output throughput of ngram is 1971 tok/s, while the output throughput of ngram+asynchronous scheduling is 1759 tok/s. @benchislett @PatchouliTIS May I ask if it's convenient to take a look? refer to this pr: https://github.com/vllm-project/vllm/pull/29184 scripts is here: vllm version: v0.17.0rc1 ngram+async script: llm serve /model/Qwen3-1.7B --port 8898 --dtype bfloat16 \ --tensor-parallel-size 1 --gpu-memory-utilization 0.8 \ --max-model-len 32768 --trust-remote-code \ --no-enable-prefix-caching \ --async-scheduling \ --speculative_config '{"method": "ngram_gpu", "num_speculative_tokens": 3, "prompt_lookup_max": 2,"prompt_lookup_min": 2}' ngram scipte: vllm serve /model/Qwen3-1.7B --port 8898 --dtype bfloat16 \ --tensor-parallel-size 1 --gpu-memory-utilization 0.8 \ --max-model-len 32768 --trust-remote-code \ --no-enable-prefix-caching \ --speculative_config '{"method": "ngram", "num_speculative_tokens": 3, "prompt_lookup_max": 2,"prompt_lookup_min": 2}' test script: expor...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ignificantly decreased, and the acceptance rate is only 1.2%. The output throughput of ngram is 1971 tok/s, while the output throughput of ngram+asynchronous scheduling is 1759 tok/s. @benchislett @PatchouliTIS May I as...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 0.17.0rc1 ngram+async script: llm serve /model/Qwen3-1.7B --port 8898 --dtype bfloat16 \ --tensor-parallel-size 1 --gpu-memory-utilization 0.8 \ --max-model-len 32768 --trust-remote-code \ --no-enable-prefix-caching \ -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ripts is here: vllm version: v0.17.0rc1 ngram+async script: llm serve /model/Qwen3-1.7B --port 8898 --dtype bfloat16 \ --tensor-parallel-size 1 --gpu-memory-utilization 0.8 \ --max-model-len 32768 --trust-remote-code \...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: https://github.com/vllm-project/vllm/pull/29184 scripts is here: vllm version: v0.17.0rc1 ngram+async script: llm serve /model/Qwen3-1.7B --port 8898 --dtype bfloat16 \ --tensor-parallel-size 1 --gpu-memory-utilization...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: st script: export CONCURRENCY=10 vllm bench serve \ --port 8898 \ --backend vllm \ --model /model/Qwen3-1.7B \ --endpoint /v1/completions \ --dataset-name sonnet \ --dataset-path ../benchmarks/sonnet.txt \ --max-concurr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
