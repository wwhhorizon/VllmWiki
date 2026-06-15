# vllm-project/vllm#3765: [Usage]: vllm does not return content for vicuna

| 字段 | 值 |
| --- | --- |
| Issue | [#3765](https://github.com/vllm-project/vllm/issues/3765) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm does not return content for vicuna

### Issue 正文摘录

### Your current environment hello, i follow your official documentation to use vllm. first is to start the server: ``` CUDA_VISIBLE_DEVICES=5 python -m vllm.entrypoints.openai.api_server \ --model "lmsys/vicuna-7b-v1.5-16k" --host '0.0.0.0' --port 4789 --dtype float16 --api-key token-abc123 ``` then call it ``` import openai,joblib print(openai.__version__) # 1.14.2 from openai import OpenAI client = OpenAI( base_url="http://36.111.143.5:4789/v1", api_key="token-abc123", ) prompt = joblib.load('./invoke_prompt.pkl') # print(prompt) res = client.chat.completions.create( model="lmsys/vicuna-7b-v1.5-16k", temperature=0, max_tokens=1024, messages=[ {"role": "system", "content": "You are a question answering assistant."}, {"role": "user", "content": "What is the capital city of British Columbia, Canada"} ] ) print(res) ``` however, i always get null content `ChatCompletionMessage(content='', role='assistant', function_call=None, tool_calls=None)` in the response. may I know if i miss something important ? thanks. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: icuna usage;stale ### Your current environment hello, i follow your official documentation to use vllm. first is to start the server: ``` CUDA_VISIBLE_DEVICES=5 python -m vllm.entrypoints.openai.api_server \ --model "lm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: --model "lmsys/vicuna-7b-v1.5-16k" --host '0.0.0.0' --port 4789 --dtype float16 --api-key token-abc123 ``` then call it ``` import openai,joblib print(openai.__version__) # 1.14.2 from openai import OpenAI client = Open...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r official documentation to use vllm. first is to start the server: ``` CUDA_VISIBLE_DEVICES=5 python -m vllm.entrypoints.openai.api_server \ --model "lmsys/vicuna-7b-v1.5-16k" --host '0.0.0.0' --port 4789 --dtype float...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: E_DEVICES=5 python -m vllm.entrypoints.openai.api_server \ --model "lmsys/vicuna-7b-v1.5-16k" --host '0.0.0.0' --port 4789 --dtype float16 --api-key token-abc123 ``` then call it ``` import openai,joblib print(openai.__...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: vllm does not return content for vicuna usage;stale ### Your current environment hello, i follow your official documentation to use vllm. first is to start the server: ``` CUDA_VISIBLE_DEVICES=5 python -m vllm....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
