# vllm-project/vllm#2418: ValueError: The model's max seq len (4096) is larger than the maximum number of tokens that can be stored in KV cache (3664). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine.`

| 字段 | 值 |
| --- | --- |
| Issue | [#2418](https://github.com/vllm-project/vllm/issues/2418) |
| 状态 | closed |
| 标签 |  |
| 评论 | 42; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: The model's max seq len (4096) is larger than the maximum number of tokens that can be stored in KV cache (3664). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine.`

### Issue 正文摘录

I followed the Quickstart tutorial and deployed the Chinese-llama-alpaca-2 model using vllm, and I got the following error. `***@***:~/Code/experiment/***/ToG$ CUDA_VISIBLE_DEVICES=0 python load_llm.py INFO 01-11 15:51:02 llm_engine.py:70] Initializing an LLM engine with config: model='/home/***/***/models/alpaca-2', tokenizer='/home/***/***/models/alpaca-2', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, enforce_eager=False, seed=0) INFO 01-11 15:51:18 llm_engine.py:275] # GPU blocks: 229, # CPU blocks: 512 Traceback (most recent call last): File "load_llm.py", line 8, in llm = LLM(model='/home/***/***/models/alpaca-2') File "/home/***/anaconda3/envs/lys-llm-env/lib/python3.8/site-packages/vllm/entrypoints/llm.py", line 105, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/home/***/anaconda3/envs/lys-llm-env/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 309, in from_engine_args engine = cls(*engine_configs, File "/home/***/anaconda3/envs/lys-llm-env/lib/python3.8/site-packages/vllm/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ValueError: The model's max seq len (4096) is larger than the maximum number of tokens that can be stored in KV cache (3664). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, enforce_eager=False, seed=0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: vllm, and I got the following error. `***@***:~/Code/experiment/***/ToG$ CUDA_VISIBLE_DEVICES=0 python load_llm.py INFO 01-11 15:51:02 llm_engine.py:70] Initializing an LLM engine with config: model='/home/***/***/model...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, enforce_eager=False, s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: del_len` when initializing the engine.` my code is: ```python from vllm import LLM, SamplingParams prompts = [ "hello, who is you?", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model='/home...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
