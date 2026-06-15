# vllm-project/vllm#15219: [Usage]: : How to properly use vllm when serving - keyerror 'text'

| 字段 | 值 |
| --- | --- |
| Issue | [#15219](https://github.com/vllm-project/vllm/issues/15219) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: : How to properly use vllm when serving - keyerror 'text'

### Issue 正文摘录

### Your current environment I serve a model: ``` vllm serve google/gemma-3-4b-it \ --max-model-len 1024 \ --max-num-seqs 2 \ --dtype bfloat16 \ --device=cuda \ --trust-remote-code \ --quantization bitsandbytes \ --load-format bitsandbytes \ --gpu-memory-utilization 0.5 \ --host 0.0.0.0 \ --port 8080 ``` Now, I want to run a script which uses that model and streamlit for example. So , I am not sure which function I should call. If I call: ``` from llama_index.embeddings.huggingface import HuggingFaceEmbedding from llama_index.core import ( VectorStoreIndex, Document, Settings, PromptTemplate ) from llama_index.llms.vllm import VllmServer def load_llm(): return VllmServer( api_url="http://127.0.0.1:8080/v1", max_new_tokens=512, temperature=0.1 ) `````` ... ``` def inference_with_mixed_precision(query_engine, prompt): with autocast('cuda'): full_response = query_engine.query(prompt) return full_response def create_query_engine(docs, llm, embed_model): ... Settings.embed_model = embed_model index = VectorStoreIndex.from_documents(docs, show_progress=True) Settings.llm = llm query_engine = index.as_query_engine() ``` .... ``` llm = load_llm() embed_model = HuggingFaceEmbedding(model_n...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ng - keyerror 'text' usage;stale ### Your current environment I serve a model: ``` vllm serve google/gemma-3-4b-it \ --max-model-len 1024 \ --max-num-seqs 2 \ --dtype bfloat16 \ --device=cuda \ --trust-remote-code \ --q...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: \ --max-model-len 1024 \ --max-num-seqs 2 \ --dtype bfloat16 \ --device=cuda \ --trust-remote-code \ --quantization bitsandbytes \ --load-format bitsandbytes \ --gpu-memory-utilization 0.5 \ --host 0.0.0.0 \
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n I should call. If I call: ``` from llama_index.embeddings.huggingface import HuggingFaceEmbedding from llama_index.core import ( VectorStoreIndex, Document, Settings, PromptTemplate ) from llama_index.llms.vllm import...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --max-num-seqs 2 \ --dtype bfloat16 \ --device=cuda \ --trust-remote-code \ --quantization bitsandbytes \ --load-format bitsandbytes \ --gpu-memory-utilization 0.5 \ --host 0.0.0.0 \ --port 8080 ``` Now, I want
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: temperature=0.1 ) `````` ... ``` def inference_with_mixed_precision(query_engine, prompt): with autocast('cuda'): full_response = query_engine.query(prompt) return full_response def create_query_engine(docs, llm, embed_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
