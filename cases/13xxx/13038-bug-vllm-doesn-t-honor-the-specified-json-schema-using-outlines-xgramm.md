# vllm-project/vllm#13038: [Bug]: vllm doesn't honor the specified json schema using outlines/xgrammar with qwen 2.5 vl

| 字段 | 值 |
| --- | --- |
| Issue | [#13038](https://github.com/vllm-project/vllm/issues/13038) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm doesn't honor the specified json schema using outlines/xgrammar with qwen 2.5 vl

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have specified the following schema: ```python class UCC1(BaseModel): # FILING_NUMBER: str = Field(..., description='Filing Number that will be unique and single valued') # FILING_DATE: str = Field(..., description='Filing Date that will be unique and single valued. DO NOT include time, if present') # COLLATERAL_DESCRIPTION: Optional[str] = Field( # default_factory=str, description="The ENTIRE text describing the collateral" # ) SECURED_PARTY_DETAILS_SECURED_PARTY_NAME: List[str] = Field( default_factory=list, description="List names of the Secured Parties" ) SECURED_PARTY_DETAILS_ADDRESS: List[str] = Field( default_factory=list, description="List of addresses of the Secured Parties" ) SECURED_PARTY_DETAILS_COUNTRY: List[str] = Field( default_factory=list, description="List of countries of the Secured Parties" ) SECURED_PARTY_DETAILS_STATE: List[str] = Field( default_factory=list, description="List of states of the Secured Parties" ) SECURED_PARTY_DETAILS_CITY: List[str] = Field( default_factory=list, description="List of cities of the Secured Parties" ) SECURED_PARTY_DETAILS_ZIP: List[str] = Field( default_factory=list, descri...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: vllm doesn't honor the specified json schema using outlines/xgrammar with qwen 2.5 vl bug;stale ### Your current environment ### 🐛 Describe the bug I have specified the following schema: ```python class UCC1(Base...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: llm doesn't honor the specified json schema using outlines/xgrammar with qwen 2.5 vl bug;stale ### Your current environment ### 🐛 Describe the bug I have specified the following schema: ```python class UCC1(BaseModel):...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ors") ``` And I have tried using outlines and xgrammar as json decoding backend for Qwen 2.5 VL. This is the sample code I am using for offline inference ```python if PAGE_LABEL == "UCC1": keys_to_extract_str = ", ".joi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: r the specified json schema using outlines/xgrammar with qwen 2.5 vl bug;stale ### Your current environment ### 🐛 Describe the bug I have specified the following schema: ```python class UCC1(BaseModel): # FILING_NUMBER:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
