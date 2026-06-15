# vllm-project/vllm#10713: [Usage]: vllm infer with 2 * Nvidia-L20, output repeat !!!!

| 字段 | 值 |
| --- | --- |
| Issue | [#10713](https://github.com/vllm-project/vllm/issues/10713) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm infer with 2 * Nvidia-L20, output repeat !!!!

### Issue 正文摘录

### Your current environment vllm==0.6.1 ### How would you like to use vllm Steps to reproduce This happens to Qwen2.5-32B-Instruct-AWQ The problem can be reproduced with the following steps: start vllm service ``` exec python3 -m vllm.entrypoints.openai.api_server\ --served-model-name ${model_name}\ --model ./${model_name}\ --port 8890 \ --quantization awq \ --tensor-parallel-size 2 \ --enable_auto_tool_choice \ --tool-call-parser hermes 1>vllm.log 2>&1 & ``` infer ``` system_prompt = "你是一个安全专家，你的任务是根据用户的输入，以markdown格式返回结果。" query = "什么是SSRF漏洞" messages = [{"role": "system", "content": system_prompt}] messages.append({"role": "user", "content": query}) completion = client.chat.completions.create( model=model_name, messages=messages, temperature=0.1, top_p=0.9, max_tokens=4096, tools=[], extra_body={ "repetition_penalty": 1.05, }, ) req_id = completion.id total_token = completion.usage.total_tokens completion_token = completion.usage.completion_tokens prompt_tokens = completion.usage.prompt_tokens ``` output results The results are expected to be ... !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! with 2 A30, I didn't succeed in reproducing. But with L20，nearly 30% can re...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: with L20，nearly 30% can reproduce is the problem related to GPU type or cuda driver? Looking for help ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### How would you like to use vllm Steps to reproduce This happens to Qwen2.5-32B-Instruct-AWQ The problem can be reproduced with the following steps: start vllm service ``` exec python3 -m vllm.entrypoints.openai.api_s...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t environment vllm==0.6.1 ### How would you like to use vllm Steps to reproduce This happens to Qwen2.5-32B-Instruct-AWQ The problem can be reproduced with the following steps: start vllm service ``` exec python3 -m vll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! with 2 A30, I didn't succeed in reproducing. But with L20，nearly 30% can reproduce is the problem related to GPU type or cuda driver? Looking for help ### Before submitting a new issue.....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: el-name ${model_name}\ --model ./${model_name}\ --port 8890 \ --quantization awq \ --tensor-parallel-size 2 \ --enable_auto_tool_choice \ --tool-call-parser hermes 1>vllm.log 2>&1 & ``` infer ``` system_prompt = "你是一个安全...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
