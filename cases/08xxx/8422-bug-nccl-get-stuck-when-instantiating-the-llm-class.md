# vllm-project/vllm#8422: [Bug]: NCCL get stuck when instantiating the LLM class.

| 字段 | 值 |
| --- | --- |
| Issue | [#8422](https://github.com/vllm-project/vllm/issues/8422) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NCCL get stuck when instantiating the LLM class.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug NCCL get stuck when instantiating the LLM class. I can't even `CTRL + C` to stop it. I open all the debug log but I don't know what to do then. ``` from vllm import LLM def init_model() -> LLM: llm = LLM( model="Qwen/Qwen2-7B-Instruct", tokenizer_mode="auto", trust_remote_code=True, download_dir="./.cache", tensor_parallel_size=2, # How many GPUs to use gpu_memory_utilization=0.85, pipeline_parallel_size=1, dtype="bfloat16", # max_model_len=20480, # Model context length enable_prefix_caching=True, enable_chunked_prefill=False, num_scheduler_steps=8, ) return llm if __name__ == "__main__": llm = init_model() print(llm.generate("Hello, world!")) ``` ``` % ~/anaconda3/envs/psp/bin/python ~/psp/Reasoning-Carefully/main.py 2024-09-13 00:35:48 - INFO - main - The save_path is: ./results/Qwen2-7B/MATH/test/planthensteprefinewoinfo/0913 2024-09-13 00:35:48 - INFO - main - Global variables have been initialized 2024-09-13 00:35:48 - INFO - main - Start logging to huggingface Token is valid (permission: read). Your token has been saved in your configured git credential helpers (store). Your token has bee...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: tantiating the LLM class. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug NCCL get stuck when instantiating the LLM class. I can't even `CTRL + C` to stop it. I open all...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: I open all the debug log but I don't know what to do then. ``` from vllm import LLM def init_model() -> LLM: llm = LLM( model="Qwen/Qwen2-7B-Instruct", tokenizer_mode="auto", trust_remote_code=True, download_dir="./.cac...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: NCCL get stuck when instantiating the LLM class. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug NCCL get stuck when instantiating the LLM class. I can't even `CT...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: gpu_memory_utilization=0.85, pipeline_parallel_size=1, dtype="bfloat16", # max_model_len=20480, # Model context length enable_prefix_caching=True, enable_chunked_prefill=False, num_scheduler_steps=8, ) return llm if __n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: del config Qwen2Config { "_name_or_path": "Qwen/Qwen2-7B-Instruct", "architectures": [ "Qwen2ForCausalLM" ], "attention_dropout": 0.0, "bos_token_id": 151643, "eos_token_id": 151645, "hidden_act": "silu", "hidden_size":...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
