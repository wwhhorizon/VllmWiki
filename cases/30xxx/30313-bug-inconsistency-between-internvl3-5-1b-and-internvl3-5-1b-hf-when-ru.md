# vllm-project/vllm#30313: [Bug]: Inconsistency between `InternVL3_5-1B` and `InternVL3_5-1B-HF` when running vLLM offline inference

| 字段 | 值 |
| --- | --- |
| Issue | [#30313](https://github.com/vllm-project/vllm/issues/30313) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Inconsistency between `InternVL3_5-1B` and `InternVL3_5-1B-HF` when running vLLM offline inference

### Issue 正文摘录

### Your current environment 1 ### 🐛 Describe the bug Hello! I encountered an inconsistency issue when using **vLLM** to perform **local offline inference** with the following two models: - `InternVL3_5-1B` - `InternVL3_5-1B-HF` ### ✔️ `InternVL3_5-1B` can run correctly ### ❌ `InternVL3_5-1B-HF` fails to generate correct results However, **LLaMA-Factory only supports finetuning `InternVL3_5-1B-HF`**, so I must rely on the HF version for downstream tasks — but currently it cannot perform correct inference under vLLM. ```python import os import time from PIL import Image from vllm import LLM, SamplingParams from transformers import AutoTokenizer import logging import warnings if __name__ == "__main__": image_folder = "/data/code/haobang.geng/code/vlm_imageanalysis/datasets/nsfw_datasets" batch_size = 16 # -------------------- 配置模型和 tokenizer -------------------- model_path = "/data/code/haobang.geng/models/InternVL3_5-1B" model_path = "/data/code/haobang.geng/models/InternVL3_5-1B-HF" tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True) # 问题模板 # questions = nsfw_rate_prompt = nsfw_rate_prompt = ["""你是一名图像内容分析助手，请根据图像内容判断其“黄色程度”，并严格按照优先级从高到低依次判断，最终输出对应等级。 # 请...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Inconsistency between `InternVL3_5-1B` and `InternVL3_5-1B-HF` when running vLLM offline inference bug;stale ### Your current environment 1 ### 🐛 Describe the bug Hello! I encountered an inconsistency issue when...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: only supports finetuning `InternVL3_5-1B-HF`**, so I must rely on the HF version for downstream tasks — but currently it cannot perform correct inference under vLLM. ```python import os import time from PIL import Image...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 模型 -------------------- llm = LLM( model=model_path, dtype="bfloat16", max_model_len=4096, gpu_memory_utilization=0.95, limit_mm_per_prompt={"image": 1, "video": 0}, trust_remote_code=True, mm_processor_kwargs={ "dynami...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: L3_5-1B` and `InternVL3_5-1B-HF` when running vLLM offline inference bug;stale ### Your current environment 1 ### 🐛 Describe the bug Hello! I encountered an inconsistency issue when using **vLLM** to perform **local off...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: jective, detailed, and accurate manner to facilitate the subsequent assessment of whether the image content violates regulations. """] placeholder = " " messages = [[{"role": "user", "content": f"{placeholder}\n{q}"}] f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
