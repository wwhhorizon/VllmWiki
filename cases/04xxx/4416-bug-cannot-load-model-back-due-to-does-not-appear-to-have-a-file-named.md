# vllm-project/vllm#4416: [Bug]: cannot load model back due to [does not appear to have a file named config.json]

| 字段 | 值 |
| --- | --- |
| Issue | [#4416](https://github.com/vllm-project/vllm/issues/4416) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: cannot load model back due to [does not appear to have a file named config.json]

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug hi there, > vllm version: 0.4.1 I fine-tuned the mistral-7b-v0.2 model using the trainer of huggingface https://huggingface.co/docs/trl/v0.8.6/trainer the training worked well and finally it saved the model, as bellow: path_to_the_model: > adapter_config.json > adapter_model.safetensors > checkpoint-16 > checkpoint-24 > checkpoint-8 > README.md > special_tokens_map.json > tokenizer_config.json > tokenizer.json > tokenizer.model > training_args.bin it can successfully be loaded back using `AutoModelForCausalLM.from_pretrained` However, when I try to load it back via vllm, it caused error: > does not appear to have a file named config.json The vllm codes: ``` from langchain_community.llms import VLLM llm = VLLM(model="path_to_the_model", trust_remote_code=True, # mandatory for hf models max_new_tokens=64, temperature=0, # tensor_parallel_size=... # for distributed inference ) ``` ``` from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest llm = LLM(model="path_to_the_model", enable_lora=True) ``` neither works. any solutions ?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: cannot load model back due to [does not appear to have a file named config.json] bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug hi there, > vllm ve...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: f `python collect_env.py` ``` ### 🐛 Describe the bug hi there, > vllm version: 0.4.1 I fine-tuned the mistral-7b-v0.2 model using the trainer of huggingface https://huggingface.co/docs/trl/v0.8.6/trainer the training wo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: model back due to [does not appear to have a file named config.json] bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug hi there, > vllm version: 0.4.1 I fine...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
