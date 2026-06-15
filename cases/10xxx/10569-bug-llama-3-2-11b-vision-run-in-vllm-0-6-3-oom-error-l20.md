# vllm-project/vllm#10569: [Bug]: llama-3.2-11B-vision run in vllm==0.6.3 OOM error（L20）

| 字段 | 值 |
| --- | --- |
| Issue | [#10569](https://github.com/vllm-project/vllm/issues/10569) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: llama-3.2-11B-vision run in vllm==0.6.3 OOM error（L20）

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug from PIL import Image from transformers import AutoTokenizer from vllm import LLM, SamplingParams from vllm.inputs import TokensPrompt import torch import torchvision.transforms as T from torchvision.transforms.functional import InterpolationMode from vllm.assets.image import ImageAsset import argparse parser = argparse.ArgumentParser() # from decord import VideoReader, cpu parser.add_argument('--batch_size', type=int, default=1) parser.add_argument('--input_len', type=int, default=128) parser.add_argument('--output_len', type=int, default=1024) args = parser.parse_args() model_name = "/home/dataset/Llama-3.2-11B-Vision-Instruct" llm = LLM( model=model_name, tensor_parallel_size=1, max_model_len=4096, trust_remote_code=True, enforce_eager=True ) sampling_params = SamplingParams(temperature=1, max_tokens=args.output_len,ignore_eos=True) tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True) query= 'Please describe the image in detail.' TEMPLATE = " User\n{prompt} \n Assistant\n" prompt = f" {query}\n" prompt = TEMPLATE.format(prompt=prompt) image = Image.open("3.png") inpu...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: llama-3.2-11B-vision run in vllm==0.6.3 OOM error（L20） bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug from PIL import Image from transformers import AutoTokenizer from
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### Model Input Dumps _No response_ ### 🐛 Describe the bug from PIL import Image from transformers import AutoTokenizer from vllm import LLM, SamplingParams from vllm.inputs import TokensPrompt import torch import torch...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory cuda;operator;quantization;triton build_error;crash;oom dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: xt) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: quantization;sampling_logits;scheduler_memory cuda;operator;quantization;triton build_error;crash;oom dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
