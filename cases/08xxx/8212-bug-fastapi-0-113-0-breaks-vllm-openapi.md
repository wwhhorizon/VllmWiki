# vllm-project/vllm#8212: [Bug]: FastAPI 0.113.0 breaks vLLM OpenAPI

| 字段 | 值 |
| --- | --- |
| Issue | [#8212](https://github.com/vllm-project/vllm/issues/8212) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FastAPI 0.113.0 breaks vLLM OpenAPI

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug FastAPI [released 0.113.0 about 5 hours ago](https://github.com/fastapi/fastapi/releases). This release has a major refactor of Pydantic support. It appears this causes a Pydantic failure with the OpenAI-API calling. Confirmed that reverting to FastAPI 0.112.2 resolves the problem (`pip install fastapi==0.112.2`). Here are logs on the failure: ``` INFO: 172.16.10.6:40700 - "GET /v1/models HTTP/1.1" 200 OK INFO: 172.16.10.6:39032 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/pydantic/type_adapter.py", line 277, in _init_core_attrs self._core_schema = _getattr_no_parents(self._type, '__pydantic_core_schema__') File "/usr/local/lib/python3.10/dist-packages/pydantic/type_adapter.py", line 119, in _getattr_no_parents raise AttributeError(attribute) AttributeError: __pydantic_core_schema__ During handling of the above exception, another exception occurred: Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi r...

## 现有链接修复摘要

#8251 [Bugfix][Frontend] Update all fastapi requests based on OpenAPIBase with annotations | #8767 [Bugfix] Ray 2.9.x doesn't expose available_resources_per_node

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Confirmed that reverting to FastAPI 0.112.2 resolves the problem (`pip install fastapi==0.112.2`). Here are logs on the failure: ``` INFO: 172.16.10.6:40700 - "GET /v1/models HTTP/1.1" 200 OK INFO: 172.16.10.6:39032 - "...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ter.py", line 264, in __init__ self._init_core_attrs(rebuild_mocks=False) File "/usr/local/lib/python3.10/dist-packages/pydantic/type_adapter.py", line 142, in wrapped return func(self, *args, **kwargs) File "/usr/local...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ere are logs on the failure: ``` INFO: 172.16.10.6:40700 - "GET /v1/models HTTP/1.1" 200 OK INFO: 172.16.10.6:39032 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application T...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8251](https://github.com/vllm-project/vllm/pull/8251) | closes_keyword | 0.95 | [Bugfix][Frontend] Update all fastapi requests based on OpenAPIBase with annotations | FIX #8212 --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> <summary><b> PR Checklist (Click to Expand) </b>< |
| [#8767](https://github.com/vllm-project/vllm/pull/8767) | mentioned | 0.6 | [Bugfix] Ray 2.9.x doesn't expose available_resources_per_node | lable. To maintain Ray 2.9 compat we also need the fastapi bump in #8212 to be reverted, as [mentioned in this comment](https://github.com/vllm-project/vllm/issues/8212#issuecomme… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
