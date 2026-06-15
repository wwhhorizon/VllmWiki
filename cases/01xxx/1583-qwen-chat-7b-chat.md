# vllm-project/vllm#1583: 如何使用千问大模型 qwen-chat-7b模型的chat 方法

| 字段 | 值 |
| --- | --- |
| Issue | [#1583](https://github.com/vllm-project/vllm/issues/1583) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 如何使用千问大模型 qwen-chat-7b模型的chat 方法

### Issue 正文摘录

我尝试使用vllm框架的示例， # Sample prompts. prompts = [ "你是谁", "你的名字是什么", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="/mnt/workspace/workgroup/Exps/zhangzai/model/Qwen-7B-Chat-v114",trust_remote_code= True) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) 输出： Prompt: '你是谁', Generated text: '，你在做什么，你在想什么。有人认为，这种意识流动是无' Prompt: '你的名字是什么', Generated text: '？\n3. 你来自哪里？\n4. 你喜欢什么样的活动？\n5' 我使用的是qwen-chat-7b模型 我发现vllm只有generate方法，输出也是续写。请问如何改造可以使用chat方法来输出指令形式的数据

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 如何使用千问大模型 qwen-chat-7b模型的chat 方法 我尝试使用vllm框架的示例， # Sample prompts. prompts = [ "你是谁", "你的名字是什么", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm =...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e_code= True) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) 输出： Promp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
