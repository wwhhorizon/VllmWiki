# vllm-project/vllm#10481: [Bug]: LLaMA3.2-1B finetuned w/ Sentence Transformer. --> ValueError: Model architectures ['LlamaModel'] are not supported for now.

| 字段 | 值 |
| --- | --- |
| Issue | [#10481](https://github.com/vllm-project/vllm/issues/10481) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: LLaMA3.2-1B finetuned w/ Sentence Transformer. --> ValueError: Model architectures ['LlamaModel'] are not supported for now.

### Issue 正文摘录

### Your current environment !pip install vllm==0.5.4 !pip install git+https://github.com/huggingface/transformers !pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/cu121 ### Model Input Dumps _No response_ ### 🐛 Describe the bug We finetune **LlaMA-3.2-1B** with **Sentence Transformers** latest version, it works well after finetuning and benchmark. However, once we tried to load it with vLLM, the error occured: !pip install vllm==0.5.4 !pip install git+https://github.com/huggingface/transformers !pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/cu121 model_path = "path to LlaMA-3.2-1B Sentence Transformer checkpoint model saved" - works without vLLM. llm = LLM(model=model_path, tokenizer=model_path, #gpu_memory_utilization=0.5, dtype="auto", kv_cache_dtype="auto", tensor_parallel_size=1, max_seq_len_to_capture=2048, max_num_batched_tokens=2048, max_num_seqs=2048, use_v2_block_manager=True, enforce_eager=True, trust_remote_code=True) ==> ERROR below: ValueError Traceback (most recent call last) Cell In[17], line 2 1 # Create an LLM. ----> 2 llm = LLM(model=model_pa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: [Bug]: LLaMA3.2-1B finetuned w/ Sentence Transformer. --> ValueError: Model architectures ['LlamaModel'] are not supported for now. bug ### Your current environment !pip install vllm==0.5.4 !pip install git+https://gith...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: odel'] are not supported for now. bug ### Your current environment !pip install vllm==0.5.4 !pip install git+https://github.com/huggingface/transformers !pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: g]: LLaMA3.2-1B finetuned w/ Sentence Transformer. --> ValueError: Model architectures ['LlamaModel'] are not supported for now. bug ### Your current environment !pip install vllm==0.5.4 !pip install git+https://github....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 159 engine_args, usage_context=UsageContext.LLM_CLASS) 160 self.request_counter = Counter() File ~/env/lib/python3.10/site-packages/vllm/engine/llm_engine.py:445, in LLMEngine.from_engine_args(cls, engine_args, usage_co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: e the bug We finetune **LlaMA-3.2-1B** with **Sentence Transformers** latest version, it works well after finetuning and benchmark. However, once we tried to load it with vLLM, the error occured: !pip install vllm==0.5....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
