# vllm-project/vllm#1838: Bad performance using two 4090

| 字段 | 值 |
| --- | --- |
| Issue | [#1838](https://github.com/vllm-project/vllm/issues/1838) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Bad performance using two 4090

### Issue 正文摘录

I am using https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_throughput.py to do some benchmarks and find that two 4090 with tp is not running good as one 4090. ``` $ python benchmark_throughput.py --model /codellama-34b-awq --backend vllm --tokenizer /codellama-34b-awq --num-prompts 200 --quantization awq --dtype float16 --input-len 512 --output-len 512 -tp 1 Namespace(backend='vllm', dataset=None, input_len=512, output_len=512, model='/input0', tokenizer='/input0', quantization='awq', tensor_parallel_size=1, n=1, use_beam_search=False, num_prompts=200, seed=0, hf_max_batch_size=None, trust_remote_code=False, dtype='float16') Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. WARNING 11-29 14:58:35 config.py:398] Casting torch.bfloat16 to torch.float16. WARNING 11-29 14:58:35 config.py:140] awq quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 11-29 14:58:35 llm_engine.py:72] Initializing an LLM engine with config: model='/input0', tokenizer='/input0', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.f...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: is not running good as one 4090. ``` $ python benchmark_throughput.py --model /codellama-34b-awq --backend vllm --tokenizer /codellama-34b-awq --num-prompts 200 --quantization awq --dtype float16 --input-len 512 --outpu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: b-awq --backend vllm --tokenizer /codellama-34b-awq --num-prompts 200 --quantization awq --dtype float16 --input-len 512 --output-len 512 -tp 1 Namespace(backend='vllm', dataset=None, input_len=512, output_len=512, mode...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ut0', quantization='awq', tensor_parallel_size=1, n=1, use_beam_search=False, num_prompts=200, seed=0, hf_max_batch_size=None, trust_remote_code=False, dtype='float16') Special tokens have been added in the vocabulary,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: using two 4090 I am using https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_throughput.py to do some benchmarks and find that two 4090 with tp is not running good as one 4090. ``` $ python benchmark_th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 4090. ``` $ python benchmark_throughput.py --model /codellama-34b-awq --backend vllm --tokenizer /codellama-34b-awq --num-prompts 200 --quantization awq --dtype float16 --input-len 512 --output-len 512 -tp 1 Namespace(b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
