# vllm-project/vllm#10219: [Usage]: Using ThreadPoolExecutor for requests, possible degradation of the output

| 字段 | 值 |
| --- | --- |
| Issue | [#10219](https://github.com/vllm-project/vllm/issues/10219) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Using ThreadPoolExecutor for requests, possible degradation of the output

### Issue 正文摘录

### Your current environment ```text vllm-openai:v0.6.1.post2 Docker image ``` ### How would you like to use vllm Hi, first, thank you for making this great library available for everyone and working actively on it!! I am utilizing OpenAI compatible server functionality and combining with [instructor](https://github.com/instructor-ai/instructor) library, I am able to get structured outputs. When I was running this for excel documents with ```python import instructor from openai import OpenAI from pydantic import Field, BaseModel from constants import PHI_MOE_ENDPOINT, PHI_MOE_MODEL system_prompt = """ As an expert data analyst, your task is to generate a concise summary or description of \ the content within user-provided context. Your summary should capture the essence of the data, highlighting key points and trends \ while maintaining the original context. For any tables encountered, provide a brief description in markdown format to \ facilitate easy comprehension. """ class Description(BaseModel): description: str = Field( ..., description="Contains contextual information about the input" " to summarize its content for semantic and keyword retrieval.", ) def get_summary_from_do...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: age;stale ### Your current environment ```text vllm-openai:v0.6.1.post2 Docker image ``` ### How would you like to use vllm Hi, first, thank you for making this great library available for everyone and working actively...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ort instructor from openai import OpenAI from pydantic import Field, BaseModel from constants import PHI_MOE_ENDPOINT, PHI_MOE_MODEL system_prompt = """ As an expert data analyst, your task is to generate a concise summ...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: t OpenAI from pydantic import Field, BaseModel from constants import PHI_MOE_ENDPOINT, PHI_MOE_MODEL system_prompt = """ As an expert data analyst, your task is to generate a concise summary or description of \ the cont...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Using ThreadPoolExecutor for requests, possible degradation of the output usage;stale ### Your current environment ```text vllm-openai:v0.6.1.post2 Docker image ``` ### How would you like to use vllm Hi, first,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: " to summarize its content for semantic and keyword retrieval.", ) def get_summary_from_document(client, context, index=None): # function gets client as an argument, this is just to show what it would be # client = Open...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
