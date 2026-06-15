# vllm-project/vllm#6499: [Bug]: When I use gemma2 27b, the openai.api returns content "" as none ChatCompletionMessage(content='', role='assistant', function_call=None, tool_calls=[])

| 字段 | 值 |
| --- | --- |
| Issue | [#6499](https://github.com/vllm-project/vllm/issues/6499) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When I use gemma2 27b, the openai.api returns content "" as none ChatCompletionMessage(content='', role='assistant', function_call=None, tool_calls=[])

### Issue 正文摘录

### Your current environment [Bug]: When I use gemma2 27b, the openai.api returns content "" as none ChatCompletionMessage(content='', role='assistant', function_call=None, tool_calls=[]) CUDA_VISIBLE_DEVICES=3 python -m vllm.entrypoints.openai.api_server --model model/gemma-2-27b-it --trust-remote-code --port 8001 --host localhost --dtype half --max-model-len 4096 --enforce-eager --disable_custom_all_reduce --api-key token-abc123 from openai import OpenAI client = OpenAI( base_url="http://localhost:8001/v1", api_key="token-abc123", ) completion = client.chat.completions.create( model="/work/jcxy/LLaMA-Factory/model/gemma-2-27b-it", messages=[ {"role": "user", "content": "Hello!"} ] ) print(completion.choices[0].message) result: ChatCompletionMessage(content='', role='assistant', function_call=None, tool_calls=[]) 2.And when I use curl, it also returns an empty value. curl http://localhost:8001/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "/work/jcxy/LLaMA-Factory/model/gemma-2-27b-it", "prompt": "San Francisco is a", "max_tokens": 12, "temperature": 0 }' {"id":"cmpl-a3599d01314b46eea5dbdf4881566a4a","object":"text_completion","created":1721200042,"model":...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: When I use gemma2 27b, the openai.api returns content "" as none ChatCompletionMessage(content='', role='assistant', function_call=None, tool_calls=[]) bug ### Your current environment [Bug]: When I use gemma2 27...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ce-eager --disable_custom_all_reduce --api-key token-abc123 from openai import OpenAI client = OpenAI( base_url="http://localhost:8001/v1", api_key="token-abc123", ) completion = client.chat.completions.create( model="/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: model/gemma-2-27b-it --trust-remote-code --port 8001 --host localhost --dtype half --max-model-len 4096 --enforce-eager --disable_custom_all_reduce --api-key token-abc123 from openai import OpenAI client = OpenAI( base_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Message(content='', role='assistant', function_call=None, tool_calls=[]) CUDA_VISIBLE_DEVICES=3 python -m vllm.entrypoints.openai.api_server --model model/gemma-2-27b-it --trust-remote-code --port 8001 --host localhost...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: When I use gemma2 27b, the openai.api returns content "" as none ChatCompletionMessage(content='', role='assistant', function_call=None, tool_calls=[]) bug ### Your current environment [Bug]: When I use gemma2 27...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
