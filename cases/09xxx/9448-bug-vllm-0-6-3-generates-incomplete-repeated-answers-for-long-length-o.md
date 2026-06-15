# vllm-project/vllm#9448: [Bug]: vllm 0.6.3 generates incomplete/repeated answers for long length (over 8k) input

| 字段 | 值 |
| --- | --- |
| Issue | [#9448](https://github.com/vllm-project/vllm/issues/9448) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm 0.6.3 generates incomplete/repeated answers for long length (over 8k) input

### Issue 正文摘录

### Your current environment ### Model Input Dumps The input is long context with over 8k tokens ### 🐛 Describe the bug 1. vllm 0.6.2 does not have this bug. 2. We are running vllm 0.6.3 with speculative decoding. When we input long context (over 8k) into the model, the output is truncated and gives incomplete answers. The command we are using is ``` python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8083 --model /home/downloaded_model/Llama-3.2-3B-Instruct/ --speculative_model /home/downloaded_model/Llama-3.2-1B-Instruct/ --served-model-name LLM --tensor-parallel-size 8 --max-model-len 34336 --max-num-seqs 128 --enable-prefix-caching --disable-log-requests --use-v2-block-manager --seed 42 --num_speculative_tokens 5 --gpu_memory_utilization 0.95 --spec-decoding-acceptance-method typical_acceptance_sampler ``` 3. We then run vllm 0.6.3 without speculative decoding, but we still get incomplete answers or repeated answers. The command we use is ``` python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8083 --model /home/downloaded_model/Llama-3.2-3B-Instruct/ --served-model-name LLM --tensor-parallel-size 8 --max-model-len 34336 --max-num-seqs 128 --enabl...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 1. vllm 0.6.2 does not have this bug. 2. We are running vllm 0.6.3 with speculative decoding. When we input long context (over 8k) into the model, the output is truncated and gives incomplete answers. The command we are...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: for long length (over 8k) input bug ### Your current environment ### Model Input Dumps The input is long context with over 8k tokens ### 🐛 Describe the bug 1. vllm 0.6.2 does not have this bug. 2. We are running vllm 0....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ax-num-seqs 128 --enable-prefix-caching --disable-log-requests --use-v2-block-manager --seed 42 --num_speculative_tokens 5 --gpu_memory_utilization 0.95 --spec-decoding-acceptance-method typical_acceptance_sampler ``` 3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
