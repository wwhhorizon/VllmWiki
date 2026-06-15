# vllm-project/vllm#2136: KV cache is low, memory profiling does not see the remaining VRAM

| 字段 | 值 |
| --- | --- |
| Issue | [#2136](https://github.com/vllm-project/vllm/issues/2136) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> KV cache is low, memory profiling does not see the remaining VRAM

### Issue 正文摘录

GPUs: 2x 4090 (2x24GB) Regarding my long context issue with CodeLlama above: - vLLM 0.2.3: `# GPU blocks: 1464, # CPU blocks: 1310` - vLLM 0.2.4: `# GPU blocks: 1464, # CPU blocks: 1310` - vLLM 0.2.5 and `main`: `# GPU blocks: 112, # CPU blocks: 1310` Something broke in VRAM profiling or before that, which prevents vLLM from using all remaining VRAM for the KV cache. Profiling already gives too low values and there is no way to manually override it from the command line. Both GPUs had ~8GB free VRAM after loading the model, so vLLM just fails to allocate it as cache. Command: ```sh python -O -u -m vllm.entrypoints.openai.api_server \ --model=TheBloke/CodeLlama-13B-Instruct-fp16 \ --chat-template=$HOME/bin/templates/llama-2-chat.jinja \ --served-model-name=model \ --host=0.0.0.0 \ --port=8000 \ --max-model-len=16384 \ --max-num-seqs=16 \ --tensor-parallel-size=2 \ --swap-space=8 \ --gpu-memory-utilization=0.95 \ --disable-log-requests ``` Tested OK up to the full 16k context window on vLLM 0.2.3 and 0.2.4. The test fails on 0.2.5 if the sequence is longer than about 1700 tokens. (I think the exact limit is 112 * 16 due to block manager allocation and the block size of 16.) vLLM 0.2...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ng VRAM GPUs: 2x 4090 (2x24GB) Regarding my long context issue with CodeLlama above: - vLLM 0.2.3: `# GPU blocks: 1464, # CPU blocks: 1310` - vLLM 0.2.4: `# GPU blocks: 1464, # CPU blocks: 1310` - vLLM 0.2.5 and `main`:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: KV cache is low, memory profiling does not see the remaining VRAM GPUs: 2x 4090 (2x24GB) Regarding my long context issue with CodeLlama above: - vLLM 0.2.3: `# GPU blocks: 1464, # CPU blocks: 1310` - vLLM 0.2.4: `# GPU...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: KV cache is low, memory profiling does not see the remaining VRAM GPUs: 2x 4090 (2x24GB) Regarding my long context issue with CodeLlama above: - vLLM 0.2.3: `# GPU blocks: 1464, # CPU blocks: 1310` - vLLM 0.2.4: `# GPU
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: garding my long context issue with CodeLlama above: - vLLM 0.2.3: `# GPU blocks: 1464, # CPU blocks: 1310` - vLLM 0.2.4: `# GPU blocks: 1464, # CPU blocks: 1310` - vLLM 0.2.5 and `main`: `# GPU blocks: 112, # CPU blocks...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 2 \ --swap-space=8 \ --gpu-memory-utilization=0.95 \ --disable-log-requests ``` Tested OK up to the full 16k context window on vLLM 0.2.3 and 0.2.4. The test fails on 0.2.5 if the sequence is longer than about 1700 toke...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
