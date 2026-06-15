# vllm-project/vllm#2710: can vllm support loading lora?

| 字段 | 值 |
| --- | --- |
| Issue | [#2710](https://github.com/vllm-project/vllm/issues/2710) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> can vllm support loading lora?

### Issue 正文摘录

my code: ``` from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig from peft import PeftModel import torch from vllm import LLM, SamplingParams tokenizer = AutoTokenizer.from_pretrained("deepseek-coder-6.7b-instruct", trust_remote_code=True) sampling_params = SamplingParams( max_tokens=2048 ) model = LLM("deepseek-coder-6.7b-instruct", trust_remote_code=True, max_model_len=45120) lora_weights = "output-20240123/checkpoint-450" if lora_weights != "": print("loading lora") model = PeftModel.from_pretrained( model, lora_weights, torch_dtype=torch.float16, ) messages = [] while True: prefix = input("Input:") lines = open(prefix+".txt", "r").readlines() user_in = ''.join(lines).strip().replace("\n","").replace(" ","") message = {'role':'user', 'content': "{}".format(user_in)} messages.append(message) inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", tokenize=False) print("Question:\n{}".format(inputs)) # 32021 is the id of token outputs = model.generate([inputs], sampling_params) outputs = outputs[0].outputs[0].text.replace(inputs,"").strip() print("Response:\n{}".format(outputs)) message = {'role':'assistant', 'content': "{}".format(outputs...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: loading lora? my code: ``` from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig from peft import PeftModel import torch from vllm import LLM, SamplingParams tokenizer = AutoTokenizer.from_pretr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: odel.from_pretrained( model, lora_weights, torch_dtype=torch.float16, ) messages = [] while True: prefix = input("Input:") lines = open(prefix+".txt", "r").readlines() user_in = ''.join(lines).strip().replace("\n","").r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: can vllm support loading lora? my code: ``` from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig from peft import PeftModel import torch from vllm import LLM, SamplingParams tokenizer = AutoTok...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tokenizer.apply_chat_template(messages, return_tensors="pt", tokenize=False) print("Question:\n{}".format(inputs)) # 32021 is the id of token outputs = model.generate([inputs], sampling_params) outputs = outputs[0].outp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
