# vllm-project/vllm#2836: how to create LLM() object given a model and a tokenizer?

| 字段 | 值 |
| --- | --- |
| Issue | [#2836](https://github.com/vllm-project/vllm/issues/2836) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> how to create LLM() object given a model and a tokenizer?

### Issue 正文摘录

Hello! I'm wondering if it's possible to load a `model` and a `tokenizer`, and then pass the two of them to `vllm.LLM()` to create an object. The reason I am trying to create the object this way (instead of using the model folder) is because my model is quantized by bitsandbytes and it seems vllm does not currently support bitsandbytes (i.e., when l run `vllm.LLM(model="path_to_model_repo", tokenizer="path_to_model_repo")`, I get the error message: `ValueError: Unknown quantization method: bitsandbytes. Must be one of ['awq', 'gptq', 'squeezellm'].`) Thus, I'm trying to load the model and tokenizer myself to create the vllm.LLM() object. I tried the following but it gives an error. ``` import vllm from transformers import AutoModelForCausalLM, AutoTokenizer import torch #load model and tokenizer model_repo = "path_to_model_repo" model = AutoModelForCausalLM.from_pretrained( model_name, use_safetensors=True, torch_dtype=torch.float16, device_map="auto", ) tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf") #create vllm.LLM() object client = vllm.LLM(model=model, tokenizer=tokenizer) Error message: Please provide either the path to a local folder or the repo_id of...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ject this way (instead of using the model folder) is because my model is quantized by bitsandbytes and it seems vllm does not currently support bitsandbytes (i.e., when l run `vllm.LLM(model="path_to_model_repo", tokeni...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: how to create LLM() object given a model and a tokenizer? Hello! I'm wondering if it's possible to load a `model` and a `tokenizer`, and then pass the two of them to `vllm.LLM()` to create an object. The reason I am try...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: the vllm.LLM() object. I tried the following but it gives an error. ``` import vllm from transformers import AutoModelForCausalLM, AutoTokenizer import torch #load model and tokenizer model_repo = "path_to_model_repo" m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
