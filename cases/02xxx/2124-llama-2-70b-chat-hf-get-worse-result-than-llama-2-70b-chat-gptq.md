# vllm-project/vllm#2124: Llama-2-70b-chat-hf get worse result than Llama-2-70B-Chat-GPTQ

| 字段 | 值 |
| --- | --- |
| Issue | [#2124](https://github.com/vllm-project/vllm/issues/2124) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Llama-2-70b-chat-hf get worse result than Llama-2-70B-Chat-GPTQ

### Issue 正文摘录

I know this is not a problem related to vLLM. Maybe I use the wrong decode parameters. But I think people in vLLM community will give good advice for me. I have posted it in [transformers](https://github.com/huggingface/transformers/issues/28055), and I also post it here too. I am trying to use Llama-2-70b-chat-hf as zero-shot text classifier for my datasets. Here is my setups. 1. vLLM + Llama-2-70b-chat-hf I used vLLM as my inference engine as run it with: ``` python api_server.py --model /nas/lili/models_hf/70B-chat --tensor-parallel-size 8 ``` api_server.py is the [example file](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/api_server.py) and I do not modify anything. client code: ``` data = { "prompt": prompt, "use_beam_search": False, "n": 1, "temperature": 0.1, "max_tokens": 128, } res = _post(data) return eval(res.content)['text'][0].strip() ``` And my prompt is: ``` You will be provided with a product name. The product name will be delimited by 3 backticks, i.e.```. Classify the product into a primary category. Primary categories: Clothing, Shoes & Jewelry Automotive Home & Kitchen Beauty & Personal Care Electronics Sports & Outdoors Patio, Lawn & Garden...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Llama-2-70b-chat-hf get worse result than Llama-2-70B-Chat-GPTQ I know this is not a problem related to vLLM. Maybe I use the wrong decode parameters. But I think people in vLLM community will give good advice for me. I
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tgi. But I think it's easy for locating problem. ``` from transformers import LlamaTokenizer, LlamaForCausalLM tokenizer_path = "/nas/lili/models_hf/70B-chat-hf/" model_path = "/nas/lili/models_hf/70B-chat-hf/" tokenize...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: etrained( model_path, #load_in_8bit=True, #torch_dtype=torch.float16, device_map="auto", ) from flask import Flask, request, jsonify from flask_cors import CORS from transformers.generation import GenerationConfig app =...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ` data = { "prompt": prompt, "use_beam_search": False, "n": 1, "temperature": 0.1, "max_tokens": 128, } res = _post(data) return eval(res.content)['text'][0].strip() ``` And my prompt is: ``` You wil
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: GPTQ I know this is not a problem related to vLLM. Maybe I use the wrong decode parameters. But I think people in vLLM community will give good advice for me. I have posted it in [transformers](https://github.com/huggin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
