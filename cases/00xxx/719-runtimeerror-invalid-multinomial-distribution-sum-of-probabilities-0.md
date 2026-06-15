# vllm-project/vllm#719: RuntimeError: invalid multinomial distribution (sum of probabilities <= 0)

| 字段 | 值 |
| --- | --- |
| Issue | [#719](https://github.com/vllm-project/vllm/issues/719) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError: invalid multinomial distribution (sum of probabilities <= 0)

### Issue 正文摘录

Hello, I am using python 3.9 with cuda 11.8 on aws with machine ml.g5.12xlarge (4 gpus A10) here's my requirements.txt: `einops torch==2.0.1 bitsandbytes==0.39.0 pandas==1.5.3 deepspeed==0.10.0 git+https://github.com/huggingface/accelerate git+https://github.com/huggingface/peft git+https://github.com/huggingface/transformers scipy xformers >= 0.0.19 langdetect numpy fastapi uvicorn ninja # For faster builds. psutil ray >= 2.5.1 vllm==0.1.3 sentencepiece # Required for LLaMA tokenizer. huggingface-hub==0.16.4` The code is: from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.1, top_p=0.75),top_k=0.4, frequency_penalty=1.17) llm = LLM(model=model_name, tensor_parallel_size=4 ) `text = ' [INST] What is your name? [/INST]'` outputs = model.generate([text], sampling_params) ``` outputs_dict = {} # Print the outputs. for idx, output in enumerate(outputs): prompt = output.prompt generated_text = output.outputs[0].text outputs_dict[f'text_{idx}']=generated_text ``` getting error: RuntimeError: invalid multinomial distribution (sum of probabilities <= 0) I guess it is because of the calculations of top_k? Thanks

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ub.com/huggingface/peft git+https://github.com/huggingface/transformers scipy xformers >= 0.0.19 langdetect numpy fastapi uvicorn ninja # For faster builds. psutil ray >= 2.5.1 vllm==0.1.3 sentencepiece # Required for L...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: sandbytes==0.39.0 pandas==1.5.3 deepspeed==0.10.0 git+https://github.com/huggingface/accelerate git+https://github.com/huggingface/peft git+https://github.com/huggingface/transformers scipy xformers >= 0.0.19 langdetect...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tribution (sum of probabilities <= 0) Hello, I am using python 3.9 with cuda 11.8 on aws with machine ml.g5.12xlarge (4 gpus A10) here's my requirements.txt: `einops torch==2.0.1 bitsandbytes==0.39.0 pandas==1.5.3 deeps...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
