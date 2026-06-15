# vllm-project/vllm#18572: [Bug]: ValueError: Attempted to assign 25 + 25 + 25 = 75 multimodal tokens to 147 placeholders

| 字段 | 值 |
| --- | --- |
| Issue | [#18572](https://github.com/vllm-project/vllm/issues/18572) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cache;cuda |
| 症状 | crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Attempted to assign 25 + 25 + 25 = 75 multimodal tokens to 147 placeholders

### Issue 正文摘录

### Your current environment vllm==0.7.3 transformers==4.49.0 ### 🐛 Describe the bug ```import os os.environ["HF_HOME"] = "/gz-data/.cache/huggingface" import torch from datasets import Dataset from qwen_vl_utils import process_vision_info from peft import LoraConfig, TaskType, get_peft_model, PeftModel from transformers import ( TrainingArguments, Trainer, DataCollatorForSeq2Seq, Qwen2_5_VLForConditionalGeneration, AutoProcessor, AutoTokenizer, TrainerCallback, TrainerControl, TrainerState, BitsAndBytesConfig ) import json import mlflow import os from transformers.integrations import HfDeepSpeedConfig import shutil from Levenshtein import ratio as levenshtein_ratio from vllm_grpo_trainer import Qwen2VLGRPOVLLMTrainer from trl import GRPOConfig from PIL import Image def process_func_for_grpo(example): conversation = example["conversations"] input_msg = conversation[0]["value"] output_msg = conversation[1]["value"] file_path = input_msg.split(" ")[1].split(" ")[0] img = Image.open(file_path).convert("RGB").resize((128, 128)) prompt = [ { "role": "user", "content": [ {"type": "image"}, {"type": "text", "text": "Is this image manipulated or synthesized?"} ] } ] return { "prompt": pro...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: ValueError: Attempted to assign 25 + 25 + 25 = 75 multimodal tokens to 147 placeholders bug;stale ### Your current environment vllm==0.7.3 transformers==4.49.0 ### 🐛 Describe the bug ```import os os.environ["HF_H...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ironment vllm==0.7.3 transformers==4.49.0 ### 🐛 Describe the bug ```import os os.environ["HF_HOME"] = "/gz-data/.cache/huggingface" import torch from datasets import Dataset from qwen_vl_utils import process_vision_info...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: f isinstance(model, str): model_id = model torch_dtype = model_init_kwargs.get("torch_dtype") if ( isinstance(torch_dtype, torch.dtype) or torch_dtype == "auto" or torch_dtype is None ):
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ed to assign 25 + 25 + 25 = 75 multimodal tokens to 147 placeholders bug;stale ### Your current environment vllm==0.7.3 transformers==4.49.0 ### 🐛 Describe the bug ```import os os.environ["HF_HOME"] = "/gz-data/.cache/h...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: train_dataset: Optional[Union[Dataset, IterableDataset]] = None, eval_dataset: Optional[ Union[Dataset, IterableDataset, dict[str, Union[Dataset, IterableDataset]]] ] = None, processing_class: Optional[PreTrainedTokeniz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
