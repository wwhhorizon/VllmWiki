# vllm-project/vllm#14506: [Bug]: RuntimeError: Phi4MM cannot process x audios and ximages in a prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#14506](https://github.com/vllm-project/vllm/issues/14506) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Phi4MM cannot process x audios and ximages in a prompt

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While starting a vllm api server to use phi-4-multimodal-instruct, error will occur. But if I remove VLLM_USE_V1=1, it's okay. ```bash CUDA_VISIBLE_DEVICES=3,1,0,2 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ TRANSFORMERS_OFFLINE=1 \ HF_DATASETS_OFFLINE=1 \ VLLM_USE_V1=1 \ python -m vllm.entrypoints.openai.api_server --model /root/HuggingFaceCache/models--microsoft--Phi-4-multimodal-instruct --dtype auto --trust-remote-code --served-model-name gpt-4 --gpu-memory-utilization 0.98 --tensor-parallel-size 4 --max-model-len 131072 --max-seq-len-to-capture=131072 --enable-lora --max-lora-rank 320 --lora-extra-vocab-size 0 --limit-mm-per-prompt audio=1,image=1 --max-loras 2 --lora-modules speech=/root/HuggingFaceCache/models--microsoft--Phi-4-multimodal-instruct/speech-lora vision=/root/HuggingFaceCache/models--microsoft--Phi-4-multimodal-instruct/vision-lora --port 8000 --api-key sk-888888 --disable-sliding-window ``` ``` (VllmWorker rank=2 pid=18327) INFO 03-09 08:55:55 [gpu_model_runner.py:1114] Starting to load model /root/HuggingFaceCache/models--microsoft--Phi-4-multimodal-instruct... Loading safetensors checkpoint shards: 0% Completed...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ### 🐛 Describe the bug While starting a vllm api server to use phi-4-multimodal-instruct, error will occur. But if I remove VLLM_USE_V1=1, it's okay. ```bash CUDA_VISIBLE_DEVICES=3,1,0,2 \ VLLM_WORKER_MULTIPROC_METHOD=s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;gemm;operator;s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ct, error will occur. But if I remove VLLM_USE_V1=1, it's okay. ```bash CUDA_VISIBLE_DEVICES=3,1,0,2 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ TRANSFORMERS_OFFLINE=1 \ HF_DATASETS_OFFLINE=1 \ VLLM_USE_V1=1 \ python -m vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 15] Encoder cache will be initialized with a budget of 10000 tokens, and profiled with 1 audio items of the maximum feature size. (VllmWorker rank=0 pid=17825) INFO 03-09 08:55:58 [gpu_model_runner.py:1315] Encoder cach...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dal_vlm;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
