# vllm-project/vllm#24058: [Feature]: Improve `vllm bench serve` startup time with random data

| 字段 | 值 |
| --- | --- |
| Issue | [#24058](https://github.com/vllm-project/vllm/issues/24058) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Improve `vllm bench serve` startup time with random data

### Issue 正文摘录

### 🚀 The feature, motivation and pitch There are some issues with the benchmark script for long requests - A) we send a single test request to the server to make sure its working- - B) generating random data from scratch is very slow For example, running the following takes over 10 minutes to startup: ```bash vllm bench serve --base-url http://infra-wide-ep-pd-inference-gateway-istio.llm-d-wide-ep-pd.svc.cluster.local --model deepseek-ai/DeepSeek-V3-0324 --dataset-name random --random-input-len 2000 --random-output-len 1000 --max-concurrency 10000 --num-prompts 100000 --seed $(date +%s) --ignore-eos ``` Update the script to: - A) use a tiny request to ensure the server is working (e.g. 200 prompt tokens, 10 decode tokens) - B) have a more efficient way to generate random data (either in parallel or all at once). Ideally generating 100000 prompts should take < 10s ### Alternatives none ### Additional context none ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: erve` startup time with random data help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch There are some issues with the benchmark script for long requests - A) we send a single test...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ### 🚀 The feature, motivation and pitch There are some issues with the benchmark script for long requests - A) we send a single test request to the server to make sure its working- - B) generating random data from scrat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: working (e.g. 200 prompt tokens, 10 decode tokens) - B) have a more efficient way to generate random data (either in parallel or all at once). Ideally generating 100000 prompts should take < 10s ### Alternatives none ##...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: one ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: -wide-ep-pd-inference-gateway-istio.llm-d-wide-ep-pd.svc.cluster.local --model deepseek-ai/DeepSeek-V3-0324 --dataset-name random --random-input-len 2000 --random-output-len 1000 --max-concurrency 10000 --num-prompts 10...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
