# vllm-project/vllm#615: Llama2 answers is noise

| 字段 | 值 |
| --- | --- |
| Issue | [#615](https://github.com/vllm-project/vllm/issues/615) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Llama2 answers is noise

### Issue 正文摘录

I tried to use Llama2, code is executing but the results are random character, what is wrong? ``` llm = LLM(model="/home/gpt/.cache/huggingface/hub/models--meta-llama--Llama-2-13b-hf/snapshots/bff3f0e93147eb2c18aa8a888e73f010d8935d17") prompts = [ "I am so fast that I can", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` and got ``` Prompt: 'I am so fast that I can', Generated text: 'hd canciónbólści Zum framідnexProgram nov напskieWrapperabi go totale' Prompt: 'The capital of France is', Generated text: 'Business Stock vieerves beskrevsiska}$. програкли laugh ","readerattednexшње савезној' Prompt: 'The future of AI is', Generated text: "pleasure Mohрю Democratic Pel.»)}{ Foi Referencias maven Yeah beyond encryption river Catalunya '" ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Llama2 answers is noise bug I tried to use Llama2, code is executing but the results are random character, what is wrong? ``` llm = LLM(model="/home/gpt/.cache/huggingface/hub/models--meta-llama--Llama-2-13b-hf/snapshots
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and got ``` Prompt: 'I am so fast that I can', Generated text: 'hd canciónbólści Zum framідnexProgram nov напskieWrapperabi go totale' Prompt: 'The capital of France is', Generated text: 'Business Stock vieerves beskrev...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
