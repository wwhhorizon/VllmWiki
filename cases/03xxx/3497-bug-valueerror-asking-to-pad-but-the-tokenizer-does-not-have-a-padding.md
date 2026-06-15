# vllm-project/vllm#3497: [Bug]: ValueError: Asking to pad but the tokenizer does not have a padding token. Please select a token to use as `pad_token` `(tokenizer.pad_token = tokenizer.eos_token e.g.)` or add a new pad token via `tokenizer.add_special_tokens({'pad_token': '[PAD]'})`

| 字段 | 值 |
| --- | --- |
| Issue | [#3497](https://github.com/vllm-project/vllm/issues/3497) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: Asking to pad but the tokenizer does not have a padding token. Please select a token to use as `pad_token` `(tokenizer.pad_token = tokenizer.eos_token e.g.)` or add a new pad token via `tokenizer.add_special_tokens({'pad_token': '[PAD]'})`

### Issue 正文摘录

### Your current environment ```text python3 benchmarks/benchmark_throughput.py --backend hf --hf-max-batch-size 20 --model /data/pretrain_models/Baichuan2-7B-Chat --trust-remote-code --input-len 512 --output-len 2048 --num-prompts 20 ``` ### 🐛 Describe the bug Warning: import flash_attn rotary fail, please install FlashAttention rotary to get higher efficiency https://github.com/Dao-AILab/flash-attention/tree/main/csrc/rotary Warning: import flash_attn rms_norm fail, please install FlashAttention layer_norm to get higher efficiency https://github.com/Dao-AILab/flash-attention/tree/main/csrc/layer_norm Warning: import flash_attn fail, please install FlashAttention to get higher efficiency https://github.com/Dao-AILab/flash-attention Loading checkpoint shards: 0%| | 0/8 [00:00 main(args) File "/data/luhairong/work/LLM/vllm/vllm-0.3.3/benchmarks/benchmark_throughput.py", line 219, in main elapsed_time = run_hf(requests, args.model, tokenizer, args.n, File "/data/luhairong/work/LLM/vllm/vllm-0.3.3/benchmarks/benchmark_throughput.py", line 154, in run_hf input_ids = tokenizer(batch, return_tensors="pt", File "/data/luhairong/anaconda3/envs/llm2/lib/python3.8/site-packages/transformers...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tokenizer.eos_token e.g.)` or add a new pad token via `tokenizer.add_special_tokens({'pad_token': '[PAD]'})` bug;stale ### Your current environment ```text python3 benchmarks/benchmark_throughput.py --backend hf --hf-ma...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rrent environment ```text python3 benchmarks/benchmark_throughput.py --backend hf --hf-max-batch-size 20 --model /data/pretrain_models/Baichuan2-7B-Chat --trust-remote-code --input-len 512 --output-len 2048 --num-prompt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vironment ```text python3 benchmarks/benchmark_throughput.py --backend hf --hf-max-batch-size 20 --model /data/pretrain_models/Baichuan2-7B-Chat --trust-remote-code --input-len 512 --output-len 2048 --num-prompts 20 ```...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: pad token via `tokenizer.add_special_tokens({'pad_token': '[PAD]'})` bug;stale ### Your current environment ```text python3 benchmarks/benchmark_throughput.py --backend hf --hf-max-batch-size 20 --model /data/pretrain_m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ken': '[PAD]'})` bug;stale ### Your current environment ```text python3 benchmarks/benchmark_throughput.py --backend hf --hf-max-batch-size 20 --model /data/pretrain_models/Baichuan2-7B-Chat --trust-remote-code --input-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
