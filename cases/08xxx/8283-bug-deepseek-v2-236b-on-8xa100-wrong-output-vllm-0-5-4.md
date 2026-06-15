# vllm-project/vllm#8283: [Bug]: deepseek_v2 236B  on 8XA100 wrong output   vllm==0.5.4 

| 字段 | 值 |
| --- | --- |
| Issue | [#8283](https://github.com/vllm-project/vllm/issues/8283) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: deepseek_v2 236B  on 8XA100 wrong output   vllm==0.5.4 

### Issue 正文摘录

### Your current environment **wrong output** Prompt: 'Funniestjoke ever:',generated text: '!!!!!!!!!!!!!!!!!!' Prompt: The capital of France is:',generated text: '!!!!!!!!!!!!!!!!!!' Prompt: 'The future of AI is:',generated text: '!!!!!!!!!!!!!!!!!!' ### 🐛 Describe the bug from llvm import LLM, SamplingPatams import argpase import torch def generate(args, prompts): sampling_params = SamplingParams(temperature=0.8, top_k=1, max_tokens=20) llm = LLM(mode=args.model_path, trust_remote_code=True, max_model_len=2048,work_use_ray=True, enforce_eager=True, dtype=torch.half, tensor_parakkek_size=8, enable_chunked_prefill=False) outputs = llm.gennrate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.output[0].text print(f"prompt: {prompt!r} Generated text {generated_text!r}") if __name__ == "__main__"： parse = argparse.ArgumentParser() parse.add_argument('--model_path',type =str) prompts = [ "Funniestjoke ever:", "The capital of France is", "The future of AI is", ] generate(args, prompts) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of th...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: deepseek_v2 236B on 8XA100 wrong output vllm==0.5.4 bug ### Your current environment **wrong output** Prompt: 'Funniestjoke ever:',generated text: '!!!!!!!!!!!!!!!!!!' Prompt: The capital of France is:',generated...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ,generated text: '!!!!!!!!!!!!!!!!!!' ### 🐛 Describe the bug from llvm import LLM, SamplingPatams import argpase import torch def generate(args, prompts): sampling_params = SamplingParams(temperature=0.8, top_k=1, max_t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ote_code=True, max_model_len=2048,work_use_ray=True, enforce_eager=True, dtype=torch.half, tensor_parakkek_size=8, enable_chunked_prefill=False) outputs = llm.gennrate(prompts, sampling_params) for output in outputs: pr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: True, dtype=torch.half, tensor_parakkek_size=8, enable_chunked_prefill=False) outputs = llm.gennrate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.output[0].text print(f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: arams(temperature=0.8, top_k=1, max_tokens=20) llm = LLM(mode=args.model_path, trust_remote_code=True, max_model_len=2048,work_use_ray=True, enforce_eager=True, dtype=torch.half, tensor_parakkek_size=8, enable_chunked_p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
