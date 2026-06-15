# vllm-project/vllm#22704: [Bug]: Using GPT-OSS with the streaming option degrades the quality of responses.

| 字段 | 值 |
| --- | --- |
| Issue | [#22704](https://github.com/vllm-project/vllm/issues/22704) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using GPT-OSS with the streaming option degrades the quality of responses.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I ran the code below to check the code quality of GPT-OSS. ```python from langchain_openai import ChatOpenAI from langchain_core.messages import AIMessage, HumanMessage MAX_TOKENS = 16384 api_url = "ENDPOINT_URL/v1" api_key = "-" model_name = "llm" reasoning_effort = "medium" # 'low', 'medium', or 'high' gpt_oss = ChatOpenAI( model_name=model_name, openai_api_base=api_url, reasoning_effort=reasoning_effort, openai_api_key='NONE', default_headers={"X-API-KEY": api_key}, temperature=1.0, max_tokens=MAX_TOKENS, # skip_special_tokens=False, extra_body={ "skip_special_tokens": False, }, streaming=True # streaming=False ) q = """ 아래 문제를 python으로 풀어서 실행 결과를 출력해줘. 입력 값은 input()함수를 사용하지 말고 test_data를 사용해. [문제] 소수의 정의는 1과 자기자신만으로 나누어 떨어지는 1보다 큰 양의 정수이다. 이를테면, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,,,,,,등은 모두 소수이며, 4(2x2), 6(2x3), 9(3x3),,,,등은 소수가 아닌 합성수이다. 두 수 A, B가 주어졌을 때, A 이상 B 이하의 소수의 개수를 출력하는 프로그램을 작성하시오. [제한조건] 1. 입력으로 주어지는 A, B는 1 이상 10,000 이하이다. 2. 1은 소수가 아님에 주의하시오. [입력] 맨 처음 테스트 케이스의 개수 T가 주어지며, 그 다음 줄부터 T 개의 테스트 케이스가 주어진다. 각 테스트 케이스는 한 줄로 구성되어 있으며, 두 수 A, B (1 ≤ A < B ≤ 10,000)가 주어진다. [출력] 각각의 테스트 케이스에 대하여 #x (x는 테스트 케이스 번호, 1부터...

## 现有链接修复摘要

#25719 [Bugfix] fixing streaming issues and tool call output for gpt-oss (#22704, #23335) | #25728 [Bugfix] fixing streaming issues and tool call output for gpt-oss (#22704)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: w to check the code quality of GPT-OSS. ```python from langchain_openai import ChatOpenAI from langchain_core.messages import AIMessage, HumanMessage MAX_TOKENS = 16384 api_url = "ENDPOINT_URL/v1" api_key = "-" model_na...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: Server pid=1) | File "/usr/local/lib/python3.12/dist-packages/anyio/_backends/_asyncio.py", line 772, in __aexit__ (APIServer pid=1) | raise BaseExceptionGroup( (APIServer pid=1) | ExceptionGroup: unhandled errors in a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: temperature=1.0, max_tokens=MAX_TOKENS, # skip_special_tokens=False, extra_body={ "skip_special_tokens": False, }, streaming=True # streaming=False ) q = """ 아래 문제를 python으로 풀어서 실행 결과를 출력해줘. 입력 값은 input()함수를 사용하지 말고 tes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: GPT-OSS with the streaming option degrades the quality of responses. bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug I ran the code below to check the code quality of GPT-OSS. ```python from langch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ontent pattern = r"```python(.*?)```" code_match = re.search(pattern, codes, re.DOTALL) if code_match: code_to_run = code_match.group(1).strip() exec(code_to_run) # run codes cnt += 1 else: print("No codes.")

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25719](https://github.com/vllm-project/vllm/pull/25719) | mentioned | 0.6 | [Bugfix] fixing streaming issues and tool call output for gpt-oss (#22704, #23335) | se Closely related to two bugs associated with streaming for gpt-oss (#22704, #23335): In `vllm/entrypoints/openai/serving_responses.py`, the stream loop was advancing the “curren… |
| [#25728](https://github.com/vllm-project/vllm/pull/25728) | mentioned | 0.6 | [Bugfix] fixing streaming issues and tool call output for gpt-oss (#22704) | y related to bugs associated with streaming for gpt-oss response API (#22704): Harmony’s streaming didn’t support `functions.*` tool calls at all. We handled reasoning on `analysi… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
