# vllm-project/vllm#34099: [Usage]: VLLM with finetuned unsloth ministral 3

| 字段 | 值 |
| --- | --- |
| Issue | [#34099](https://github.com/vllm-project/vllm/issues/34099) |
| 状态 | open |
| 标签 | usage |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: VLLM with finetuned unsloth ministral 3

### Issue 正文摘录

### Your current environment - Using the VLLM docker vllm/vllm-openai:latest running on Runpod with RTX A6000 instance ### Problem Hi everyone, i have successfully trained a ministral 3 model and now i want to deploy it to VLLM but have faced many challenges. I have used the following command to serve vllm: ``` vllm serve --host 0.0.0.0 --port 8000 --model REPO_ID --dtype bfloat16 --enforce-eager --gpu-memory-utilization 0.95 --api-key API_KEY --max-model-len 8128 --tokenizer_mode mistral --config_format mistral --load_format mistral --enable-auto-tool-choice --tool-call-parser mistral ``` It works normally with https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 but for the finetuned model from this guide, it not works and missing many necessary files like the params.json, ... https://unsloth.ai/docs/models/tutorials/ministral-3#fine-tuning I have tried to manually fill in the missing files but got this error: "[0;36m(APIServer pid=19)[0;0m ValueError: No valid tokenizer file found in the repo REPO_ID" even the repo got the necessary tokenizer.json and tokenizer_config.json. I want to ask about is there anything special related to mistral deployment for VLLM? ### Bef...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ance ### Problem Hi everyone, i have successfully trained a ministral 3 model and now i want to deploy it to VLLM but have faced many challenges. I have used the following command to serve vllm: ``` vllm serve --host 0....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: serve vllm: ``` vllm serve --host 0.0.0.0 --port 8000 --model REPO_ID --dtype bfloat16 --enforce-eager --gpu-memory-utilization 0.95 --api-key API_KEY --max-model-len 8128 --tokenizer_mode mistral --config_format mistra...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: unsloth ministral 3 usage ### Your current environment - Using the VLLM docker vllm/vllm-openai:latest running on Runpod with RTX A6000 instance ### Problem Hi everyone, i have successfully trained a ministral 3 model a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: - Using the VLLM docker vllm/vllm-openai:latest running on Runpod with RTX A6000 instance ### Problem Hi everyone, i have successfully trained a ministral 3 model and now i want to deploy it to VLLM but have faced many...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Usage]: VLLM with finetuned unsloth ministral 3 usage ### Your current environment - Using the VLLM docker vllm/vllm-openai:latest running on Runpod with RTX A6000 instance ### Problem Hi everyone, i have successfully...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
