# vllm-project/vllm#6977: [Bug]: Wrong image hallucination for InternVL2 model

| 字段 | 值 |
| --- | --- |
| Issue | [#6977](https://github.com/vllm-project/vllm/issues/6977) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Wrong image hallucination for InternVL2 model

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug - As reported in #6514, `InternVL2-26B`, `InternVL2-40B` and `InternVL2-76B` all have wrong image hallucination issue. We use this issue for tracking. - These problematic models all use [InternViT-6B-448px-V1-5](https://huggingface.co/OpenGVLab/InternViT-6B-448px-V1-5) as ViT, while models use [InternViT-300M-448px](https://huggingface.co/OpenGVLab/InternViT-300M-448px) don't have this issue. ### Reproduce Code ```python import os from openai import OpenAI client = OpenAI( api_key="EMPTY", base_url="http://localhost:8000/v1" ) stream = True chat_completion = client.chat.completions.create( model="OpenGVLab/InternVL2-40B", stream=stream, messages=[ { "role": "user", "content": [ { "type": "text", "text": "What's in this image?" }, { "type": "image_url", "image_url": { "url": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Llama%2C_peru%2C_machu_picchu.jpg", }, }, ], } ], extra_body={ "skip_special_tokens": False } ) ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Wrong image hallucination for InternVL2 model bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug - As reported in #6514, `InternVL2-26B`, `InternVL2-40B` and...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Wrong image hallucination for InternVL2 model bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug - As reported in #6514, `InternVL2-26B`, `InternVL2-40B` and...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ggingface.co/OpenGVLab/InternViT-300M-448px) don't have this issue. ### Reproduce Code ```python import os from openai import OpenAI client = OpenAI( api_key="EMPTY", base_url="http://localhost:8000/v1" ) stream = True...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ], } ], extra_body={ "skip_special_tokens": False } ) ```

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
