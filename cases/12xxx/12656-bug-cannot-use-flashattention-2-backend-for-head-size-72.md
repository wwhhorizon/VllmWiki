# vllm-project/vllm#12656: [Bug]: Cannot use FlashAttention-2 backend for head size 72.

| 字段 | 值 |
| --- | --- |
| Issue | [#12656](https://github.com/vllm-project/vllm/issues/12656) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot use FlashAttention-2 backend for head size 72.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python import os import gc from transformers import AutoTokenizer import os from PIL import Image from vllm import LLM import requests # os.environ["HF_HUB_OFFLINE"]="1" # openbmb/MiniCPM-V-2_6 modelName="openbmb/MiniCPM-V-2_6" llm = LLM(model=modelName,trust_remote_code=True,gpu_memory_utilization=0.9 ,dtype="float16", max_model_len=2048 ,max_num_seqs=2) tokenizer = AutoTokenizer.from_pretrained(modelName, trust_remote_code=True) import requests import torch from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor from vllm import LLM, SamplingParams from PIL import Image from io import BytesIO url="https://soujpg-images-1307121509.cos.ap-shanghai.myqcloud.com/souJpg/images/Xk4T5wbnb9eWp4qMS6iv4c.webp" # prompt=''' system # You are a helpful assistant. # user # 详细的描述这张图片 # assistant''' messages = [{ "role": "user", "content": # Number of images "( ./ )" + \ "\n详细描述这张图片内容" }] prompt = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) print(prompt) image=Image.open(BytesIO(requests.get(url).content)) stop_tokens = [' ', ' '] st...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ion-2 backend for head size 72. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python import os import gc from transformers import AutoTokenizer import os from PIL import...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Cannot use FlashAttention-2 backend for head size 72. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python import os import gc from transformers import AutoTokeniz...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python import os import gc from transformers import AutoTokenizer import os from PIL import Image from vllm import LLM import requests # os.environ["HF_HUB_O...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: M(model=modelName,trust_remote_code=True,gpu_memory_utilization=0.9 ,dtype="float16", max_model_len=2048 ,max_num_seqs=2) tokenizer = AutoTokenizer.from_pretrained(modelName, trust_remote_code=True) import requests impo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tputs[0].text print(generated_text) ``` INFO 02-02 03:40:39 cuda.py:235] Using Flash Attention backend. INFO 02-02 03:40:39 model_runner.py:1111] Starting to load model openbmb/MiniCPM-V-2_6... INFO 02-02 03:40:40 cuda....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
