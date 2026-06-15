# vllm-project/vllm#11761: [Bug]: After successfully loading the LoRA module with load_lora_adapter, the result returned by v1/models does not include this LoRA module.

| 字段 | 值 |
| --- | --- |
| Issue | [#11761](https://github.com/vllm-project/vllm/issues/11761) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: After successfully loading the LoRA module with load_lora_adapter, the result returned by v1/models does not include this LoRA module.

### Issue 正文摘录

### Your current environment ```text ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug After successfully loading the LoRA module with load_lora_adapter, the result returned by v1/models does not include this LoRA module. ``` # Deploy the base model. CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.openai.api_server \ --port=8010 \ --disable_log_stats \ --tensor-parallel-size=1 \ --served-model-name=Qwen/Qwen2.5-1.5B-Instruct \ --model=/pretrain_model_llm/qwen2.5/models--Qwen--Qwen2.5-1.5B-Instruct/snapshots/5fee7c4ed634dc66c6e318c8ac2897b8b9154536 \ --enable-lora # Load the LoRA module. curl --location 'http://localhost:8010/v1/load_lora_adapter' \ --header "Content-Type: application/json" \ --data '{ "lora_name": "fat_390", "lora_path": "/finetune_model_llm/sft/qwen2.5/fat_390" }' # return Success: LoRA adapter 'fat_390' added successfully. # Get the model list. curl -X 'GET' http://localhost:8010/v1/models # return {"object":"list","data":[{"id":"Qwen/Qwen2.5-1.5B-Instruct","object":"model","created":1736149337,"owned_by":"vllm","root":"/pretrain_model_llm/qwen2.5/models--Qwen--Qwen2.5-1.5B-Instruct/snapshots/5fee7c4ed634dc66c6e318c8ac2897b8b9154536","parent":null...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: /models does not include this LoRA module. ``` # Deploy the base model. CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.openai.api_server \ --port=8010 \ --disable_log_stats \ --tensor-parallel-size=1 \ --served-model...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: "object":"model_permission","created":1736149337,"allow_create_engine":false,"allow_sampling":true,"allow_logprobs":true,"allow_search_indices":false,"allow_view":true,"allow_fine_tuning":false,"organization":"*","group...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: oading the LoRA module with load_lora_adapter, the result returned by v1/models does not include this LoRA module. bug;stale ### Your current environment ```text ``` ### Model Input Dumps _No response_ ### 🐛 Describe th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: the result returned by v1/models does not include this LoRA module. bug;stale ### Your current environment ```text ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug After successfully loading the LoRA modul...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eet in a renowned area along the Río Seviça.That is the part of the Valencia city. It offers a unique blend of traditional Spanish life, art, and culture. Alternatively, if you like beaches, the city of Granada is a top...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
