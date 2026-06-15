# vllm-project/vllm#10442: [Bug]: Speculative decoding + guided decoding not working

| 字段 | 值 |
| --- | --- |
| Issue | [#10442](https://github.com/vllm-project/vllm/issues/10442) |
| 状态 | closed |
| 标签 | bug;structured-output;speculative-decoding;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Speculative decoding + guided decoding not working

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using speculative decoding plus guided decoding (outlines), the output is truncated to like 5 tokens on return. I am using ngram speculation and extracting company names from a document: ``` from pydantic import BaseModel, Field from typing import List, Optional from datetime import date class CompanyNameEntry(BaseModel): company_name: str #index: int #duration: str class CompanyNamesList(BaseModel): company_names: List[CompanyNameEntry] completion = client.chat.completions.create( model="model", messages=[ {"role": "user", "content": document_instruction} ], extra_body={ "guided_json": CompanyNamesList.schema(), } ) ``` It states here that this mode is supported. https://docs.vllm.ai/en/stable/serving/compatibility_matrix.html Can you please confirm this is not supported yet? Can you point me how to add this functionality ? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Speculative decoding + guided decoding not working bug;structured-output;speculative-decoding;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using speculative de
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ulation and extracting company names from a document: ``` from pydantic import BaseModel, Field from typing import List, Optional from datetime import date class CompanyNameEntry(BaseModel): company_name: str #index: in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: y ? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d-output;speculative-decoding;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using speculative decoding plus guided decoding (outlines), the output is truncated to lik...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
