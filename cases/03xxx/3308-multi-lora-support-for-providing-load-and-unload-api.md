# vllm-project/vllm#3308: Multi-LoRA - Support for providing /load and /unload API

| 字段 | 值 |
| --- | --- |
| Issue | [#3308](https://github.com/vllm-project/vllm/issues/3308) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Multi-LoRA - Support for providing /load and /unload API

### Issue 正文摘录

### Problem statement: In the production system, there should be an API to add\\\\remove fine-tuned weights dynamically. Inference caller should not have to specify LoRA location with each call. Current Multi-LoRA support allows adaptor load during inference calls, which doesn't check if finetune weights are already loaded and ready for inferencing. ### Proposal: Introduce an API - /load and /unload to allow fine-tuned weights inclusions in vllm. `POST /load` -> add finetunes weight as part of models. `POST /unload` -> remove finetunes weight from models list. This will allow the set of finetuned weights present in vllm server. This will infer no need to specify finetune weight names, and locations as part of each inference request. Sample code: ```python lora_request = None index = 1 @app.post("/load") async def load(request: Request) -> Response: request_dict = await request.json() global lora_request lora_local_path = request_dict.pop("lora_path", "/models/lora/") global index lora_request = LoRARequest( lora_name=lora_local_path, lora_int_id=index, lora_local_path=lora_local_path) index = index + 1 return Response(status_code=201) @app.post("/unload") async def unload(request:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e fine-tuned weights dynamically. Inference caller should not have to specify LoRA location with each call. Current Multi-LoRA support allows adaptor load during inference calls, which doesn't check if finetune weights...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: hts inclusions in vllm. `POST /load` -> add finetunes weight as part of models. `POST /unload` -> remove finetunes weight from models list. This will allow the set of finetuned weights present in vllm server. This will...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: o specify finetune weight names, and locations as part of each inference request. Sample code: ```python lora_request = None index = 1 @app.post("/load") async def load(request: Request) -> Response: request_dict = awai...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
