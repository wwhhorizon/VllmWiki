# vllm-project/vllm#1071: AWQ: vLLM cannot load AWQ models in Safetensors format

| 字段 | 值 |
| --- | --- |
| Issue | [#1071](https://github.com/vllm-project/vllm/issues/1071) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AWQ: vLLM cannot load AWQ models in Safetensors format

### Issue 正文摘录

Hi guys ## Issue: vLLM cannot load AWQ models saved in Safetensors format by AutoAWQ. ### The error ``` File "/home/vllm/vllm/vllm/model_executor/models/llama.py", line 340, in load_weights loaded_weight = loaded_weight.T AttributeError: 'builtins.PySafeSlice' object has no attribute 'T' ``` ### Background AutoAWQ recently gained the ability to save models in safetensors format. I requested this was added before I started mass AWQ production, because: - safetensors is considered the best format for the future, as it's safer and quicker - it is hoped that Transformers will soon add native AWQ support, and when they do they will definitely require safetensors support. Safetensors was added to AutoAWQ in this PR: https://github.com/casper-hansen/AutoAWQ/pull/47 I would really like for there to be working AWQ support in vLLM before I start mass releasing AWQs, but I also want to be able to release models in Safetensors format, so that I don't have update them all later. So it'd be great if we could get a fix for this, so I can start pushing out lots of models for people to try. ### Example Safetensors AWQ model for testing, and log of trying to load it in vLLM Model: [TheBlokeAI/Test-...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: AWQ: vLLM cannot load AWQ models in Safetensors format bug Hi guys ## Issue: vLLM cannot load AWQ models saved in Safetensors format by AutoAWQ. ### The error ``` File "/home/vllm/vllm/vllm/model_executor/models/llama.p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Log: ``` Launching vLLM with args: --model TheBlokeAI/Test-AWQ-13B-128 --quantization awq --host 0.0.0.0 INFO 09-17 14:21:24 llm_engine.py:72] Initializing an LLM engine with config: model='TheBlokeAI/Test-AWQ-13B-128',...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: st-AWQ-13B-128', tokenizer_mode=auto, revision=None, trust_remote_code=False, dtype=torch.float16, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) Traceback (most recent call last)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: oAWQ recently gained the ability to save models in safetensors format. I requested this was added before I started mass AWQ production, because: - safetensors is considered the best format for the future, as it's safer...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: lots of models for people to try. ### Example Safetensors AWQ model for testing, and log of trying to load it in vLLM Model: [TheBlokeAI/Test-AWQ-13B-128](https://huggingface.co/TheBlokeAI/Test-AWQ-13B-128/tree/main) Lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
