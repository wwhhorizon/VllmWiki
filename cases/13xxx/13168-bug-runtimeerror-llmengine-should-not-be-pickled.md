# vllm-project/vllm#13168: [Bug]: RuntimeError: LLMEngine should not be pickled!

| 字段 | 值 |
| --- | --- |
| Issue | [#13168](https://github.com/vllm-project/vllm/issues/13168) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: LLMEngine should not be pickled!

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python import re from datasets import load_dataset, Dataset from unsloth import FastLanguageModel, PatchFastRL, is_bfloat16_supported from trl import GRPOConfig, GRPOTrainer SYSTEM_PROMPT = """ Respond in the following format: ... ... """ XML_COT_FORMAT = """\ {reasoning} {answer} """ MAX_SEQ_LENGTH = 1024 LORA_RANK = 64 def extract_xml_answer(text: str) -> str: answer = text.split(" ")[-1] answer = answer.split(" ")[0] return answer.strip() def extract_hash_answer(text: str) -> str | None: if "####" not in text: return None return text.split("####")[1].strip() def get_gsm8k_questions(split="train") -> Dataset: data = load_dataset("openai/gsm8k", "main")[split] data = data.map( lambda x: { "prompt": [ {"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": x["question"]}, ], "answer": extract_hash_answer(x["answer"]), } ) return data # Reward functions remain the same... def correctness_reward_func(prompts, completions, answer, **kwargs) -> list[float]: responses = [completion[0]["content"] for completion in completions] q = prompts[0][-1]["content"] extracted_responses = [extract_xml_answer(r) for r in respo...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: : return None return text.split("####")[1].strip() def get_gsm8k_questions(split="train") -> Dataset: data = load_dataset("openai/gsm8k", "main")[split] data = data.map( lambda x: { "prompt": [ {"role": "system", "conte...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: om datasets import load_dataset, Dataset from unsloth import FastLanguageModel, PatchFastRL, is_bfloat16_supported from trl import GRPOConfig, GRPOTrainer SYSTEM_PROMPT = """ Respond in the following format: ... ... """...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ! bug ### Your current environment ### 🐛 Describe the bug ```python import re from datasets import load_dataset, Dataset from unsloth import FastLanguageModel, PatchFastRL, is_bfloat16_supported from trl import GRPOConf...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: _dataset, Dataset from unsloth import FastLanguageModel, PatchFastRL, is_bfloat16_supported from trl import GRPOConfig, GRPOTrainer SYSTEM_PROMPT = """ Respond in the following format: ... ... """ XML_COT_FORMAT = """\...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ta2=0.99, weight_decay=0.1, warmup_ratio=0.1, lr_scheduler_type="cosine", optim="adamw_8bit", logging_steps=1, bf16=is_bfloat16_supported(), fp16=not is_bfloat16_supported(), per_device_train_batch_size=1, gradient_accu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
