# vllm-project/vllm#13127: [Bug]: AttributeError: Qwen2Tokenizer has no attribute lower

| 字段 | 值 |
| --- | --- |
| Issue | [#13127](https://github.com/vllm-project/vllm/issues/13127) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: Qwen2Tokenizer has no attribute lower

### Issue 正文摘录

### Your current environment I downloaded models from modelscope, with transformers== 4.48.2 and vllm==0.7.1. ### 🐛 Describe the bug Got an AttributeError while calling AutoTokenizer.from_pretrained(model, use_fast=False)： ``` Traceback (most recent call last): File "/n/work3/jzhao/1_song/test.py", line 37, in outputs = get_completion(text, model, tokenizer=tokenizer, max_tokens=512, temperature=1, top_p=1, max_model_len=2048) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/n/work3/jzhao/1_song/test.py", line 14, in get_completion llm = LLM(model=model, tokenizer=tokenizer, max_model_len=max_model_len,trust_remote_code=True) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/n/work3/jzhao/miniconda3/envs/syj_llm/lib/python3.12/site-packages/vllm/utils.py", line 1039, in inner return fn(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^ File "/n/work3/jzhao/miniconda3/envs/syj_llm/lib/python3.12/site-packages/vllm/entrypoints/llm.py", line 240, in __init__ self.llm_engine = self.engine_class.from_engine_args( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/n/work3/jzhao/miniconda3/envs/sy...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: AttributeError: Qwen2Tokenizer has no attribute lower bug;stale ### Your current environment I downloaded models from modelscope, with transformers== 4.48.2 and vllm==0.7.1. ### 🐛 Describe the bug Got an Attribut...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 2Tokenizer has no attribute lower ``` Here's the script code： `from vllm import LLM, SamplingParams from transformers import AutoTokenizer import os import json os.environ['VLLM_USE_MODELSCOPE']='True' def get_completio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ")` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ibuteError while calling AutoTokenizer.from_pretrained(model, use_fast=False)： ``` Traceback (most recent call last): File "/n/work3/jzhao/1_song/test.py", line 37, in outputs = get_completion(text, model, tokenizer=tok...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: AttributeError: Qwen2Tokenizer has no attribute lower bug;stale ### Your current environment I downloaded models from modelscope, with transformers== 4.48.2 and vllm==0.7.1. ### 🐛 Describe the bug Got an Attribut...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
