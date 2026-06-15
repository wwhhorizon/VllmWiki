# vllm-project/vllm#37235: [Bug]: Non-monotonic latency at ctx=8192: concurrency 1 slower than concurrency 2 (local vLLM)

| 字段 | 值 |
| --- | --- |
| Issue | [#37235](https://github.com/vllm-project/vllm/issues/37235) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Non-monotonic latency at ctx=8192: concurrency 1 slower than concurrency 2 (local vLLM)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary I observed non-monotonic latency behavior when serving long-context requests locally with vLLM. For a ctx=8192 prompt bucket, p95 latency at concurrency=1 was significantly worse than concurrency=2. Example: - concurrency=1 → p95 ≈ 30.29s - concurrency=2 → p95 ≈ 6.37s This inversion (~4.7× difference) did not appear in smaller context buckets (512 or 2048). ## Prior investigation According to the vLLM documentation chatbot and related issues (e.g. #3096 and #4498), latency—especially TTFT—typically **increases** with concurrency for long contexts because requests queue behind the prefill stage. However, in my experiments with a ctx=8192 prompt bucket, I observed the opposite behavior between concurrency=1 and concurrency=2: - concurrency=1 → p95 ≈ 30.29s - concurrency=2 → p95 ≈ 6.37s This suggests something unusual in how the scheduler or batching interacts with very long prompts at low concurrency. Serve command used for the experiment: ```bash vllm serve Qwen/Qwen2-0.5B-Instruct --host 0.0.0.0 --port 8000 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chat...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ary I observed non-monotonic latency behavior when serving long-context requests locally with vLLM. For a ctx=8192 prompt bucket, p95 latency at concurrency=1 was significantly worse than concurrency=2. Example: - concu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: - concurrency=1 → p95 ≈ 30.29s - concurrency=2 → p95 ≈ 6.37s This inversion (~4.7× difference) did not appear in smaller context buckets (512 or 2048). ## Prior investigation According to the vLLM documentation chatbot...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: y=2 → p95 ≈ 6.37s This inversion (~4.7× difference) did not appear in smaller context buckets (512 or 2048). ## Prior investigation According to the vLLM documentation chatbot and related issues (e.g. #3096 and #4498),...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Non-monotonic latency at ctx=8192: concurrency 1 slower than concurrency 2 (local vLLM) bug ### Your current environment ### 🐛 Describe the bug ## Summary I observed non-monotonic latency behavior when serving lo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: concurrency. Serve command used for the experiment: ```bash vllm serve Qwen/Qwen2-0.5B-Instruct --host 0.0.0.0 --port 8000 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
