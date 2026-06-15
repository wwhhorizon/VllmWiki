# vllm-project/vllm#22961: [Bug]: TypeError: MoeWNA16Method.get_weight_loader.<locals>.moe_wna16_weight_loader() got an unexpected keyword argument 'return_sucess'

| 字段 | 值 |
| --- | --- |
| Issue | [#22961](https://github.com/vllm-project/vllm/issues/22961) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: MoeWNA16Method.get_weight_loader.<locals>.moe_wna16_weight_loader() got an unexpected keyword argument 'return_sucess'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug the code in vllm/model_executor/models/glm4_moe.py is: success = weight_loader(param, loaded_weight, name_mapped, shard_id=shard_id, expert_id=expert_id, return_success=True) But the define of moe_wna16_weight_loader is: def moe_wna16_weight_loader(param: torch.nn.Parameter, loaded_weight: torch.Tensor, weight_name: str, shard_id: str, expert_id: int): ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton bui...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ## Your current environment ### 🐛 Describe the bug the code in vllm/model_executor/models/glm4_moe.py is: success = weight_loader(param, loaded_weight, name_mapped, shard_id=shard_id, expert_id=expert_id, return_success...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t): ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: TypeError: MoeWNA16Method.get_weight_loader.<locals>.moe_wna16_weight_loader() got an unexpected keyword argument 'return_sucess' bug;stale ### Your current environment ### 🐛 Describe the bug the code in vllm/mod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 6_weight_loader() got an unexpected keyword argument 'return_sucess' bug;stale ### Your current environment ### 🐛 Describe the bug the code in vllm/model_executor/models/glm4_moe.py is: success = weight_loader(param, lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
