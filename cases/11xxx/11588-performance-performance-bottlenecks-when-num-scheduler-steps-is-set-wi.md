# vllm-project/vllm#11588: [Performance]: Performance bottlenecks when num-scheduler-steps is set with enable-chunked-prefill and large prompts.

| 字段 | 值 |
| --- | --- |
| Issue | [#11588](https://github.com/vllm-project/vllm/issues/11588) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Performance bottlenecks when num-scheduler-steps is set with enable-chunked-prefill and large prompts.

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am having trouble realising performance gains when setting the num-scheduler-steps parameter for online inference via the openai server. model: llama 3.3. 70b instruct Test suite: 600 large prompts from 5k to 15k tokens each sent simultaneously. Hardware: 8 x A100 80GB GPU's. when using the below arguments: ``` - '--model=/mnt2/genai/meta-llama--Llama-3.3-70B-Instruct' - '--served-model-name=meta-llama--Llama-3.3-70B-Instruct' - '--port=5000' - '--block-size=32' - '--disable-log-requests' - '--distributed-executor-backend=ray' - '--dtype=bfloat16' - '--enable-chunked-prefill' - '--enforce-eager' - '--gpu-memory-utilization=0.90' - '--load-format=safetensors' - '--max-model-len=128000' - '--max-num-batched-tokens=128000' - '--max-num-seqs=1024' - '--tensor-parallel-size=8' ``` I can get responses for my 600 prompts in approximately 750 seconds. However when adding `--num-scheduler-steps=64` to the above, I actually see a lower throughput and it takes around 850 seconds to process all the responses. While looking through the logs, I can see that a...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Performance]: Performance bottlenecks when num-scheduler-steps is set with enable-chunked-prefill and large prompts. performance;stale ### Proposal to improve performance _No response_ ### Report of performance regress...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: - '--distributed-executor-backend=ray' - '--dtype=bfloat16' - '--enable-chunked-prefill' - '--enforce-eager' - '--gpu-memory-utilization=0.90' - '--load-format=safetensors' - '--max-model-len=12
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: Llama-3.3-70B-Instruct' - '--port=5000' - '--block-size=32' - '--disable-log-requests' - '--distributed-executor-backend=ray' - '--dtype=bfloat16' - '--enable-chunked-prefill' - '--enforce-eager'
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: -scheduler-steps parameter for online inference via the openai server. model: llama 3.3. 70b instruct Test suite: 600 large prompts from 5k to 15k tokens each sent simultaneously. Hardware: 8 x A100 80GB GPU's. when usi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am having trouble realising performance gains when setting the num-scheduler-steps par...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
