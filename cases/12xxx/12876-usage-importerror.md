# vllm-project/vllm#12876: [Usage]: ImportError

| 字段 | 值 |
| --- | --- |
| Issue | [#12876](https://github.com/vllm-project/vllm/issues/12876) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: ImportError

### Issue 正文摘录

### Your current environment import PIL import os import argparse import random from transformers import AutoTokenizer from vllm import LLM, SamplingParams from vllm.assets.image import ImageAsset from vllm.assets.video import VideoAsset from vllm.utils import FlexibleArgumentParser def run_internvl(question: str, modality: str): assert modality == "image" parser = argparse.ArgumentParser() parser.add_argument("--model", type=str, required=True) args = parser.parse_args() llm = LLM( model=args.model, trust_remote_code=True, max_model_len=4096, # disable_mm_preprocessor_cache=args.disable_mm_preprocessor_cache, ) tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True) messages = [{'role': 'user', 'content': f" \n{question}"}] prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) # Stop tokens for InternVL # models variants may have different stop tokens # please refer to the model card for the correct "stop words": # https://huggingface.co/OpenGVLab/InternVL2-2B/blob/main/conversation.py stop_tokens = [" ", " ", " ", " "] stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens] return llm, prompt, stop_t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: import VideoAsset from vllm.utils import FlexibleArgumentParser def run_internvl(question: str, modality: str): assert modality == "image" parser = argparse.ArgumentParser() parser.add_argument("--model", type=str, requ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Usage]: ImportError usage ### Your current environment import PIL import os import argparse import random from transformers import AutoTokenizer from vllm import LLM, SamplingParams from vllm.assets.image import ImageA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e vllm ImportError: /usr/local/lib/python3.9/site-packages/flash_attn_2_cuda.cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops5zeros4callEN3c108ArrayRefINS2_6SymIntEEENS2_8optionalINS2_10ScalarTypeEEENS6_INS...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: template(messages, tokenize=False, add_generation_prompt=True) # Stop tokens for InternVL # models variants may have different stop tokens # please refer to the model card for the correct "stop
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
