# vllm-project/vllm#17169: [Bug]:  deepseek-v2-lite hangs during loading with tp=8; inference works with tp=2 using v1 engine, but both loading and inference succeed with v0 engine on H20

| 字段 | 值 |
| --- | --- |
| Issue | [#17169](https://github.com/vllm-project/vllm/issues/17169) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  deepseek-v2-lite hangs during loading with tp=8; inference works with tp=2 using v1 engine, but both loading and inference succeed with v0 engine on H20

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM import torch model = LLM(model="hf_models/DeepSeek-V2-Lite", trust_remote_code=True, dtype=torch.bfloat16, tensor_parallel_size=8, ) tokenizer = model.get_tokenizer() print(model) print(model.generate(tokenizer.apply_chat_template([{"role":"user","content":"Hello, how are you?"}], tokenize= False,add_generation_prompt=True))) ``` ``` INFO 04-25 07:45:43 [__init__.py:239] Automatically detected platform cuda. INFO 04-25 07:45:44 [config.py:209] Replacing legacy 'type' key with 'rope_type' INFO 04-25 07:45:50 [config.py:600] This model supports multiple tasks: {'generate', 'classify', 'embed', 'score', 'reward'}. Defaulting to 'generate'. INFO 04-25 07:45:51 [config.py:1600] Defaulting to use mp for distributed inference INFO 04-25 07:45:51 [config.py:1780] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 04-25 07:45:51 [cuda.py:160] Forcing kv cache block size to 64 for FlashMLA backend. INFO 04-25 07:45:55 [__init__.py:239] Automatically detected platform cuda. INFO 04-25 07:45:57 [core.py:61] Initializing a V1 LLM engine (v0.8.3) with config: model='hf_models/DeepSeek-V2-Lite', ski...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: current environment ### 🐛 Describe the bug ```python from vllm import LLM import torch model = LLM(model="hf_models/DeepSeek-V2-Lite", trust_remote_code=True, dtype=torch.bfloat16, tensor_parallel_size=8, )
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: epSeek-V2-Lite", trust_remote_code=True, dtype=torch.bfloat16, tensor_parallel_size=8, ) tokenizer = model.get_tokenizer() print(model) print(model.generate(tokenizer.apply_chat_template([{"role":"user","content":"H
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: scribe the bug ```python from vllm import LLM import torch model = LLM(model="hf_models/DeepSeek-V2-Lite", trust_remote_code=True, dtype=torch.bfloat16, tensor_parallel_size=8, ) tokenizer = model.get_tokenizer
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: p for distributed inference INFO 04-25 07:45:51 [config.py:1780] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 04-25 07:45:51 [cuda.py:160] Forcing kv cache block size to 64 for FlashMLA backend. INF...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ` INFO 04-25 07:45:43 [__init__.py:239] Automatically detected platform cuda. INFO 04-25 07:45:44 [config.py:209] Replacing legacy 'type' key with 'rope_type' INFO 04-25 07:45:50 [config.py:600] This model supports mult...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
