# vllm-project/vllm#27171: [Bug]: Gemma3-4b-it + lora's QPS is very low

| 字段 | 值 |
| --- | --- |
| Issue | [#27171](https://github.com/vllm-project/vllm/issues/27171) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma3-4b-it + lora's QPS is very low

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using Gemma3-4b-it with LoRA for single-token generation and observe a significant QPS drop compared to the base model. In contrast, Llama3.1-8b-instruct with LoRA maintains normal QPS. QPS comparison (single instance): 1. Gemma3-4b-it: 253; 2. Gemma3-4b-it + LoRA: **53**; (Severe drop) 3. Llama3.1-8b-instruct: 202; 4. Llama3.1-8b-instruct + LoRA: 198 (Normal). The core script and code are as follows: ```shell MODEL_TYPE="llama" if [ "$MODEL_TYPE" = "llama" ]; then MODEL_PATH="llama31_8b_instruct/" LORA_MODULES="llama_3.1_8b_instruct_lora_adapter" MODEL_NAME="llama31_8b_instruct" LORA_NAME="llama31_8b_instruct_lora" DTYPE="float16" elif [ "$MODEL_TYPE" = "gemma" ]; then MODEL_PATH="gemma3_4b_it/" LORA_MODULES="gemma3_4b_it_lora_adapter" MODEL_NAME="gemma3_4b_it" LORA_NAME="gemma3_4b_it_lora" DTYPE="bfloat16" else echo "error'" exit 1 fi GPU_MEMORY_UTILIZATION=0.9 MAX_MODEL_LEN=4096 export CUDA_VISIBLE_DEVICES="0" python3 -m vllm.entrypoints.openai.api_server \ --port 37374 \ --dtype ${DTYPE} \ --load-format safetensors \ --gpu-memory-utilization 0.9 \ --disable-log-requests \ --enable-prefix-caching \ --enable-lora \ --max-lo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma3-4b-it + lora's QPS is very low bug ### Your current environment ### 🐛 Describe the bug I'm using Gemma3-4b-it with LoRA for single-token generation and observe a significant QPS drop compared to the base m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf dtype;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: _NAME="llama31_8b_instruct" LORA_NAME="llama31_8b_instruct_lora" DTYPE="float16" elif [ "$MODEL_TYPE" = "gemma" ]; then MODEL_PATH="gemma3_4b_it/" LORA_MODULES="gemma3_4b_it_lora_adapter" MODEL_NAME="gemma3_4b_it" LORA_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: or'" exit 1 fi GPU_MEMORY_UTILIZATION=0.9 MAX_MODEL_LEN=4096 export CUDA_VISIBLE_DEVICES="0" python3 -m vllm.entrypoints.openai.api_server \ --port 37374 \ --dtype ${DTYPE} \ --load-format safetensors \ --gpu-memory-uti...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
