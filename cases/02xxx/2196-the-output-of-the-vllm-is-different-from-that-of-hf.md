# vllm-project/vllm#2196: the output of the vLLM is different from that of HF

| 字段 | 值 |
| --- | --- |
| Issue | [#2196](https://github.com/vllm-project/vllm/issues/2196) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> the output of the vLLM is different from that of HF

### Issue 正文摘录

Thank you very much for your outstanding work！When trying to use the internlm model, I found that the features obtained by vLLM forward for the first time are different from those obtained by HF for the same input. I want to ask why this is, is it caused by the inconsistency of the underlying implementation architecture Here are some of the configurations for the experiment： Environment ``` cuda==11.8 python==3.9 torch==2.1.0+cu118 xformers==0.0.22.post7+cu118 transformers==4.35.0 graphics_card：V100 ``` The code used to test the results ``` vLLM code： from vllm import LLM, SamplingParams prompts = ['请介绍下爱因斯坦的生平。'] sampling_params = SamplingParams( temperature=0, top_p=1, max_tokens=128, repetition_penalty=1.1, use_beam_search=True, best_of=5) llm = LLM(model="internlm/internlm-7b", trust_remote_code=True) outputs = llm.generate(prompts, sampling_params, use_tqdm=False) Huggingface code： import torch from transformers import AutoTokenizer, AutoModelForCausalLM tokenizer = AutoTokenizer.from_pretrained("internlm/internlm-7b", trust_remote_code=True) model = AutoModelForCausalLM.from_pretrained("internlm/internlm-7b", torch_dtype=torch.float16, trust_remote_code=True).cuda() model =...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: the output of the vLLM is different from that of HF stale Thank you very much for your outstanding work！When trying to use the internlm model, I found that the features obtained by vLLM forward for the first time are di...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ard：V100 ``` The code used to test the results ``` vLLM code： from vllm import LLM, SamplingParams prompts = ['请介绍下爱因斯坦的生平。'] sampling_params = SamplingParams( temperature=0, top_p=1, max_tokens=128, repetition_penalty=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: del = AutoModelForCausalLM.from_pretrained("internlm/internlm-7b", torch_dtype=torch.float16, trust_remote_code=True).cuda() model = model.eval() prompts = ['请介绍下爱因斯坦的生平。'] for prompt in prompts: inputs = tokenizer([pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s is, is it caused by the inconsistency of the underlying implementation architecture Here are some of the configurations for the experiment： Environment ``` cuda==11.8 python==3.9 torch==2.1.0+cu118 xformers==0.0.22.po...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: the output of the vLLM is different from that of HF stale Thank you very much for your outstanding work！When trying to use the internlm model, I found that the features obtained by vLLM forward for the first time are di...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
