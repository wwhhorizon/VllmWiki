# vllm-project/vllm#12808: [Bug]: Embedding model with Lora doesn't work.

| 字段 | 值 |
| --- | --- |
| Issue | [#12808](https://github.com/vllm-project/vllm/issues/12808) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Embedding model with Lora doesn't work.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Embedding model API with Lora weights doesn't work as expected. For example, the transformer version is: ```python import torch from transformers import AutoModel, AutoTokenizer from peft import PeftModel, PeftConfig def get_model(peft_model_name): config = PeftConfig.from_pretrained(peft_model_name) base_model = AutoModel.from_pretrained(config.base_model_name_or_path) model = PeftModel.from_pretrained(base_model, peft_model_name) model = model.merge_and_unload() model.eval() return model # Load the tokenizer and model tokenizer = AutoTokenizer.from_pretrained('meta-llama/Llama-2-7b-hf') model = get_model('castorini/repllama-v1-7b-lora-passage') # Define query and passage inputs query = "What is llama?" title = "Llama" passage = "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era." query_input = tokenizer(f'query: {query} ', return_tensors='pt') passage_input = tokenizer(f'passage: {title} {passage} ', return_tensors='pt') # Run the model forward to compute embeddings and query-passage similarity score with torch.no_grad(): # compute query embe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ith Lora weights doesn't work as expected. For example, the transformer version is: ```python import torch from transformers import AutoModel, AutoTokenizer from peft import PeftModel, PeftConfig def get_model(peft_mode...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Embedding model with Lora doesn't work. bug ### Your current environment ### 🐛 Describe the bug Embedding model API with Lora weights doesn't work as expected. For example, the transformer version is: ```python i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: de. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: import LLM from huggingface_hub import snapshot_download from vllm.lora.request import LoRARequest from vllm.config import PoolerConfig lora_path = snapshot_download(repo_id="castorini/repllama-v1-7b-lora-passage") # Sa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e_model, peft_model_name) model = model.merge_and_unload() model.eval() return model # Load the tokenizer and model tokenizer = AutoTokenizer.from_pretrained('meta-llama/Llama-2-7b-hf') model = get_model('castorini/repl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
