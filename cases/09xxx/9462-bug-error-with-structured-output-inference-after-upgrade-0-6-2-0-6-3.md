# vllm-project/vllm#9462: [Bug]: Error with structured output inference after upgrade 0.6.2->0.6.3

| 字段 | 值 |
| --- | --- |
| Issue | [#9462](https://github.com/vllm-project/vllm/issues/9462) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error with structured output inference after upgrade 0.6.2->0.6.3

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After upgrading from version 0.6.2 to 0.6.3 I started getting a validation error while generating structured input. To reproduce: 1. vllm serve NousResearch/Meta-Llama-3-8B-Instruct --dtype auto 2. Execute the following code. In my case, I do it from a Jupyter Notebook: ````{python} #### OUTPUT DEFINITION from pydantic import BaseModel, Field from enum import Enum from typing import List from typing import Optional import json from openai import OpenAI class BedType(Enum): Twin = "Twin" Double = "Double" Queen = "Queen" King = "King" class RoomBeds(BaseModel): bed_type: BedType = Field(...,description="Type of the bed in the hotel room") quantity: int = Field(...,description="Number of beds of the given bed type within the hotel room") class HotelRoom(BaseModel): """ Represents a hotel room. """ room_id: str = Field(...,description="Id of the room from the input") room_name: Optional[str] = Field(...,description="Freetext name of the hotel room") room_class: Optional[str] = Field(..., description="Room class of the hotel room.") bed_types: Optional[List[RoomBeds]] = Field(..., description="List...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Input Dumps _No response_ ### 🐛 Describe the bug After upgrading from version 0.6.2 to 0.6.3 I started getting a validation error while generating structured input. To reproduce: 1. vllm serve NousResearch/Meta-Llama-3-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: while generating structured input. To reproduce: 1. vllm serve NousResearch/Meta-Llama-3-8B-Instruct --dtype auto 2. Execute the following code. In my case, I do it from a Jupyter Notebook: ````{python} #### OUTPUT DEFI...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ->0.6.3 bug;structured-output;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After upgrading from version 0.6.2 to 0.6.3 I started getting a validation error while generati...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ctured output inference after upgrade 0.6.2->0.6.3 bug;structured-output;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After upgrading from version 0.6.2 to 0.6.3 I starte...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ut. To reproduce: 1. vllm serve NousResearch/Meta-Llama-3-8B-Instruct --dtype auto 2. Execute the following code. In my case, I do it from a Jupyter Notebook: ````{python} #### OUTPUT DEFINITION from pydantic import Bas...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
