# vllm-project/vllm#18791: [Bug]: something wrong with hermes tool parser

| 字段 | 值 |
| --- | --- |
| Issue | [#18791](https://github.com/vllm-project/vllm/issues/18791) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: something wrong with hermes tool parser

### Issue 正文摘录

### Your current environment ```text # here's my code # langchain=0.3.24 # fastmcp=2.4.0 # langchain-mcp-adapters=0.1.1 # mcp=1.9.0 client = MultiServerMCPClient(mcp_config) tool = await client.get_tools() llm = ChatOpenAI(base_url=self_dict['url'], model=self_dict['model_name'], api_key='anything', temperature=0.7, extra_body={"chat_template_kwargs": { "enable_thinking": False}}) system_message = '你是一个优秀的AI助手' prompt = ChatPromptTemplate.from_messages( [ ("system", system_message), ("human", "{user_input}"), ("placeholder", "{agent_scratchpad}"), ] ) agent = create_tool_calling_agent(llm, tools=tt_Tool_list, prompt=prompt) agent_executor = AgentExecutor( agent=agent, tools=tt_Tool_list, verbose=True, return_intermediate_steps=True, handle_parsing_errors=True ) ``` ### 🐛 Describe the bug ```text DEBUG 05-28 02:39:59 [hermes_tool_parser.py:128] delta_token_ids: [35946] DEBUG 05-28 02:39:59 [hermes_tool_parser.py:131] No tool call tokens found! DEBUG 05-28 02:39:59 [hermes_tool_parser.py:127] delta_text: 意识到 DEBUG 05-28 02:39:59 [hermes_tool_parser.py:128] delta_token_ids: [106079] DEBUG 05-28 02:39:59 [hermes_tool_parser.py:131] No tool call tokens found! DEBUG 05-28 02:39:59 [herm...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: something wrong with hermes tool parser bug;stale ### Your current environment ```text # here's my code # langchain=0.3.24 # fastmcp=2.4.0 # langchain-mcp-adapters=0.1.1 # mcp=1.9.0 client = MultiServerMCPClient(...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tokens=31869, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: None,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ngchain-mcp-adapters=0.1.1 # mcp=1.9.0 client = MultiServerMCPClient(mcp_config) tool = await client.get_tools() llm = ChatOpenAI(base_url=self_dict['url'], model=self_dict['model_name'], api_key='anything', temperature...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
