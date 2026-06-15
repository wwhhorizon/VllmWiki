# vllm-project/vllm#1670: [Bug] Misaligned output from ChatGLM2 compared to HuggingFace version

| 字段 | 值 |
| --- | --- |
| Issue | [#1670](https://github.com/vllm-project/vllm/issues/1670) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 | shape_align |
| Operator 关键词 | cuda |
| 症状 | mismatch;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Misaligned output from ChatGLM2 compared to HuggingFace version

### Issue 正文摘录

I am using vLLM to generate responses from ChatGLM2 models. However, I found sometimes vLLM does not output exactly the same as its original Huggingface version, especially when you are asking it some rarely-seen question and the sequence is long. Here is a test example. I am using the main branch of vLLM, torch 2.0.1, huggingface 4.35, cuda 12.2 and A100 GPUs. ```python PATH_TO_CHATGLM2_6B = "THUDM/chatglm2-6b" PATH_TO_CHATGLM2_6B = "chatglm2-6b" # if model repo are cloned or linked here def test_default(prompts): # from https://huggingface.co/THUDM/chatglm2-6b # Note that sample and histories are disabled from transformers import AutoTokenizer, AutoModel tokenizer = AutoTokenizer.from_pretrained( PATH_TO_CHATGLM2_6B, trust_remote_code=True ) model = ( AutoModel.from_pretrained(PATH_TO_CHATGLM2_6B, trust_remote_code=True) .half() .cuda() ) model = model.eval() for prompt in prompts: response, history = model.chat(tokenizer, prompt, do_sample=False, history=[]) print(repr(response)) def test_vllm(prompts): from vllm import LLM, SamplingParams llm = LLM( model=PATH_TO_CHATGLM2_6B, tokenizer=PATH_TO_CHATGLM2_6B, trust_remote_code=True, tensor_parallel_size=1, ) sampling_params = Sam...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug] Misaligned output from ChatGLM2 compared to HuggingFace version I am using vLLM to generate responses from ChatGLM2 models. However, I found sometimes vLLM does not output exactly the same as its original Huggingf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: le. I am using the main branch of vLLM, torch 2.0.1, huggingface 4.35, cuda 12.2 and A100 GPUs. ```python PATH_TO_CHATGLM2_6B = "THUDM/chatglm2-6b" PATH_TO_CHATGLM2_6B = "chatglm2-6b" # if model repo are cloned or linke...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug] Misaligned output from ChatGLM2 compared to HuggingFace version I am using vLLM to generate responses from ChatGLM2 models. However, I found sometimes vLLM does not output exactly the same as its original Huggingf...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: asking it some rarely-seen question and the sequence is long. Here is a test example. I am using the main branch of vLLM, torch 2.0.1, huggingface 4.35, cuda 12.2 and A100 GPUs. ```python PATH_TO_CHATGLM2_6B = "THUDM/ch...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 本可能存在兼容性问题，` correctness frontend_api;model_support;sampling_logits cuda mismatch;slowdown env_dependency I am using vLLM to generate responses from ChatGLM2 models. However, I found sometimes vLLM does not output exact...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
