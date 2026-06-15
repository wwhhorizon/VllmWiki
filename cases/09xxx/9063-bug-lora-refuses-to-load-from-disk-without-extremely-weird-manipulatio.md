# vllm-project/vllm#9063: [Bug]: Lora refuses to load from disk without extremely weird manipulations with file paths

| 字段 | 值 |
| --- | --- |
| Issue | [#9063](https://github.com/vllm-project/vllm/issues/9063) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Lora refuses to load from disk without extremely weird manipulations with file paths

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug So, for me to load lora from disk you need to load it 4 times for some reason. This is clean env and vLLM installed from source. First I tested lora with fp8 and found that bug, but later I reproduced it with other model I can load without quantization. And in general it looks like loading issue first. I did all testing in jupyter notebook, but I can confirm that it works the same way in usual python, I managed to do the same loading process with 4 lora requests inside for loop with `try/except` and on 4th try it loaded correctly. Reproducing steps. First we load and prepare prompt/parameters, verify that model loaded correctly. ```python from pathlib import Path from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest from transformers import AutoTokenizer llm_path = Path("/media/data/username/models/vicuna-7b-v1.5") llm = LLM(model=llm_path, max_model_len=500, enable_lora=True, tokenizer_mode='slow') tokenizer = AutoTokenizer.from_pretrained(llm_path, use_fast=False) terminators = [tokenizer.eos_token_id] sampling_params = SamplingParams( min_tokens=5, max_tokens=30, top...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: you need to load it 4 times for some reason. This is clean env and vLLM installed from source. First I tested lora with fp8 and found that bug, but later I reproduced it with other model I can load without quantization....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: pulations with file paths bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug So, for me to load lora from disk you need to load it 4 times for some reason. This is clean en...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: load from disk without extremely weird manipulations with file paths bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug So, for me to load lora from disk you need to load i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: is is clean env and vLLM installed from source. First I tested lora with fp8 and found that bug, but later I reproduced it with other model I can load without quantization. And in general it looks like loading issue fir...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
