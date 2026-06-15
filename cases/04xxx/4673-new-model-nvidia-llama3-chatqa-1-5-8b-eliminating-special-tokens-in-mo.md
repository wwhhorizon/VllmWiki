# vllm-project/vllm#4673: [New Model]: nvidia/Llama3-ChatQA-1.5-8B eliminating special tokens in model output

| 字段 | 值 |
| --- | --- |
| Issue | [#4673](https://github.com/vllm-project/vllm/issues/4673) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: nvidia/Llama3-ChatQA-1.5-8B eliminating special tokens in model output

### Issue 正文摘录

### The model to consider. https://huggingface.co/nvidia/Llama3-ChatQA-1.5-8B ### The closest model vllm already supports. Llama 3 8B and 70B ### What's your difficulty of supporting the model you want? Nvidia just released Q&A and RAG optimised versions of LLama3. The vLLM loads both the models successfully and output is generated. The huggingface model page gives specific instructions that needs to be followed during tokenization. This makes the vLLM output with special tokens. How to avoid this issue? I serve the model using ``` python -m vllm.entrypoints.openai.api_server --dtype auto --api-key token-abc123 --tensor-parallel-size 1 --enforce-eager --host 0.0.0.0 --port 8005 --model ./model_path ``` ``` #vLLM model class vLLM: def __init__(self, base_url, model_name): self.model_name = model_name self.base_url = base_url self.llm_client = OpenAI(base_url=self.base_url, api_key="token-abc123") self.system_prompt="System: This is a chat between a user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions based on the context. The assistant should also indicate when the answer cannot be found in the context." de...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: nvidia/Llama3-ChatQA-1.5-8B eliminating special tokens in model output new-model ### The model to consider. https://huggingface.co/nvidia/Llama3-ChatQA-1.5-8B ### The closest model vllm already supports. Ll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [New Model]: nvidia/Llama3-ChatQA-1.5-8B eliminating special tokens in model output new-model ### The model to consider. https://huggingface.co/nvidia/Llama3-ChatQA-1.5-8B ### The closest model vllm already supports. Ll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: serve the model using ``` python -m vllm.entrypoints.openai.api_server --dtype auto --api-key token-abc123 --tensor-parallel-size 1 --enforce-eager --host 0.0.0.0 --port 8005 --model ./model_path ``` ``` #vLLM model cla...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: get a clear answer: ``` tokenizer.decode(response, skip_special_tokens=False) Hello! How can I help you? tokenizer.decode(response, skip_special_tokens=True) Hello! How can I help you? ```
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: low the instructions on huggingface, I get a clear answer: ``` tokenizer.decode(response, skip_special_tokens=False) Hello! How can I help you? tokenizer.decode(response, skip_special_tokens=True) Hello! How can I help...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
