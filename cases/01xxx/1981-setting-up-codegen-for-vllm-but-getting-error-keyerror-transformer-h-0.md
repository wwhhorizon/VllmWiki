# vllm-project/vllm#1981: Setting up CodeGen for vllm but getting error "KeyError: 'transformer.h.0.attn.causal_mask'"

| 字段 | 值 |
| --- | --- |
| Issue | [#1981](https://github.com/vllm-project/vllm/issues/1981) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Setting up CodeGen for vllm but getting error "KeyError: 'transformer.h.0.attn.causal_mask'"

### Issue 正文摘录

I have created a new 'codegen' adaptor for vllm but am getting the error "KeyError: 'transformer.h.0.attn.causal_mask'" when trying to do my first test. Need help to find and fix the issue. Exception: INFO 12-08 05:00:54 llm_engine.py:73] Initializing an LLM engine with config: model='Salesforce/codegen-350M-mono', tokenizer='Salesforce/codegen-350M-mono', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. Traceback (most recent call last): File "/content/drive/MyDrive/Workspace/vllm-main/./examples/offline_inference.py", line 14, in llm = LLM(model="Salesforce/codegen-350M-mono") File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 93, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 246, in from_engine_args engine = cls(*engine_configs, File "/usr/local/lib/python3.10/dist-packages/...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) Special tokens have...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: n: INFO 12-08 05:00:54 llm_engine.py:73] Initializing an LLM engine with config: model='Salesforce/codegen-350M-mono', tokenizer='Salesforce/codegen-350M-mono', tokenizer_mode=auto, revision=None, tokenizer_revision=Non...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. Traceback (most recent call last...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) Special tokens...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n-350M-mono") # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print t...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
