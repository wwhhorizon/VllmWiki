# vllm-project/vllm#1087: if token limit reached in OpenAI API, client hangs

| 字段 | 值 |
| --- | --- |
| Issue | [#1087](https://github.com/vllm-project/vllm/issues/1087) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> if token limit reached in OpenAI API, client hangs

### Issue 正文摘录

Related: https://github.com/vllm-project/vllm/issues/525 Repro: * Start vllm, e.g. ```bash export NCCL_IGNORE_DISABLED_P2P=1 export CUDA_VISIBLE_DEVICESs=0,1,2,3 python -m vllm.entrypoints.openai.api_server --port=5000 --host=0.0.0.0 --model h2oai/h2ogpt-4096-llama2-70b-chat --tokenizer=hf-internal-testing/llama-tokenizer --tensor-parallel-size=4 --seed 1234 ``` * Connect via OpenAI API and make prompt too large (> 2560).

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ython -m vllm.entrypoints.openai.api_server --port=5000 --host=0.0.0.0 --model h2oai/h2ogpt-4096-llama2-70b-chat --tokenizer=hf-internal-testing/llama-tokenizer --tensor-parallel-size=4 --seed 1234 ``` * Connect via Ope...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ro: * Start vllm, e.g. ```bash export NCCL_IGNORE_DISABLED_P2P=1 export CUDA_VISIBLE_DEVICESs=0,1,2,3 python -m vllm.entrypoints.openai.api_server --port=5000 --host=0.0.0.0 --model h2oai/h2ogpt-4096-llama2-70b-chat --t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: .0.0.0 --model h2oai/h2ogpt-4096-llama2-70b-chat --tokenizer=hf-internal-testing/llama-tokenizer --tensor-parallel-size=4 --seed 1234 ``` * Connect via OpenAI API and make prompt too large (> 2560).

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
