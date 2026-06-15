# vllm-project/vllm#12199: [Bug]: Dynamically load lora got wrong output

| 字段 | 值 |
| --- | --- |
| Issue | [#12199](https://github.com/vllm-project/vllm/issues/12199) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Dynamically load lora got wrong output

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am using the "Dynamically serving LoRA Adapters" function. After loading the new Lora, the inference result I got was wrong. Here are the steps I tested: 0. vLLM initial setting, Base model + Lora_1, Lora_2, Lora3 ``` # Start docker $ sudo docker run --runtime nvidia --gpus device=0 -v ~/.cache/huggingface:/root/.cache/huggingface -v /model:/mnt/adapters/ -p 8090:8090 --env "HUGGING_FACE_HUB_TOKEN=xxxxx" --env "VLLM_ALLOW_RUNTIME_LORA_UPDATING=True" -it --entrypoint /bin/bash vllm/vllm-openai ``` ``` # Run vLLM service in container root@45b50a8c64f3:/vllm-workspace# vllm serve meta-llama/Llama-3.1-8B-Instruct --dtype float16 --max-model-len 4000 --enable-lora --max_loras 3 --lora-module Lora_1=/mnt/adapters/Llama-3_1-DS-medical Lora_2=/mnt/adapters/Llama-3_1-DS-medical Lora_3=/mnt/adapters/Llama-3_1-DS-medical --gpu-memory-utilization 0.25 --port 8090 ``` 1. Test loras The results of the three lora inferences are all correct. From the vLLM log, the corresponding index of Lora Lora_1: lora_int_id=1, Lora_2: lora_int_id=2, Lora_3: lora_int_id=3 ``` # Inference by Lora_1 $ curl http://localhost:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 0. vLLM initial setting, Base model + Lora_1, Lora_2, Lora3 ``` # Start docker $ sudo docker run --runtime nvidia --gpus device=0 -v ~/.cache/huggingface:/root/.cache/huggingface -v /model:/mnt/adapters/ -p 8090:8090 --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ally load lora got wrong output bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am using the "Dynamically serving LoRA Adapters" function. After loading the new Lora, the in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 50a8c64f3:/vllm-workspace# vllm serve meta-llama/Llama-3.1-8B-Instruct --dtype float16 --max-model-len 4000 --enable-lora --max_loras 3 --lora-module Lora_1=/mnt/adapters/Llama-3_1-DS-medical Lora_2=/mnt/adapters/Llama-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;mismatch;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
