# vllm-project/vllm#27746: [Bug]: `strict` value in function definitions causes request error when using Mistral tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#27746](https://github.com/vllm-project/vllm/issues/27746) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `strict` value in function definitions causes request error when using Mistral tokenizer

### Issue 正文摘录

### Your current environment Tested with latest vllm source build from main ### 🐛 Describe the bug Start vLLM with a model that uses the mistral tokenizer: ``` vllm serve mistralai/Mistral-Small-24B-Instruct-2501 \ --enable-auto-tool-choice \ --tool-call-parser mistral \ --tokenizer-mode mistral ``` Send a simple tool call request with the `strict` parameter set to a value of `False`: ```python from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="fake") tools = [ { "type": "function", "function": { "name": "get_current_time", "description": "Get the current time in UTC", "parameters": { "type": "object", "properties": {}, "required": [] }, "strict": False, } }, ] model = client.models.list().data[0].id response = client.chat.completions.create( model=model, messages=[{"role": "user", "content": "What is the current time?"}], tools=tools, ) print("Success!") ``` The request fails with a 400 error like: `openai.BadRequestError: Error code: 400 - {'error': {'message': '1 validation error for Tool\nfunction.strict\n Extra inputs are not permitted [type=extra_forbidden, input_value=False, input_type=bool]\n For further information visit https://errors...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: r bug;stale ### Your current environment Tested with latest vllm source build from main ### 🐛 Describe the bug Start vLLM with a model that uses the mistral tokenizer: ``` vllm serve mistralai/Mistral-Small-24B-Instruct...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model that uses the mistral tokenizer: ``` vllm serve mistralai/Mistral-Small-24B-Instruct-2501 \ --enable-auto-tool-choice \ --tool-call-parser mistral \ --tokenizer-mode mistral ``` Send a simple tool call request wit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t vllm source build from main ### 🐛 Describe the bug Start vLLM with a model that uses the mistral tokenizer: ``` vllm serve mistralai/Mistral-Small-24B-Instruct-2501 \ --enable-auto-tool-choice \ --tool-call-parser mis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: `strict` value in function definitions causes request error when using Mistral tokenizer bug;stale ### Your current environment Tested with latest vllm source build from main ### 🐛 Describe the bug Start vLLM wit...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: imple tool call request with the `strict` parameter set to a value of `False`: ```python from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="fake") tools = [ { "type": "function", "fu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
