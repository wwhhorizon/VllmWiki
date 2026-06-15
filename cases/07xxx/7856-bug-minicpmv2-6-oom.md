# vllm-project/vllm#7856: [Bug]: minicpmv2_6 OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#7856](https://github.com/vllm-project/vllm/issues/7856) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;operator;quantization;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: minicpmv2_6 OOM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug my code: ```python def run_minicpmv(question): # 2.0 # The official repo doesn't work yet, so we need to use a fork for now # For more details, please see: See: https://github.com/vllm-project/vllm/pull/4087#issuecomment-2250397630 # noqa # model_name = "HwwwH/MiniCPM-V-2" # 2.5 # model_name = "openbmb/MiniCPM-Llama3-V-2_5" #2.6 model_name_or_path = "/home/hadoop-platcv/minicpm-v-v2_6/checkpoint-2709-merged" tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=True) llm = LLM( model=model_name_or_path, trust_remote_code=True, # quantization="fp8", # gpu_memory_utilization=0.5, enforce_eager=True, # swap_space=30, # cpu_offload_gb=30, ) # NOTE The stop_token_ids are different for various versions of MiniCPM-V # 2.0 # stop_token_ids = [tokenizer.eos_id] # 2.5 # stop_token_ids = [tokenizer.eos_id, tokenizer.eot_id] # 2.6 stop_tokens = [' ', ' '] stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens] messages = [{ 'role': 'user', 'content': f'( ./ )\n{question}' }] prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) return llm, prompt, stop_token_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: my code: ```python def run_minicpmv(question): # 2.0 # The official repo doesn't work yet, so we need to use a fork for now # For more details, please see: See: https://github.com/vllm-project/vllm/pull/4087#issuecommen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: hub.com/vllm-project/vllm/pull/4087#issuecomment-2250397630 # noqa # model_name = "HwwwH/MiniCPM-V-2" # 2.5 # model_name = "openbmb/MiniCPM-Llama3-V-2_5" #2.6 model_name_or_path = "/home/hadoop-platcv/minicpm-v-v2_6/che...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: model=model_name_or_path, trust_remote_code=True, # quantization="fp8", # gpu_memory_utilization=0.5, enforce_eager=True, # swap_space=30, # cpu_offload_gb=30, ) # NOTE The stop_token_ids are different for various versi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: minicpmv2_6 OOM bug ### Your current environment ### 🐛 Describe the bug my code: ```python def run_minicpmv(question): # 2.0 # The official repo doesn't work yet, so we need to use a fork for now # For more detai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m occurs OOM, details as follows: ```sh [rank0]: torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 16.00 GiB. GPU 0 has a total capacity of 44.32 GiB of which 15.81 GiB is free. Process 48868 has 28.50 GiB m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
