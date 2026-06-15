# vllm-project/vllm#18267: [Bug]: Llama-4 on long-context tasks generates garbage with pipeline parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#18267](https://github.com/vllm-project/vllm/issues/18267) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama-4 on long-context tasks generates garbage with pipeline parallelism

### Issue 正文摘录

### Your current environment I think that there is something broken with long context on Llama-4 and pipeline parallelism in vLLM. I am serving the model like this: `vllm serve meta-llama/Llama-4-Scout-17B-16E-Instruct -tp 8 -pp $PP --dtype auto --max-model-len 524288 --gpu-memory-utilization 0.9 --enable-chunked-prefill` and I am evaluating on RULER (128k) with lm-evaluation-harness: ``` lm_eval \ --model local-completions \ --model_args model="meta-llama/Llama-4-Scout-17B-16E-Instruct",tokenizer="meta-llama/Llama-4-Scout-17B-16E-Instruct",base_url="http://localhost:8000/v1/completions",max_retries=3,timeout=300,tokenized_requests=True,add_bos_token=False,max_length=524288,num_concurrent=1 \ --metadata='{"max_seq_lengths":[131072]}' \ --tasks niah_single_1 \ \ --show_config ``` 1. for `PP=1` : `niah_single_1 = 1.0` 2. for `PP=2`: `niah_single_2 = 0.0` This does not happen on shorter sequences like 4k and 8k. Both PP=1 and PP=2 have the score of 1.0. The same issue happens for Maverick model as well. vLLM version: 0.8.5.post1 Engine: V0 (V1 engine doesn't work due to https://github.com/vllm-project/vllm/issues/18023#issuecomment-2887043290) ### 🐛 Describe the bug . ### Before subm...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Llama-4 on long-context tasks generates garbage with pipeline parallelism bug ### Your current environment I think that there is something broken with long context on Llama-4 and pipeline parallelism in vLLM. I a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : Llama-4 on long-context tasks generates garbage with pipeline parallelism bug ### Your current environment I think that there is something broken with long context on Llama-4 and pipeline parallelism in vLLM. I am ser...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: tions",max_retries=3,timeout=300,tokenized_requests=True,add_bos_token=False,max_length=524288,num_concurrent=1 \ --metadata='{"max_seq_lengths":[131072]}' \ --tasks niah_single_1 \ \ --show_config ``` 1. for `PP=1` : `...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: uto --max-model-len 524288 --gpu-memory-utilization 0.9 --enable-chunked-prefill` and I am evaluating on RULER (128k) with lm-evaluation-harness: ``` lm_eval \ --model local-completions \ --model_args model="meta-llama/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: n 524288 --gpu-memory-utilization 0.9 --enable-chunked-prefill` and I am evaluating on RULER (128k) with lm-evaluation-harness: ``` lm_eval \ --model local-completions \ --model_args model="meta-llama/Llama-4-Scout-17B-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
