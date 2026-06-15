# vllm-project/vllm#2733: Better defaults to match Hugging Face

| 字段 | 值 |
| --- | --- |
| Issue | [#2733](https://github.com/vllm-project/vllm/issues/2733) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;sampling |
| 症状 | slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Better defaults to match Hugging Face

### Issue 正文摘录

While I appreciate the fact that CUDA kernels can cause issues with bitwize exactness, there's an issue with vLLM defaults that causes significantly worse results on benchmarks than using the corresponding slow Huggingface code. This becomes a much bigger deal with using the openai api_endpoint.py script - the lack of easy way to know the defaults of vllm + how to pass arguments that arent normally accepted by the completions API caused me to waste practically an entire day. Hopefully the solution below helps someone not waste that much time. So in an effort to enable at least greedy scores to be closely aligned, here is some example code that helps achieve nearly same greedy scores on HumanEval compared to HF but about 20x faster. # Serve model (Note: as of v0.3.0 there a bug with logprobs calculation and using echo=True). The fix is easy but will need manual patching of the `serving_completion.py` script. We also use a large max-num-seqs cause we want to process entire dataset in one pass if memory allows. I'll use a mistral 7b instruct 0.1 for this example. ```python python -m vllm.entrypoints.openai.api_server \ --model "${MODEL_PATH}" \ --trust-remote-code \ --seed=${SEED} \...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: nificantly worse results on benchmarks than using the corresponding slow Huggingface code. This becomes a much bigger deal with using the openai api_endpoint.py script - the lack of easy way to know the defaults of vllm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Better defaults to match Hugging Face stale While I appreciate the fact that CUDA kernels can cause issues with bitwize exactness, there's an issue with vLLM defaults that causes significantly worse results on benchmark...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Better defaults to match Hugging Face stale While I appreciate the fact that CUDA kernels can cause issues with bitwize exactness, there's an issue with vLLM defaults that causes significantly worse results on benchmark...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: s an issue with vLLM defaults that causes significantly worse results on benchmarks than using the corresponding slow Huggingface code. This becomes a much bigger deal with using the openai api_endpoint.py script - the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er defaults to match Hugging Face stale While I appreciate the fact that CUDA kernels can cause issues with bitwize exactness, there's an issue with vLLM defaults that causes significantly worse results on benchmarks th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
