# vllm-project/vllm#10798: [Bug]: LoRa adapter responses not matching peft/transformers response

| 字段 | 值 |
| --- | --- |
| Issue | [#10798](https://github.com/vllm-project/vllm/issues/10798) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LoRa adapter responses not matching peft/transformers response

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Issue: LoRa adapter responses with vLLM do not match peft/transformer responses.** The reproduction involves running inference using a) vllm, compared to b) running inference with transformers and peft. I have run both on A40 machines on runpod. # vLLM approach ## vLLM server startup with statically loaded LoRa ``` ADAPTER_REPO="Trelis/Qwen2.5-7B-Instruct-touch-rugby-1" ADAPTER_PATH=$(python3 -c "from huggingface_hub import snapshot_download; print(snapshot_download('${ADAPTER_REPO}', ignore_patterns=['model-*', 'pytorch_model*', 'tf_model*', 'flax_model*']))") # Start server with LoRA pre-loaded vllm serve Qwen/Qwen2.5-7B-Instruct \ --max-model-len 8192 \ --enable-lora \ --max-lora-rank 8 \ --port 8000 \ --lora-modules "{\"name\": \"touch-rugby-1\", \"path\": \"${ADAPTER_PATH}\", \"base_model_name\": \"Qwen/Qwen2.5-7B-Instruct\"}" ``` ## vLLM Script to call the server endpoint, aka `vllm_replication.py` ``` import requests import json from typing import List, Dict, Any def send_chat_completion( messages: List[Dict[str, str]], model: str, base_url: str = "http://localhost:8000" ) -> Dict[str,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: -Instruct-touch-rugby-1" ADAPTER_PATH=$(python3 -c "from huggingface_hub import snapshot_download; print(snapshot_download('${ADAPTER_REPO}', ignore_patterns=['model-*', 'pytorch_model*', 'tf_model*', 'flax_model*']))")...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: hing peft/transformers response bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Issue: LoRa adapter responses with vLLM do not match peft/transformer responses.** The reprod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: del = AutoModelForCausalLM.from_pretrained( base_model_id, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True ) # Test prompt prompt = "How many players are on the field on each team at the start of a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Script to call the server endpoint, aka `vllm_replication.py` ``` import requests import json from typing import List, Dict, Any def send_chat_completion( messages: List[Dict[str, str]], model: str, base_url: str = "htt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: apter_response) # Free up memory del base_model del adapter_model torch.cuda.empty_cache() ``` # Results / Output ## vLLM > The adapter response does not take on the adapter/fine-tune attributes). It does not know what...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
