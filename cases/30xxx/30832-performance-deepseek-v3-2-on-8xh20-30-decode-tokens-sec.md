# vllm-project/vllm#30832: [Performance]: DeepSeek-V3.2 on 8xH20 30 decode tokens/sec

| 字段 | 值 |
| --- | --- |
| Issue | [#30832](https://github.com/vllm-project/vllm/issues/30832) |
| 状态 | open |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: DeepSeek-V3.2 on 8xH20 30 decode tokens/sec

### Issue 正文摘录

### Proposal to improve performance **My Env:** vllm 0.13.0rc2.dev178+g676db55ee deep_gemm 2.1.1+c9f8b34 cuda. 12.9 python. 3.10.18 **command** is the same as: vllm serve mypath/DeepSeek-V3.2 \ --tensor-parallel-size 8 \ --tokenizer-mode deepseek_v32 \ --tool-call-parser deepseek_v32 \ --enable-auto-tool-choice \ --reasoning-parser deepseek_v3 **My Question:** The output tokens is 30 tokens/s 1/req which is slower than excpted on https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html#benchmarking: is there any wrong with this? ------------------------------------------------ Benchmarking[¶](https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html#benchmarking) We used the following script to benchmark deepseek-ai/DeepSeek-V3.2 on 8xH20. vllm bench serve \ --model deepseek-ai/DeepSeek-V3.2 \ --dataset-name random \ --random-input 2048 \ --random-output 1024 \ --request-rate 10 \ --num-prompt 100 \ --trust-remote-code TP8 Benchmark Output[¶](https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html#tp8-benchmark-output) ============ Serving Benchmark Result ============ Successful requests: 100 Failed requests: 0 Request rate...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: ich is slower than excpted on https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html#benchmarking: is there any wrong with this? ------------------------------------------------ Benchmarking[¶](http...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: /s 1/req which is slower than excpted on https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html#benchmarking: is there any wrong with this? ------------------------------------------------ Benchmark...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 3.0rc2.dev178+g676db55ee deep_gemm 2.1.1+c9f8b34 cuda. 12.9 python. 3.10.18 **command** is the same as: vllm serve mypath/DeepSeek-V3.2 \ --tensor-parallel-size 8 \ --tokenizer-mode deepseek_v32 \ --tool-call-parser dee...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: to benchmark deepseek-ai/DeepSeek-V3.2 on 8xH20. vllm bench serve \ --model deepseek-ai/DeepSeek-V3.2 \ --dataset-name random \ --random-input 2048 \ --random-output 1024 \ --request-rate 10 \ --num-prompt 100 \ --trust...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: DeepSeek-V3.2 on 8xH20 30 decode tokens/sec performance ### Proposal to improve performance **My Env:** vllm 0.13.0rc2.dev178+g676db55ee deep_gemm 2.1.1+c9f8b34 cuda. 12.9 python. 3.10.18 *

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
