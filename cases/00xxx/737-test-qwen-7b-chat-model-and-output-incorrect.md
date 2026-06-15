# vllm-project/vllm#737: test qwen-7b-chat  model and  output  incorrect

| 字段 | 值 |
| --- | --- |
| Issue | [#737](https://github.com/vllm-project/vllm/issues/737) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> test qwen-7b-chat  model and  output  incorrect

### Issue 正文摘录

run script: python3 vllm/examples/offline_inference.py # changed model to qwen-7b-chat (download from huggingface on 2023.8.10) INFO 08-11 09:49:39 llm_engine.py:70] Initializing an LLM engine with config: model='model/', tokenizer='model/', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) WARNING 08-11 09:49:40 tokenizer.py:63] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. Prompt: 'Hello, my name is', Generated text: ' [Your Name] and I am excited to join the [Company Name] team' Prompt: 'The president of the United States is', Generated text: ' the head of state of the United States. \n A polygon with $' Prompt: 'The capital of France is', Generated text: ' Paris. It is located in the northern part of the country and is known for' Prompt: '你好', Generated text: 'nge\n 0.001*10^10=多少'

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: test qwen-7b-chat model and output incorrect run script: python3 vllm/examples/offline_inference.py # changed model to qwen-7b-chat (download from huggingface on 2023.8.10) INFO 08-11 09:49:39 llm_engine.py:70] Ini
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: odel/', tokenizer='model/', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) WARNING 08-11 09:49:40 toke...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: . Prompt: 'Hello, my name is', Generated text: ' [Your Name] and I am excited to join the [Company Name] team' Prompt: 'The president of the United States is', Generated text: ' the head of state of the United States. \...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e=auto, trust_remote_code=True, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) WARNING 08-11 09:49:40 tokenizer.py:63] Using a slow tokenizer. This...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: test qwen-7b-chat model and output incorrect run script: python3 vllm/examples/offline_inference.py # changed model to qwen-7b-chat (download from huggingface on 2023.8.10) INFO 08-11 09:49:39 llm_engine.py:70

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
