# vllm-project/vllm#2749: Mistral model architecture is not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#2749](https://github.com/vllm-project/vllm/issues/2749) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mistral model architecture is not supported

### Issue 正文摘录

The Mistral model is [🤗Salesforce/SFR-Embedding-Mistral](https://huggingface.co/Salesforce/SFR-Embedding-Mistral). ```shell INFO 02-05 03:05:04 llm_engine.py:72] Initializing an LLM engine with config: model='SFR-Embedding-Mistral', tokenizer='SFR-Embedding-Mistral', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, seed=0) Traceback (most recent call last): File "/app/embedding.py", line 33, in model = LLM('SFR-Embedding-Mistral') File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 109, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 356, in from_engine_args engine = cls(*engine_configs, File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 111, in __init__ self._init_workers() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 152, in _init_workers self._run_workers("load_mode...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: Mistral model architecture is not supported The Mistral model is [🤗Salesforce/SFR-Embedding-Mistral](https://huggingface.co/Salesforce/SFR-Embedding-Mistral). ```shell INFO 02-05 03:05:04 llm_engine.py:72] Initializing...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM',...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Mistral model architecture is not supported The Mistral model is [🤗Salesforce/SFR-Embedding-Mistral](https://huggingface.co/Salesforce/SFR-Embedding-Mistral). ```shell INFO 02-05 03:05:04 llm_engine.py:72] Initializing...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GPT2LMHeadMo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
