# vllm-project/vllm#2419: anyone can Qwen-14B-Chat-AWQ work with VLLM/TP ?

| 字段 | 值 |
| --- | --- |
| Issue | [#2419](https://github.com/vllm-project/vllm/issues/2419) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> anyone can Qwen-14B-Chat-AWQ work with VLLM/TP ?

### Issue 正文摘录

I trying quantize [lightblue/qarasu-14B-chat-plus-unleashed](https://huggingface.co/lightblue/qarasu-14B-chat-plus-unleashed) based [Qwen/Qwen-14B-Chat](https://huggingface.co/Qwen/Qwen-14B-Chat) . Transformer(4.36.2) with autoawq(0.1.8) , it works. VLLM(0.2.7) with autoawq(0.1.8) , **tensor_parallel_size=1**, it works. But VLLM(0.2.7) with autoawq(0.1.8) , **tensor_parallel_size=2**, ray worker dead with Error. **Engin args** ``` INFO 01-11 08:55:54 llm_engine.py:70] Initializing an LLM engine with config: model='/usr/local/model/llm', tokenizer='/usr/local/model/llm', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=awq, enforce_eager=False, seed=0) ``` **Error** ``` File "/usr/local/api/chat_models/chat_local_vllm.py", line 112, in _prepare_vllm engine = AsyncLLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 500, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", li...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: anyone can Qwen-14B-Chat-AWQ work with VLLM/TP ? stale I trying quantize [lightblue/qarasu-14B-chat-plus-unleashed](https://huggingface.co/lightblue/qarasu-14B-chat-plus-unleashed) based [Qwen/Qwen-14B-Chat](https://hug...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: anyone can Qwen-14B-Chat-AWQ work with VLLM/TP ? stale I trying quantize [lightblue/qarasu-14B-chat-plus-unleashed](https://huggingface.co/lightblue/qarasu-14B-chat-plus-unleashed) based [Qwen/Qwen-14B-Chat](https://hug...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: d_format=auto, tensor_parallel_size=2, quantization=awq, enforce_eager=False, seed=0) ``` **Error** ``` File "/usr/local/api/chat_models/chat_local_vllm.py", line 112, in _prepare_vllm engine = AsyncLLMEngine.from_engin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: -Chat-AWQ is work with same parameters. Qwen-**14B**-Chat has different architecture?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: anyone can Qwen-14B-Chat-AWQ work with VLLM/TP ? stale I trying quantize [lightblue/qarasu-14B-chat-plus-unleashed](https://huggingface.co/lightblue/qarasu-14B-chat-plus-unleashed) based [Qwen/Qwen-14B-Chat](https://hug...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
