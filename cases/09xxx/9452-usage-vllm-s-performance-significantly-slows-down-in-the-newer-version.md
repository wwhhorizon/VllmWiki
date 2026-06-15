# vllm-project/vllm#9452: [Usage]: vLLM's performance significantly slows down in the newer version when using multi-LoRA inference

| 字段 | 值 |
| --- | --- |
| Issue | [#9452](https://github.com/vllm-project/vllm/issues/9452) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vLLM's performance significantly slows down in the newer version when using multi-LoRA inference

### Issue 正文摘录

### Test Conditions - **Dataset:** Alpaca (Chinese) - **Total Requests:** 500 - **Request Rate:** 16 req/s - **Model:** Qwen2.5-32B-Instruct - **Hardware:** A100_40G × 2 ### Results I modified the benchmark code to run the Alpaca dataset. The benchmark duration (in seconds) is as follows: | vLLM Version | 0.5.0|0.5.4 | 0.6.2 | | ------------- | ----- | ----- | ----- | | Only Base | 49.33| 48.47 | 37.93 | | Base with LoRA | 58.96 | 71.81 | 83.56 | The results indicate that vLLM's performance significantly slows down in the newer version (0.6.2) when using multi-LoRA inference. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: quest Rate:** 16 req/s - **Model:** Qwen2.5-32B-Instruct - **Hardware:** A100_40G × 2 ### Results I modified the benchmark code to run the Alpaca dataset. The benchmark duration (in seconds) is as follows: | vLLM Versio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: aca (Chinese) - **Total Requests:** 500 - **Request Rate:** 16 req/s - **Model:** Qwen2.5-32B-Instruct - **Hardware:** A100_40G × 2 ### Results I modified the benchmark code to run the Alpaca dataset. The benchmark dura...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: lows down in the newer version when using multi-LoRA inference usage ### Test Conditions - **Dataset:** Alpaca (Chinese) - **Total Requests:** 500 - **Request Rate:** 16 req/s - **Model:** Qwen2.5-32B-Instruct - **Hardw...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: vLLM's performance significantly slows down in the newer version when using multi-LoRA inference usage ### Test Conditions - **Dataset:** Alpaca (Chinese) - **Total Requests:** 500 - **Request Rate:** 16 req/s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ence usage ### Test Conditions - **Dataset:** Alpaca (Chinese) - **Total Requests:** 500 - **Request Rate:** 16 req/s - **Model:** Qwen2.5-32B-Instruct - **Hardware:** A100_40G × 2 ### Results I modified the benchmark c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
