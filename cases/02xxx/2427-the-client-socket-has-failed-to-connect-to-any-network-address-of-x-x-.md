# vllm-project/vllm#2427: The client socket has failed to connect to any network address of ( x.x.x.x, 48247)

| 字段 | 值 |
| --- | --- |
| Issue | [#2427](https://github.com/vllm-project/vllm/issues/2427) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The client socket has failed to connect to any network address of ( x.x.x.x, 48247)

### Issue 正文摘录

I try to run the script below ``` from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="THUDM/chatglm2-6b",trust_remote_code=True) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` And met this error ``` [W socket.cpp:663] [c10d] The client socket has failed to connect to ?UNKNOWN? (errno: 110 - Connection timed out). [W socket.cpp:663] [c10d] The client socket has failed to connect to xxx:48247 (errno: 110 - Connection timed out). [E socket.cpp:719] [c10d] The client socket has failed to connect to any network address of (x.x.x.x, 48247). RuntimeError: The client socket has failed to connect to any network add...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="THUDM/chatglm2-6b",trust_remote_code=True) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ddress of ( x.x.x.x, 48247) I try to run the script below ``` from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: te_code=True) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
