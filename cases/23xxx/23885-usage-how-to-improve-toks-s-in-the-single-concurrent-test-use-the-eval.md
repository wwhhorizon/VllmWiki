# vllm-project/vllm#23885: [Usage]: how to improve toks/s in the single-concurrent test use the  evalscope tool? deploy qwen3-30-a3b model use 4 cards.

| 字段 | 值 |
| --- | --- |
| Issue | [#23885](https://github.com/vllm-project/vllm/issues/23885) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to improve toks/s in the single-concurrent test use the  evalscope tool? deploy qwen3-30-a3b model use 4 cards.

### Issue 正文摘录

### Your current environment start command is : VLLM_USE_FLASH_ATTN_PA=1 vllm serve /data/Qwen3-30B-A3B -tp=4 --max-num-seqs 128 --dtype bfloat16 --block-size 32 --max-num-batched-tokens 128 --enable-prefix-caching --max-model-len 32678 the follow is the new test information, +-----------------------------------+----------+ | Key | Value | +===================================+==========+ | Time taken for tests (s) | 605.768 | +-----------------------------------+----------+ | Number of concurrency | 1 | +-----------------------------------+----------+ | Total requests | 20 | +-----------------------------------+----------+ | Succeed requests | 20 | +-----------------------------------+----------+ | Failed requests | 0 | +-----------------------------------+----------+ | Output token throughput (tok/s) | 32.2219 | +-----------------------------------+----------+ | Total token throughput (tok/s) | 33.1876 | +-----------------------------------+----------+ | Request throughput (req/s) | 0.033 | +-----------------------------------+----------+ | Average latency (s) | 30.2874 | +-----------------------------------+----------+ | Average time to first token (s) | 0.0419 | +--------------...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Usage]: how to improve toks/s in the single-concurrent test use the evalscope tool? deploy qwen3-30-a3b model use 4 cards. usage;stale ### Your current environment start command is : VLLM_USE_FLASH_ATTN_PA=1 vllm serve...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: LASH_ATTN_PA=1 vllm serve /data/Qwen3-30B-A3B -tp=4 --max-num-seqs 128 --dtype bfloat16 --block-size 32 --max-num-batched-tokens 128 --enable-prefix-caching --max-model-len 32678 the follow is the new test information,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ove toks/s in the single-concurrent test use the evalscope tool? deploy qwen3-30-a3b model use 4 cards. usage;stale ### Your current environment start command is : VLLM_USE_FLASH_ATTN_PA=1 vllm serve /data/Qwen3-30B-A3B...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: st use the evalscope tool? deploy qwen3-30-a3b model use 4 cards. usage;stale ### Your current environment start command is : VLLM_USE_FLASH_ATTN_PA=1 vllm serve /data/Qwen3-30B-A3B -tp=4 --max-num-seqs 128 --dtype bflo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
