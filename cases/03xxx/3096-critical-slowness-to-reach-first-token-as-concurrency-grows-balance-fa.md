# vllm-project/vllm#3096: critical slowness to reach first token as concurrency grows -- balance fairness vs. throughput?

| 字段 | 值 |
| --- | --- |
| Issue | [#3096](https://github.com/vllm-project/vllm/issues/3096) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> critical slowness to reach first token as concurrency grows -- balance fairness vs. throughput?

### Issue 正文摘录

Doing pytest parallel attack on vllm with OpenAI client. Running these on A100 each model, 70b and cabybara ares on 4*A100 80GB, Mixtral on 2*A100 80GB. e.g. for 70b we run: ``` python -m vllm.entrypoints.openai.api_server \ --port=5000 \ --host=0.0.0.0 \ --model=h2oai/h2ogpt-4096-llama2-70b-chat \ --tokenizer=hf-internal-testing/llama-tokenizer \ --tensor-parallel-size=4 \ --seed 1234 \ --trust-remote-code \ --max-num-batched-tokens 8192 \ --download-dir=/workspace/.cache/huggingface/hub ``` or for Mistral 7b v0.2: ``` python -m vllm.entrypoints.openai.api_server \ --port=5004 \ --host=0.0.0.0 \ --model=mistralai/Mistral-7B-Instruct-v0.2 \ --tensor-parallel-size=1 \ --seed 1234 \ --trust-remote-code \ --max-num-batched-tokens 131072 \ --download-dir=/workspace/.cache/huggingface/hub ``` i.e. high batching. or for Mixtral: ``` python -m vllm.entrypoints.openai.api_server \ --port=5002 \ --host=0.0.0.0 \ --model mistralai/Mixtral-8x7B-Instruct-v0.1 \ --seed 1234 \ --tensor-parallel-size=2 \ --max-num-batched-tokens=163840 \ --max-log-len=100 ``` also pretty high batching size. However, while it's understandable that the concurrency increase leads to lower tokens per second, most co...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: parallel attack on vllm with OpenAI client. Running these on A100 each model, 70b and cabybara ares on 4*A100 80GB, Mixtral on 2*A100 80GB. e.g. for 70b we run: ``` python -m vllm.entrypoints.openai.api_server \ --port=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ach first token as concurrency grows -- balance fairness vs. throughput? stale Doing pytest parallel attack on vllm with OpenAI client. Running these on A100 each model, 70b and cabybara ares on 4*A100 80GB, Mixtral on...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: owness to reach first token as concurrency grows -- balance fairness vs. throughput? stale Doing pytest parallel attack on vllm with OpenAI client. Running these on A100 each model, 70b and cabybara ares on 4*A100 80GB,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ing pytest parallel attack on vllm with OpenAI client. Running these on A100 each model, 70b and cabybara ares on 4*A100 80GB, Mixtral on 2*A100 80GB. e.g. for 70b we run: ``` python -m vllm.entrypoints.openai.api_serve...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
