# vllm-project/vllm#4297: [New Model]: Llama 3 8B Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#4297](https://github.com/vllm-project/vllm/issues/4297) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Llama 3 8B Instruct

### Issue 正文摘录

### The model to consider. https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct ### The closest model vllm already supports. LLama 1 & 2 ### What's your difficulty of supporting the model you want? LLama 3 instruct requires a different stop token than is specified in the `tokenizer.json` file. The `tokenizer.json` specifies ` ` as the end of string token which works for the base LLama 3 model, but this is not the right token for the instruct tune. The instruct tune uses ` `. You can see this in the inference code for the model on the [llama 3 8B instruct model card](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct), where this token is added: ```python import transformers import torch model_id = "meta-llama/Meta-Llama-3-8B-Instruct" pipeline = transformers.pipeline( "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto", ) messages = [ {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"}, {"role": "user", "content": "Who are you?"}, ] prompt = pipeline.tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) # HERE is where they add the ` ` token, whic...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ine( "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto", ) messages = [ {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"}, {"r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Llama 3 8B Instruct new-model ### The model to consider. https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct ### The closest model vllm already supports. LLama 1 & 2 ### What's your difficulty of sup...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: l you want? LLama 3 instruct requires a different stop token than is specified in the `tokenizer.json` file. The `tokenizer.json` specifies ` ` as the end of string token which works for the base LLama 3 model, but this...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ine.tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) # HERE is where they add the ` ` token, which is not the default end of string token, to the list of terminators. terminators = [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
