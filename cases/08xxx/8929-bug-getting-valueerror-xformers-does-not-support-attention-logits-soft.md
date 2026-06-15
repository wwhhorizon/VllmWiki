# vllm-project/vllm#8929: [Bug]: Getting `ValueError: XFormers does not support attention logits soft capping.` in colab on T4

| 字段 | 值 |
| --- | --- |
| Issue | [#8929](https://github.com/vllm-project/vllm/issues/8929) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Getting `ValueError: XFormers does not support attention logits soft capping.` in colab on T4

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug My code is: ```python import vllm model_id = 'google/gemma-2-9b' llm = vllm.LLM(model=model_id, dtype='half') ``` Colab link: https://colab.research.google.com/drive/1YobPvwjmEpeu165diojf85GNLbmLtx61?usp=sharing Getting error: ``` ValueError Traceback (most recent call last) [ ](https://localhost:8080/#) in () 1 import vllm 2 model_id = 'google/gemma-2-9b' ----> 3 llm = vllm.LLM(model=model_id, dtype='half') 17 frames [/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py](https://localhost:8080/#) in __init__(self, model, tokenizer, tokenizer_mode, skip_tokenizer_init, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, cpu_offload_gb, enforce_eager, max_context_len_to_capture, max_seq_len_to_capture, disable_custom_all_reduce, disable_async_output_proc, mm_processor_kwargs, **kwargs) 212 **kwargs, 213 ) --> 214 self.llm_engine = LLMEngine.from_engine_args( 215 engine_args, usage_context=UsageContext.LLM_CLASS) 216 self.request_counter = Counter() [/usr/local/lib/python3.10/dist-packages/vllm/engine/llm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: put Dumps _No response_ ### 🐛 Describe the bug My code is: ```python import vllm model_id = 'google/gemma-2-9b' llm = vllm.LLM(model=model_id, dtype='half') ``` Colab link: https://colab.research.google.com/drive/1YobPv...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: s soft capping.` in colab on T4 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug My code is: ```python import vllm model_id = 'google/gemma-2-9b' llm = vllm.LLM(model=model_id,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: engine_args, usage_context=UsageContext.LLM_CLASS) 216 self.request_counter = Counter() [/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py](https://localhost:8080/#) in from_engine_args(cls, engine_args,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: mport vllm model_id = 'google/gemma-2-9b' llm = vllm.LLM(model=model_id, dtype='half') ``` Colab link: https://colab.research.google.com/drive/1YobPvwjmEpeu165diojf85GNLbmLtx61?usp=sharing Getting error: ``` ValueError...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: is not None) 83 impl_cls = attn_backend.get_impl_cls() ---> 84 self.impl = impl_cls(num_heads, head_size, scale, num_kv_heads, 85 alibi_slopes, sliding_window, kv_cache_dtype, 86

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
